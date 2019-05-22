def is_year_leap(year):
    assert isinstance(year, int)
    assert year >= 0
    return year % 4 == 0


# let's test
print(is_year_leap(2000))   # true
print(is_year_leap(2002))   # false
print(is_year_leap(2.5))    # error
