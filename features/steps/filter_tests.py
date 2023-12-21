from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_welcome_page(context):
    context.app.welcome_page.open_welcome_page()


@when('Log in to the page')
def open_main_page(context):
    context.app.welcome_page.click_open_main_page()
    context.app.sign_in_page.sign_in()


@when('Click on “off plan” at the left side menu')
def open_off_plan_page(context):
    context.app.main_page.open_off_plan_page()

@when('Verify the right page opens')
def verify_off_page_opened(context):
    context.app.off_plan_page.verify_off_plan_opened()


@then('Filter by sale status of “Future Launch”')
def filter_by_future_launch(context):
    context.app.off_plan_page.filter_by_future_launch()

@then('Verify each product contains the Future Launch tag')
def filter_by_future_launch(context):
    context.app.off_plan_page.verify_each_future_launch_tag()