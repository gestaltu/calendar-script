from pprint import pprint
from collections import OrderedDict
import pendulum
import holidays
import mysql.connector

start_date = pendulum.datetime(2009, 1, 1)
end_date = pendulum.datetime(2030, 1, 2)
us_holidays = holidays.US()

#MYSQL CONFIG
config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cnx.autocommit = True


def db_insert(data):
    """Insert to  db"""
    sql = """INSERT INTO  beta_Dimensions  SET Date=%(Date)s,Day=%(Day)s,
    DaySuffix=%(DaySuffix)s,Weekday=%(Weekday)s,WeekDayName=%(WeekDayName)s,IsWeekend=%(IsWeekend)s,
    IsHoliday=%(IsHoliday)s,HolidayText=%(HolidayText)s,DOWInMonth=%(DOWInMonth)s,DayOfYear=%(DayOfYear)s,
    WeekOfMonth=%(WeekOfMonth)s,WeekOfYear=%(WeekOfYear)s,
    ISOWeekOfYear=%(ISOWeekOfYear)s,Month=%(Month)s,MonthName=%(MonthName)s,Quarter=%(Quarter)s,
    QuarterName=%(QuarterName)s,Year=%(Year)s,MMYYYY=%(MMYYYY)s,MonthYear=%(MonthYear)s,
    FirstDayOfMonth=%(FirstDayOfMonth)s,LastDayOfMonth=%(LastDayOfMonth)s,
    FirstDayOfQuarter=%(FirstDayOfQuarter)s,LastDayOfQuarter=%(LastDayOfQuarter)s,
    FirstDayOfYear=%(FirstDayOfYear)s,LastDayOfYear=%(LastDayOfYear)s,
    FirstDayOfNextMonth=%(FirstDayOfNextMonth)s,FirstDayOfNextYear=%(FirstDayOfNextYear)s
    """
    cursor = cnx.cursor()
    cursor.execute(sql, data)
    cursor.close()


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
        "DaySuffix": start_date.format('Do')[-2:],
        "Weekday": start_date.weekday(),
        "WeekDayName": start_date.strftime("%A"),
        "IsWeekend": isWeekend(start_date),
        "HolidayText": holiday_name,
        "IsHoliday": is_holiday,
        "DOWInMonth": start_date.days_in_month,
        "DayOfYear": start_date.day_of_year,
        "WeekOfMonth": start_date.week_of_month,
        "WeekOfYear": start_date.week_of_year,
        "ISOWeekOfYear": iso_week_of_year,
        "Month": start_date.strftime("%m"),
        "MonthName": start_date.strftime("%B"),
        "Quarter": start_date.quarter,
        "QuarterName": start_date.format('Qo'),
        "Year": start_date.strftime("%Y"),
        "MMYYYY": start_date.strftime("%m%Y"),
        "MonthYear": start_date.strftime("%B%Y"),
        "FirstDayOfMonth": start_date.start_of('month').to_datetime_string(),
        "LastDayOfMonth": start_date.end_of('month').to_datetime_string(),
        "FirstDayOfQuarter":
            start_date.first_of('quarter').to_datetime_string(),
        "LastDayOfQuarter": start_date.last_of('quarter').to_datetime_string(),
        "FirstDayOfYear": start_date.start_of('year').to_datetime_string(),
        "LastDayOfYear": start_date.end_of('year').to_datetime_string(),
        "FirstDayOfNextMonth":
            start_date.add(months=1).start_of('day').to_datetime_string(),
        "FirstDayOfNextYear":
            start_date.add(years=1).start_of('year').to_datetime_string(),
    }
    pprint(info)
    db_insert(info)
    start_date = start_date.add(minutes=1)
