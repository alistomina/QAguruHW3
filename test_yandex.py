from selene import browser, be, have

def test_find_course (browser_settings, browser_open):
    browser.element('[id="text"]').should(be.blank).type('QAGURU').press_enter()
    browser.element('[id="search-result"]').should(have.text('Курсы тестировщиков'))
    print("Success")

def test_find_wrong (browser_settings, browser_open):
    browser.element('[id="text"]').should(be.blank).type('рмонмгнпдшгидшгирл').press_enter()
    browser.element('[class="EmptySearchResults-Title"]').should(have.text('Ничего не нашли'))
    print("Success")