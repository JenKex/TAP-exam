from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.firefox
    context.browser = context.browser_type.launch()

# Runs at the start of each scenario
def before_scenario(context, scenario):
    # Open a new page, to prevent cookies to leak between tests. Set default timeout to something appropriate. Close the page in after_scenario.
    context.page = context.browser.new_page()
    context.page.set_default_timeout(100)
    context.url = "https://tap-ht25-testverktyg.github.io/exam/"

# Runs directly after each scenario - clean up to avoid memory leaks
def after_scenario(context, scenario):
    if context.page:
        context.page.close()

# Runs after all scenarios have finished - clean up
def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()