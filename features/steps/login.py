
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


@given('the user exists in the system')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.login
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addLoginPayload(config.get_email(), config.get_password())
    log.allure_json('Request body:', context.payLoad)


@given('the user non-exists in the system')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.login
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addLoginPayload("non-existe@test.com", config.get_password())
    log.allure_json('Request body:', context.payLoad)


@given('I try login without password')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.login
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addLoginPayload(config.get_email(), "")
    log.allure_json('Request body:', context.payLoad)



@given('I try login without email')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.login
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addLoginPayload("", config.get_password())
    log.allure_json('Request body:', context.payLoad)


@when('the Login post method is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    log.allure_json('Response body: ', context.response.json())



@then('I should get the "Missing password" error')
def step_impl(context):
    response_body = context.response.json()

    assert_that("Missing password", response_body["error"])
    log.allure_log('Verified Error: ' + response_body["error"])

    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.error(), status_code=400)


@then('the user should login successfully')
def step_impl(context):
    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.login())
    


@then('I should get the "user not found" error')
def step_impl(context):
    response_body = context.response.json()

    assert_that("user not found", response_body["error"])
    log.allure_log('Verified Error: ' + response_body["error"])

    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.error(), status_code=400)


@then('I should get the "Missing email or username" error')
def step_impl(context):
    response_body = context.response.json()

    assert_that("Missing email or username", response_body["error"])
    log.allure_log('Verified Error: ' + response_body["error"])

    #Verify status code, headers and schema
    response_assertion.verify_response(context, schema=schema.error(), status_code=400)


