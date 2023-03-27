from behave import *
from utilities.api_resources import ApiResources
import utilities.configuration as config
import utilities.payload as payload
import requests
import utilities.logger as log
from json_schema_matchers.common_matcher import matches_json_schema
import utilities.schemas as schema
from hamcrest import assert_that


@given('we want register a new user')
def step_impl(context):
    context.url = config.get_endpoint() + ApiResources.register
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = payload.addRegisterPayload(config.get_email(), config.get_password())
    log.allure_json('Request body:', context.payLoad)


@when('the Register post method is executed')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    log.allure_json('Response body:', context.response.json())


@then('the user should be created')
def step_impl(context):
    response_body = context.response.json()

    #Verify status code
    assert context.response.status_code == 200
    log.allure_log(f'Verified status code: {context.response.status_code}.')

    #Verify  header
    assert 'application/json', context.response.headers['Content-Type'] 
    log.allure_log(f'Verified Content-Type: ' + context.response.headers['Content-Type'])

    #Verify  Schema
    assert_that(response_body, matches_json_schema(schema.register()))
    log.allure_json('Verified Response schema:', schema.register())

