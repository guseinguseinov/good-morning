from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.devtools.v140.page import search_in_resource


class Instagram:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.instagram.com/accounts/login/')

    def login(self, username, password):

        username_input = self.driver.find_element(By.NAME, 'username')
        password_input = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[3]/button')

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        sleep(15)

        verification_code_input = self.driver.find_element(By.NAME, 'verificationCode')
        confirm_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/form/div[2]/button')

        login_code = input('Your ig login code : ')
        sleep(15)
        verification_code_input.send_keys(login_code)
        confirm_button.click()
        sleep(15)

    def go_to_profile(self, profile_name='hilalizade'):
        self.driver.get(f"https://www.instagram.com/{profile_name}/")
        sleep(15)

    def send_message(self, msg=""):
        message_button = self.open_message_box()
        message_button.click()
        sleep(6)

        input = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[1]')
        input.click()

        message_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/p')

        message_box.text = 'asdad'

    def open_message_box(self):
        try:
            message_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[2]/div/div/div/div/div[2]/div')
        except :
            print("Something went wrong!")
            self.quit()
        else :
            return message_button

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()