import sys

def test(did_pass):

    lineum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(lineum)
    else:
        msg = "Test at line {0} FAILED.".format(lineum)
    print(msg)

def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def test_suite():

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(1, 20, 20) == 100)
    test(to_secs(5, 1, 5) == 18065)

test_suite()


