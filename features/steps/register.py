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

@given('we want register a new user')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.register
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addRegisterPayload(config.get_email(), config.get_password())
    log.allure_json('Request body:', context.payLoad)


@given('we try register a user without email')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.register
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addRegisterPayload("", config.get_password())
    log.allure_json('Request body:', context.payLoad)


@then('I should get an error message')
def step_impl(context):

    response_body = context.response.json()

    assert_that("Missing email or username", response_body["error"])
    log.allure_log('Verified Error: ' + response_body["error"])

    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.error(), status_code=400)


@when('the Register post method is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    log.allure_json('Response body: ', context.response.json())


@then('the user should be created')
def step_impl(context):
    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.register())

