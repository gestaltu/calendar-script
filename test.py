from pprint import pprint
from collections import OrderedDict
import pendulum
import holidays

start_date = pendulum.datetime(2019, 1, 1)
end_date = pendulum.datetime(2020, 1, 2)
us_holidays = holidays.US()


def isWeekend(date):
    weekno = date.weekday()
    if weekno < 5:
        return 0
    else:
        return 1


while start_date <= end_date:
    info = OrderedDict()

    is_holiday = 0
    is_weekend = 0

    date_str = start_date.strftime("%Y-%m-%d-%H-%M")
    iso_week_of_year = start_date.isocalendar()[1]
    holiday_name = us_holidays.get(start_date, "Nill")
    if holiday_name != "Nill":
        is_holiday = 1

    info = {
        "Date": start_date.to_datetime_string(),
        "Day": start_date.strftime("%d"),
        "DaySuffix": start_date.format("Do")[-2:],
        "Weekday": start_date.weekday(),
        "WeekDayName": start_date.strftime("%A"),
        "IsWeekend": isWeekend(start_date),
        "HolidayText": holiday_name,
        "IsHoliday": is_holiday,
        "DOWInMonth": start_date.days_in_month,
        "DayOfYear": start_date.day_of_year,
        "WeekOfMonth": start_date.week_of_month,
        "WeekOfYear": start_date.week_of_year,
        "ISOWeekOfYear ": iso_week_of_year,
        "Month": start_date.strftime("%m"),
        "MonthName": start_date.strftime("%B"),
        "Quarter": start_date.quarter,
        "QuarterName": start_date.format('Qo'),
        "Year": start_date.strftime("%Y"),
        "MMYYYY": start_date.strftime("%m%Y"),
        "MonthYear": None,
        "FirstDayOfMonth": start_date.start_of('month').to_datetime_string(),
        "LastDayOfMonth": start_date.end_of('month').to_datetime_string(),
        "FirstDayOfQuarter":
            start_date.first_of('quarter').to_datetime_string(),
        "LastDayOfQuarter": start_date.last_of('quarter').to_datetime_string(),
        "FirstDayOfYear": start_date.start_of('year').to_datetime_string(),
        "LastDayOfYear": start_date.end_of('year').to_datetime_string(),
        "FirstDayOfNextMonth": None,
        "FirstDayOfNextYear": None,
    }
    pprint(info)
    start_date = start_date.add(minutes=1)
