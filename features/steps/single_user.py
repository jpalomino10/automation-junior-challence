
from behave import *
from utilities.api_resources import ApiResources
import utilities.configuration as config
import utilities.payload as payload
import requests
import utilities.logger as log
from json_schema_matchers.common_matcher import matches_json_schema
import utilities.schemas as schema
from hamcrest import assert_that
import utilities.response_assertions as response_assertion


@given('I want search a user by id')
def step_impl(context):
    context.url = f'{config.get_endpoint()}{ApiResources.users}/{config.get_user_id()}'
    context.headers = {"Content-Type": "application/json"}
    log.allure_json('url param:',  context.url)


@given('I want search a non-exists user by id')
def step_impl(context):
    context.url = f'{config.get_endpoint()}{ApiResources.users}/0000000'
    context.headers = {"Content-Type": "application/json"}
    log.allure_json('url param:', context.url)


@when('the Users GET method is executed')
def step_impl(context):
    context.response = requests.get(context.url, headers=context.headers, )
    log.allure_json('Response body: ', context.response.json())


@then('the user should be founded')
def step_impl(context):
    response_body = context.response.json()
    data = response_body["data"]

    assert_that(4, data["id"])
    log.allure_log('Verified ID: ' + str(data["id"]))

    assert_that(config.get_email(), data["email"])
    log.allure_log('Verified Email: ' + data["email"])

    assert_that(config.get_first_name(), data["first_name"])
    log.allure_log('Verified First Name: ' + data["first_name"])

    assert_that(config.get_last_name(), data["last_name"])
    log.allure_log('Verified Last Name: ' + data["last_name"])

    assert_that(config.get_avatar(), data["last_name"])
    log.allure_log('Verified Avatar: ' + data["avatar"])

    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.users())


@then("I shouldn't get any result")
def step_impl(context):
    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.empty(), status_code=404)
    

