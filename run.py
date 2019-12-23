from datetime import datetime, timedelta
from pprint import pprint
import holidays
import pendulum

start_date = datetime(2019, 1, 1)
end_date = datetime(2020, 1, 2)
delta = timedelta(days=0, hours=0, minutes=1)
us_holidays = holidays.US()


def isWeekend(date):
    weekno = date.weekday()
    if weekno < 5:
        return 0
    else:
        return 1


while start_date <= end_date:
    is_holiday = 0
    is_weekend = 0

    date_str = start_date.strftime("%Y-%m-%d-%H-%M")
    iso_week_of_year = start_date.isocalendar()[1]
    holiday_name = us_holidays.get(start_date, "Nill")
    if holiday_name != "Nill":
        is_holiday = 1

    info = {
        "Date": date_str,
        "Day": start_date.strftime("%d"),
        "DaySuffix": None,
        "Weekday": start_date.weekday(),
        "WeekDayName": start_date.strftime("%A"),
        "IsWeekend": isWeekend(start_date),
        "HolidayText": holiday_name,
        "IsHoliday": is_holiday,
        "DOWInMonth": None,
        "DayOfYear": None,
        "WeekOfMonth": None,
        "WeekOfYear": None,
        "ISOWeekOfYear ": iso_week_of_year,
        "Month": start_date.strftime("%m"),
        "MonthName": start_date.strftime("%B"),
        "Quarter": None,
        "QuarterName": None,
        "Year": start_date.strftime("%Y"),
        "MMYYYY": start_date.strftime("%m%Y"),
        "MonthYear": None,
        "FirstDayOfMonth": None,
        "LastDayOfMonth": None,
        "FirstDayOfQuarter": None,
        "LastDayOfQuarter": None,
        "FirstDayOfYear": None,
        "LastDayOfYear": None,
        "FirstDayOfNextMonth": None,
        "FirstDayOfNextYear": None,
    }
    pprint(info)
    start_date += delta
