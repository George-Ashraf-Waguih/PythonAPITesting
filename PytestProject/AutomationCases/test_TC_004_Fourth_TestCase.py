import pytest


# Test case code must be written inside a method
# Method name must start with 'test'

a = 100

@pytest.mark.Smoke
def test_tc_001_Login_logout():
    print("This is smoke test case code")
    print("This is the end of the test case")

@pytest.mark.Sanity
# @pytest.mark.skipif(a=100, reason="Skipping this test case")
def test_tc_003_Login_Logout_Invalid_Credentials():
    print("This is Sanity test case code")
    print("This is the end of the test case")


# Print statement output display (-s)
# Print testcases names (-v)

