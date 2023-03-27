import os

def before_all(context):
    print("------Automation Started------")


def after_all(context):
    os.system(f'allure generate reports -o allure-report --clean')
    print("------Automation Finished------")
