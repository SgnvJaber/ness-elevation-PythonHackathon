from smart_assertions import soft_assert, verify_expectations

def verify_equals(actual, expected):
    assert actual == expected

def do_soft_assert(actual, expected):
    soft_assert(actual == expected)

def do_verify_expectations():
    verify_expectations()
