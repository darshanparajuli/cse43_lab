# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. 

# Use days_in and is_leap_year in your advance_to function

import re

day_dict = {1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31}


def is_leap_year(month: int) -> bool:
    return (month % 4 == 0 and month % 100 != 0) or month % 400 == 0


def days_in(month: int, year: int) -> int:
    return (29 if month == 2 and is_leap_year(year) else day_dict[month])


def future_date(date: str, advance: int, year_now: int) -> str:
    match = re.match("^([1-9]|(1[0-2]))/((\s[1-9])|([0-2][0-9])|(3[01]))(/[0-9]{2})?$", date)
    assert match
    groups = match.groups()
    m = int(groups[0].strip())
    d = int(groups[2].strip())
    y = int('20' + groups[6].strip('/')) if groups[6] is not None else year_now
    assert d <= days_in(m, year_now) and advance >= 0
    d += advance
    while True:
        d_in_m = days_in(m, y)
        if d <= d_in_m:
            break
        d -= d_in_m
        m += 1
        if m == 13:
            m = 1
            y += 1
    return '{}/{}{}'.format(str(m), str(d), ('/' + str(y % 100)) if groups[6] is not None else '')


def compare_files(f1: open, f2: open) -> [(int, str, str)]:
    return [(a, b[0].rstrip('\n'), b[1].rstrip('\n')) for a, b in enumerate(zip(f1, f2), 1) if b[0] != b[1]]


if __name__ == '__main__':
    # Put your own function calls here to test the regular expressions
    #   or functions

    import driver

    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
