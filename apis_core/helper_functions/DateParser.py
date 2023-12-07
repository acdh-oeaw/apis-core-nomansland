import math
import re
from datetime import datetime, timedelta
import convertdate


def parse_date( date_string: str ) -> (datetime, datetime, datetime):
    """
    function to parse a string date field of an entity

    :param date_string : str :
        the field value passed by a user

    :return date_single : datetime :
        single date which represents either the precise date given by user or median in between a range.

    :return date_ab : datetime :
        starting date of a range if user passed a range value either implicit or explicit.

    :return date_bis : datetime :
        ending date of a range if user passed a range value either implicit or explicit.
    """



    def get_last_day_of_month(month, year):
        """
        Helper function to return the last day of a given month and year (respecting leap years)

        :param month : int

        :param year : int

        :return day : int
        """

        if month in [1, 3, 5, 7, 8, 10, 12]:
            # 31 day months
            return 31
        elif month in [4, 6, 9, 11]:
            # 30 day months
            return 30
        elif month == 2:
            # special case february, differentiate leap years with respect to gregorian leap rules
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        # divisible by 4, by 100, by 400
                        # thus is leap year
                        return 29
                    else:
                        # divisible by 4, by 100, not by 400
                        # thus is not leap yar
                        return 28
                else:
                    # divisible by 4, not by 100, if by 400 doesn't matter
                    # thus is leap year
                    return 29
            else:
                # not divisible by 4, if by 100 or by 400 doesn't matter
                return 28
        else:
            # no valid month
            raise ValueError("Month " + str(month) + " does not exist.")


    try:

        # return variables
        date_single = None
        date_ab = None
        date_bis = None

        # split for angle brackets, check if explicit iso date is contained within them
        date_split_angle = re.split(r"(<.*?>)", date_string)


        if len(date_split_angle) > 1:

            # date string contains angle brackets. Parse them, ignore the rest

            def parse_iso_date(date_string):
                date_string_split = date_string.split("-")
                try:
                    return datetime(year=int(date_string_split[0]), month=int(date_string_split[1]), day=int(date_string_split[2]) )
                except:
                    raise ValueError("Invalid iso date: ", date_string)

            if len(date_split_angle) > 3:
                # invalid case
                raise ValueError("Too many angle brackets.")

            elif len(date_split_angle) == 3:
                # the right amount of substrings, indicating exactly one pair of angle brackets.
                # Parse the iso date in between

                # remove angle brackets and split by commas
                dates_iso = date_split_angle[1][1:-1]

                # check for commas, which would indicate that either one iso date or three are being input
                dates_iso = dates_iso.split(",")
                if len(dates_iso) != 1 and len(dates_iso) != 3:
                    # only either one iso date or three are allowed
                    raise ValueError(
                        "Incorrect number of dates given. Within angle brackets only one or three (separated by commas) are allowed.")

                elif len(dates_iso) == 3:
                    # three iso dates indicate further start and end dates

                    # parse start date
                    date_ab_string = dates_iso[1].strip()
                    if date_ab_string != "":
                        date_ab = parse_iso_date(date_ab_string)

                    # parse end date
                    date_bis_string = dates_iso[2].strip()
                    if date_bis_string != "":
                        date_bis = parse_iso_date(date_bis_string)

                # parse single date
                date_single_string = dates_iso[0].strip()
                if date_single_string != "":
                    date_single = parse_iso_date(date_single_string)
            return date_single, date_ab, date_bis

        date_string = date_string.lower().strip()
        date_ab = None
        date_bis = None
        date_single = None

        date_ext = None
        date_ah = False
        # check for century prefixes
        century = None
        
        date_prefixes = ["late", "before", "until"]
        date_prefix = None
        
        for d_prefix in date_prefixes:
            if d_prefix in date_string.lower():
                date_string = date_string.replace(d_prefix, "").strip()
                date_prefix = d_prefix
        
        for cent in re.finditer(r"(\d{1,2})c", date_string):
            century = int(cent.group(1))
            date_string = date_string.replace(cent.group(0), cent.group(1)).strip()

        # check for AH prefixes
        for ah in re.finditer(r"(\d{1,4}(-\d{1,2}-\d{1,2})?) ah", date_string):
            date_ext = ah.group(1)
            date_string = date_string.replace(ah.group(0), ah.group(1)).strip()
            date_ah = True

        if century is not None:
            if not date_ah:
                date_ab = datetime(year=century*100, month=1, day=1)
                date_bis = datetime(year=century*100+99, month=12, day=31)
                date_single = datetime(year=century*100+50, month=6, day=15)
            else:
                date_ab = convertdate.islamic.to_gregorian(century*100, 1, 1)
                date_bis = convertdate.islamic.to_gregorian(century*100+99, 12, 29)
                date_single = convertdate.islamic.to_gregorian(century*100+50, 6, 15)

        # get prefixes first
        if date_ab is None and date_bis is None and date_single is None:
            date_regex = re.match(r"(\d{1,4})-?(\d{1,2})?-?(\d{1,2})?", date_string)
            if date_regex and not date_ah:
                if date_regex.group(3) is not None:
                    date_ab = datetime(year=int(date_regex.group(1)), month=int(date_regex.group(2)), day=int(date_regex.group(3)))
                    date_bis = date_ab
                    date_single = date_ab
                elif date_regex.group(2) is not None:
                    date_ab = datetime(year=int(date_regex.group(1)), month=int(date_regex.group(2)), day=1)
                    date_bis = datetime(year=int(date_regex.group(1)), month=int(date_regex.group(2)), day=get_last_day_of_month(int(date_regex.group(2)), int(date_regex.group(1))))
                    date_single = datetime(year=int(date_regex.group(1)), month=int(date_regex.group(2)), day=15)
                else:
                    date_ab = datetime(year=int(date_regex.group(1)), month=1, day=1)
                    date_bis = datetime(year=int(date_regex.group(1)), month=12, day=31)
                    date_single = datetime(year=int(date_regex.group(1)), month=6, day=15)
            elif date_regex and date_ah:
                if date_regex.group(3) is not None:
                    date_ab = convertdate.islamic.to_gregorian(int(date_regex.group(1)), int(date_regex.group(2)), int(date_regex.group(3)))
                    date_bis = date_ab
                    date_single = date_ab
                elif date_regex.group(2) is not None:
                    date_ab = convertdate.islamic.to_gregorian(int(date_regex.group(1)), int(date_regex.group(2)), 1)
                    date_bis = convertdate.islamic.to_gregorian(int(date_regex.group(1)), int(date_regex.group(2)), 29)
                    date_single = convertdate.islamic.to_gregorian(int(date_regex.group(1)), int(date_regex.group(2)), 15)
                else:
                    date_ab = convertdate.islamic.to_gregorian(int(date_regex.group(1)), 1, 1)
                    date_bis = convertdate.islamic.to_gregorian(int(date_regex.group(1)), 12, 29)
                    date_single = convertdate.islamic.to_gregorian(int(date_regex.group(1)), 6, 15)


    except Exception as e:
        print("Could not parse date: '", date_string, "' due to error: ", e)
        return None, None, None
    if isinstance(date_ab, tuple):
        date_ab = datetime(year=date_ab[0], month=date_ab[1], day=date_ab[2])
    if isinstance(date_bis, tuple):
        date_bis = datetime(year=date_bis[0], month=date_bis[1], day=date_bis[2])
    if isinstance(date_single, tuple):
        date_single = datetime(year=date_single[0], month=date_single[1], day=date_single[2])

    return date_single, date_ab, date_bis



