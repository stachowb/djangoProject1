from datetime import time, timedelta, date

# data and corresponding column in input file
DRIVER_NAME = 0
COMPANY_NAME = 1
EQ_REGNO = 2
EQ_TYPE = 3
CLOCK_IN = 4
CLOCK_OUT = 5
KM_DRIVEN = 11

# regular hourly rate per eq type
rates = {
    "Trekker": 522,
    "Containerbil m/løftelem": 537,
    "Containerbil": 537,
    "-": 537,
    "XV71109": 600
}
# bonus hourly rate
bonus_rate = 120

# when do we start to count the bonus hours, when do we start to count break, how long is the break
morning_limit = time(hour=6, minute=0)
evening_limit = time(hour=21, minute=0)
before_break = timedelta(hours=8, minutes=0)
break_time = timedelta(hours=0, minutes=30)

# holidays dates 2021
holidays = [date(2021, 5, 1), date(2021, 5, 13), date(2021, 5, 24)]

# weekend days as weekday() return
weekend = [5, 6]

# norwegian weekdays shortcuts
day_names_NO = {0: 'man.',
                1: 'tir.',
                2: 'ons.',
                3: 'tor.',
                4: 'fre.',
                5: 'lør.',
                6: 'søn.'}