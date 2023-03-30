

from hamcrest import assert_that
import utilities.logger as log
from json_schema_matchers.common_matcher import matches_json_schema


def verify_response(context, schema, status_code=200):

    response_body = context.response.json() or {}

    #Verify Status Code
    assert_that(context.response.status_code, status_code)
    log.allure_log(f'Verified status code: {context.response.status_code}.')

    #Verify Headers
    assert_that('application/json', context.response.headers['Content-Type'])
    log.allure_log(f'Verified Content-Type: ' + context.response.headers['Content-Type'])

     #Verify Schema
    assert_that(response_body, matches_json_schema(schema))
    log.allure_json('Verified Response schema:', schema)