def get_date_help_text_from_dates(single_date, single_start_date, single_end_date, single_date_written):
    """
    function for creating string help text from parsed dates, to provide feedback to the user
    about the parsing status of a given date field.

    :param single_date: datetime :
        the individual date point

    :param single_start_date: datetime :
        the start range of a date

    :param single_end_date: datetime :
        the endrange of a date

    :param single_date_written: str :
        the textual user entry of a date field (needed to check if empty or not)

    :return help_text: str :
        The text to be displayed underneath a date field, informing the user about the parsing result
    """


    # check which of the dates could be parsed to construct the relevant feedback text

    help_text = ""
    if single_date:
        # single date could be parsed

        help_text = "Date interpreted as "

        if single_start_date or single_end_date:
            # date has also start or end ranges, then ignore single date

            if single_start_date:
                # date has start range

                help_text += \
                    str(single_start_date.year) + "-" + \
                    str(single_start_date.month) + "-" + \
                    str(single_start_date.day) + " until "

            else:
                # date has no start range, then write "undefined"

                help_text += "undefined start until "

            if single_end_date:
                # date has end range

                help_text += \
                    str(single_end_date.year) + "-" + \
                    str(single_end_date.month) + "-" + \
                    str(single_end_date.day)

            else:
                # date has no start range, then write "undefined"

                help_text += "undefined end"

        else:
            # date has no start nor end range. Use single date then.

            help_text += \
                str(single_date.year) + "-" + \
                str(single_date.month) + "-" + \
                str(single_date.day)

    elif single_date_written is not None:
        # date input field is not empty but it could not be parsed either. Show parsing info and help text

        help_text = "<b>Date could not be interpreted</b><br>" + get_date_help_text_default()

    else:
        # date field is completely empty. Show help text only

        help_text = get_date_help_text_default()

    return help_text



def get_date_help_text_default():

    return "Please always use YYYY-MM-DD (or YYYY-MM) format for dates. If you want to add Hijri dates use 'AH' as postfix, eg. '1234-12-12 AH'. You can specify centuries by using 'c' as postfix, eg. '12c' or '12c AH'. You can also specify date ranges by using angle brackets, eg. '<1234-12-12, 1234-12-13>' or '<1234-12-12, 1234-12-13, 1234-12-14>'. Please note that in angel brackets only Gregorian ISO dates can be used."
