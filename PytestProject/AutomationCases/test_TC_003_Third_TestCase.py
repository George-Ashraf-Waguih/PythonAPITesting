import pytest


# Test case code must be written inside a method
# Method name must start with 'test'

@pytest.fixture(scope='module')
def fixture_code():
    print('-----------------------------')
    print('Fixture code before test case')
    print('-----------------------------')
    yield
    print('Close Connection after test case')
    print('-----------------------------')

@pytest.mark.Smoke
def test_tc_001_Login_logout(fixture_code):
    print("This is smoke test case code")
    print("This is the end of the test case")

@pytest.mark.Sanity
def test_tc_003_Login_Logout_Invalid_Credentials(fixture_code):
    print("This is Sanity test case code")
    print("This is the end of the test case")


# Print statement output display (-s)
# Print testcases names (-v)

