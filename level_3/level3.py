import mechanicalsoup

browser = mechanicalsoup.Browser()
URL = 'http://158.69.76.135/level1.php'


for l in range(4096):
    page = browser.get(URL)
    page_html = page.soup
    form = page_html.select('form')[0]
    print(form)
    form.select('input')[0]['value'] = 35

    browser.submit(form, page.url)
