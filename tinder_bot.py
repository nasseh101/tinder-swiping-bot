from selenium import webdriver
from time import sleep
from random import random
from secrets import email, password

class TinderBot():
  def __init__(self):
    self.driver = webdriver.Chrome()   

  def login(self):
    self.driver.get("https://tinder.com/")
    sleep(3)

    cls_cookies_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    cls_cookies_btn.click()

    try:
      fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button')
      fb_btn.click()
    except:
      try:
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        if fb_btn.text == 'LOG IN WITH FACEBOOK':
          fb_btn.click()
        else:
          more_options_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')  
          more_options_btn.click()
          fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
          fb_btn.click()
      except:
        more_options_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')  
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        fb_btn.click()

    base_window = self.driver.window_handles[0]
    self.driver.switch_to_window(self.driver.window_handles[1])

    email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
    email_in.send_keys(email)

    pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
    pw_in.send_keys(password)

    login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
    login_btn.click()
    self.driver.switch_to_window(base_window)

    sleep(6)


    # This closes the location and notification popus
    popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    popup_1.click()

    popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    popup_2.click()

    sleep(6)
    popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
    popup_3.click()


  def likes(self):
    like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
    like_btn.click()

  def dislikes(self):
    dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button')
    dislike_btn.click()

  def auto_swipe(self):
    while True:
      sleep(1)
      try:
        self.likes()
      except Exception:
        try:
          self.close_match_popup()  
        except:
          self.close_homescreen_popup  


  def close_match_popup(self):
    match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    match_popup.click()

  def close_homescreen_popup(self):
    homescreen_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')

bot = TinderBot()
bot.login()

