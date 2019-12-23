CREATE DATABASE IF NOT EXISTS CALENDAR;

CREATE TABLE beta_dimensions(
    Date	date
    Day	tinyint
    DaySuffix	char(2)
    Weekday	tinyint
    WeekDayName	varchar(10)
    IsWeekend	bit
    IsHoliday	bit
    HolidayText	varchar(64) NULL
    DOWInMonth	tinyint
    DayOfYear	smallint
    WeekOfMonth	tinyint
    WeekOfYear	tinyint
    ISOWeekOfYear	tinyint
    Month	tinyint
    MonthName	varchar(10)
    Quarter	tinyint
    QuarterName	varchar(6)
    Year	int
    MMYYYY	char(6)
    MonthYear	char(7)
    FirstDayOfMonth	date
    LastDayOfMonth	date
    FirstDayOfQuarter	date
    LastDayOfQuarter	date
    FirstDayOfYear	date
    LastDayOfYear	date
    FirstDayOfNextMonth	date
    FirstDayOfNextYear	date
);