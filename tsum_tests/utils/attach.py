import json
from allure_commons.types import AttachmentType
import logging
import allure
import os


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    browser_name = browser.driver.capabilities['browserName']
    if browser_name == 'chrome':
        log = "".join(f'{text}\n'
                      for text in browser.driver.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = f"https://{os.getenv("SELENOID_URL")}/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def request_url_and_body(response):
    allure.attach(body=response.request.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")

    try:
        allure.attach(body=response.request.body, name="Request payload",
                  attachment_type=AttachmentType.TEXT, extension="txt")
    except (AttributeError, TypeError):
        print('Not body')



def response_json_and_cookies(response):
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")

    allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    
    allure.attach(body=str(response.headers), name="Headers", attachment_type=AttachmentType.TEXT, extension="txt")

def logging_response(response):
    logging.info(response.request.url)
    logging.info(response.status_code)
    logging.info(response.text)


def attach_bstack_video(session_id):
    import requests
    bstack_session = requests.get(
        f'{os.getenv("BS_API_SESSIONS")}/{session_id}.json',
        auth=(os.getenv("BS_LOGIN"), os.getenv("BS_PASS")),
    ).json()
    print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def attach_screenshot_and_dump(browser):
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )