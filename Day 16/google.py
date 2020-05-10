from selenium import webdriver

browser = webdriver.Chrome()

url = 'https://google.com'
browser.get(url)

"""
<input class="gLFyf gsfi name="q" type="text">
"""

name = "q"
search_el = browser.find_element_by_name(name)

"""
<inputname="btnK" type="submit">
"""

search_el.send_keys("Hello Ward")

submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
submit_btn_el.click()