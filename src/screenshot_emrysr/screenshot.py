#!/usr/bin/env python3
from urllib.parse import urlparse
import sys,asyncio,base64
from playwright.sync_api import sync_playwright

def uri_validator(x):
    if x == 'about:blank': return True
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

def main(inputurl):
    if not uri_validator(inputurl):
        raise Exception(f"Not valid url! {inputurl}")

    with sync_playwright() as p:
        for browser_type in [p.chromium]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto(inputurl)
            screenshot_bytes = page.screenshot()
            screenshot = base64.b64encode(screenshot_bytes).decode()
            browser.close()

    return screenshot

if __name__ == '__main__':
    url = str(sys.argv[1]).strip()
    print(main(url));
