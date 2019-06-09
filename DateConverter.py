from datetime import datetime


def validate_month_or_day(date):
    if len(date) < 2:
        return '0' + date
    return date


class DateConverter:

    @staticmethod
    def get_current_year_string():
        return str(datetime.now().year)

    @staticmethod
    def get_current_month_string():
        current_month = str(datetime.now().month)
        return validate_month_or_day(current_month)

    @staticmethod
    def get_current_day_string():
        current_day = str(datetime.now().day)
        return validate_month_or_day(current_day)
