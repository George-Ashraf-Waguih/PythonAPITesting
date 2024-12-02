import requests
from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given('the book details which needs to be added to library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-type": "'application/json"}
    context.payload = addBookPayload('1gawash', '299929')


@when('we execute the AddBook Post API method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    print(context.response.status_code)
    response_json = context.response.json()
    context.bookID = response_json['ID']
    print(context.bookID)
    assert response_json['Msg'] == 'successfully added'


@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-type": "'application/json"}
    context.payload = addBookPayload(isbn, aisle)


@given('I have github credentials')
def step_impl(context):
    # Session Managing
    context.se = requests.session()
    context.se.auth = auth = ('George-Ashraf-Waguih', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
