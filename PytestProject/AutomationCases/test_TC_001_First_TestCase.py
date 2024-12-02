import pytest


# Test case code must be written inside a method
# Method name must start with 'test'

a = 100
actual_result = 'Testing'

@pytest.mark.TopPriority
def test_tc_001_Login_logout():
    print("This is Smoke test case code")
    print("This is the end of the test case")
    assert actual_result == 'Testing1', "These 2 values are not the same"

@pytest.mark.TopPriority
# @pytest.mark.skipif(a=100, reason="Skipping this test case")
def test_tc_003_Login_Logout_Invalid_Credentials():
    print("This is Sanity test case code")
    print("This is the end of the test case")


# Print statement output display (-s)
# Print testcases names (-v)

