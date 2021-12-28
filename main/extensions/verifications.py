import allure
from smart_assertions import soft_assert, verify_expectations


@allure.step("Verify actual value is as expected")
def verify_equals(actual, expected):
    assert actual == expected


@allure.step("Soft assert values")
def do_soft_assert(actual, expected):
    soft_assert(actual == expected)


@allure.step("Verify expectations")
def do_verify_expectations():
    verify_expectations()


@allure.step("Verify if key is a substring ")
def contains(word, key):
    assert key in word
