# Create Screenshot
Uses python and Puppeteer to open headless browser to return a screenshot as a base64 encoded string
Intended for terminal use

## Example
Decode base64 string and save to disk as screenshot.png:

`$ ./screenshot https://bbc.co.uk | base64 -d > screenshot.png`

> requires python3 and base64

## Install
Install as venv package

`$ python -m venv venv`
`$ source venv/venv/bin/activate`
`$ pip install -r requirements.txt`
`$ playwright install`

## Run
Return base64 string of screenshot for example.com

`./screenshot.py https://example.com`

