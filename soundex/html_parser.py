import requests
from bs4 import BeautifulSoup

TEST_URL = "https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md#avoid-using-taskrun-for-long-running-work-that-blocks-the-thread"


def get_body(html_text: str) -> str:
    return BeautifulSoup(html_text, "html.parser").find("body").get_text()


def get_text_from_url(url: str) -> str:
    html_text = requests.get(url)
    return get_body(html_text.text)
