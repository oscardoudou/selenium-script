import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

USERNAME = '13612062189'
PASSWORD = 'zhych2608250308'

class CrackHupu():
	def __init__(self):
		self.username = USERNAME
		self.password = PASSWORD
		self.url = 'https://passport.hupu.com/pc/login?project=soccer&from=pc'
		self.browser = webdriver.Chrome(executable_path = "./driver/chromedriver")
		self.wait = WebDriverWait(self.browser, 20)

	def __del__(self):
		self.browser.close()

	def run(self):
		#input username password
		self.open()
		#get slider 
		slider = self.get_slider()
		#move cursor to slider 
		self.move_to_slider(slider)
		user_choice = raw_input('Please click ENTER button to close application')
		top, bottom, left, right = self.get_position()
		print('verification img location', top, bottom, left, right)
		if not user_choice:
			print "ABORTED"
			quit()

	def open(self):
		# browser = webdriver.Chrome(executable_path = "./driver/chromedriver")
		# browser.get('https://passport.hupu.com/pc/login?project=soccer&from=pc')
		self.browser.get(self.url)
		email = self.wait.until(EC.presence_of_element_located((By.ID, 'J_username')))
		password = self.wait.until(EC.presence_of_element_located((By.ID, 'J_pwd')))
		email.send_keys(self.username)
		password.send_keys(self.password)

	def get_slider(self):
		slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'shumei_captcha_slide_btn')))
		return slider

	def move_to_slider(self, slider):
		ActionChains(self.browser).move_to_element(slider).perform()

	def get_position(self):
		img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shumei_captcha_img_wrapper')))
		time.sleep(2)
		location = img.location
		size = img.size
		top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
		return (top, bottom, left, right)