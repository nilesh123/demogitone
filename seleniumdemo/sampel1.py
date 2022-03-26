from selenium import webdriver

driver = webdriver.Chrome(executable_path = 'D:\ejagruti_selenium_python\Drivers\chromedriver_win32\chromedriver.exe')
driver.get("file:///D:/Nilesh/D%20Drive/Selenium_all/Html%20task/Task1/signup.html")
driver.find_element_by_id('firstname').send_keys("Nilesh")