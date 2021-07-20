from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from datetime import datetime, timedelta
from .config import before_break, break_time, rates, weekend, morning_limit, evening_limit, holidays, bonus_rate
from apps.drivers.models import Driver


class Shift(models.Model):
    """
    Abstract representation of a single work-shift
    """
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=10)
    clock_in = models.CharField(max_length=120)
    clock_out = models.CharField(max_length=120)
    distance = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def calculate_distance_above_200(self):
        """
        calculates how many KM above 200 a driver has traveled during his shift (required for bonus calculations)
        :return:
        """
        return self.distance - 200 if self.distance > 200 else 0

    def calculate_shift_length(self):
        """
        calculates how long has the shift lasted
        """
        frt = '%d-%m-%Y %H:%M'

        clock_in_dt = datetime.strptime(self.clock_in, frt)
        clock_out_dt = datetime.strptime(self.clock_out, frt)

        shift_length = clock_out_dt - clock_in_dt

        if shift_length >= before_break:
            shift_length -= break_time
            shift_length = shift_length

        return shift_length

    def calculate_regular_pay(self):
        """
        calculates money owed only for regular hours (06:00 - 21:00)
        """
        if self.reg_number in rates:
            regular_pay = rates[self.reg_number] * float(self.calculate_shift_length().total_seconds() / 3600)
            return round(regular_pay, 2)
        else:
            regular_pay = rates[self.driver.get_vehicle_display()] * float(
                self.calculate_shift_length().total_seconds() / 3600)
            return round(regular_pay, 2)

    @staticmethod
    def end_day(date):
        """
        prepares an datetime object at the end of the day
        :param date: datetime.datetime object
        """
        return date.replace(hour=23, minute=59, second=59)

    @staticmethod
    def start_day(date):
        """
        prepares an datetime object at the start of the day
        :param date: datetime.datetime object
        """
        return date.replace(hour=0, minute=0)

    @staticmethod
    def create_time(date, limit):
        """
        prepares an datetime object with a shift date combined with the 06:00 or 21:00 limit (bonus hours)
        :param date: datetime.datetime object, limit: datetime.time object
        """
        return datetime.combine(date[0].date(), limit)

    @staticmethod
    def is_weekend(date):
        """
        checks if the shift has taken place during a holiday day extra payed)
        :param date: datetime.date object
        :return:
        """
        return date.weekday() in weekend

    @staticmethod
    def bonus_limit(date, limit):
        """
        prepares an datetime object with a shift date combined with the 06:00 or 21:00 limit (bonus hours)
        :param date: datetime.datetime object, limit: datetime.time object
        """
        return datetime.combine(date.date(), limit)

    def calculate_bonus_time(self):
        """
        calculates bonus time (time before 06:00 and 21:00). It also checks if the shift is happening during one day or
        overexceeds 24:00
        """
        frt = '%d-%m-%Y %H:%M'
        shift = []
        bonus_time = timedelta(0)
        start = 0
        end = 1

        clock_in = datetime.strptime(self.clock_in, frt)
        clock_out = datetime.strptime(self.clock_out, frt)

        # splitting shift into one-day span shifts
        shift.append([clock_in, clock_out])
        for date in shift:
            if date[start].date() != date[end].date():
                shift.append([date[start], self.end_day(date[start])])
                shift.append([self.start_day(date[end]), date[end]])
                shift.pop(0)

        for date in shift:
            if self.is_weekend(date[start]):
                bonus_time += date[end] - date[start]
            else:
                # morning limit
                if date[start] < self.bonus_limit(date[start], morning_limit) <= date[end]:
                    bonus_time += self.bonus_limit(date[start], morning_limit) - date[start]

                if date[start] < self.bonus_limit(date[start], morning_limit) > date[end]:
                    bonus_time += date[end] - date[start]

                # evening limit
                if date[end] > self.bonus_limit(date[end], evening_limit):
                    bonus_time += date[end] - self.bonus_limit(date[end], evening_limit)

                if date[end] > self.bonus_limit(date[end], evening_limit) < date[start]:
                    bonus_time += date[end] - date[start]

        if bonus_time > before_break:
            bonus_time -= break_time

        clock_in_date, _ = self.clock_in.split(' ')
        frt = '%d-%m-%Y'
        clock_in_date = datetime.strptime(clock_in_date, frt)
        if clock_in_date.date() in holidays:
            bonus_time = self.calculate_shift_length()

        return bonus_time

    def calculate_overhour_bonus(self):
        """
        calculates money owed for bonus hours
        :return:
        """
        return bonus_rate * float(self.calculate_bonus_time().total_seconds() / 3600)

    def calculate_distance_bonus(self):
        """
        calculates money owed for distance above 200KM
        :return:
        """
        return 7 * self.calculate_distance_above_200()

    def calculate_total(self):
        """
        sums up all the owed money for that shift
        :return:
        """
        return self.calculate_regular_pay() + self.calculate_overhour_bonus() + self.calculate_distance_bonus()

    def __str__(self):
        return f'{self.clock_in} - {self.clock_out}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.__str__())
        super(Shift, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('shift-view', kwargs={"slug": self.slug})


class Tag(models.Model):
    """
    Additional information connect to every shift (approved, payed, rejected etc...)
    """
    shift = models.ManyToManyField(Shift, blank=True, null=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('tag-list')
