
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


@given('I want delete a user by id')
def step_impl(context):
    context.url = f'{config.get_endpoint()}{ApiResources.users}/{config.get_user_id()}'
    context.headers = {"Content-Type": "application/json"}
    log.allure_json('url param:',  context.url)


@when('the Users DELETE method is executed')
def step_impl(context):
    context.response = requests.delete(context.url, headers=context.headers, )

   
@then('the user should be deleted')
def step_impl(context):
     #Verify Status Code
    assert_that(context.response.status_code, 204)
    log.allure_log(f'Verified status code: {context.response.status_code}.')
