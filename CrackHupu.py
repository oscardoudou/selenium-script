import os
import time
import urllib
from PIL import Image
from io import BytesIO
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
		#top, bottom, left, right = self.get_position()
		#print('verification img location', top, bottom, left, right)
		image1 = self.get_verify_image()
		print (self.get_screenshot())
		image2 =self.download_bg()
		base = self.get_vertical_base(image1, image2)
		print base
		height = base[1];
		print height
		res = self.get_gap(image1, height)
		print res
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
		# ActionChains(self.browser).move_by_offset(1,1).perform()
		# ActionChains(self.browser).move_by_offset(-1,-1).perform()

	def get_position(self):
		img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shumei_captcha_img_wrapper')))
		time.sleep(2)
		location = img.location
		size = img.size
		top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
		i = 1;
		#could be refractored 
		while top == 0.0:
			print i
			i = i + 1
			slider = self.get_slider()
			self.move_to_slider(slider)
			img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shumei_captcha_img_wrapper')))
			ActionChains(self.browser).move_by_offset(100,100).perform()
			time.sleep(1)
			ActionChains(self.browser).move_by_offset(-99,-99).perform()
			img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shumei_captcha_img_wrapper')))			
			time.sleep(4)
			location = img.location
			size = img.size
			top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
		return (top, bottom, left, right)

	def get_screenshot(self):
		#return self.browser.get_screenshot_as_file('/Users/zhangyichi/topic-trend-detector/foo.png')
		screenshot = self.browser.get_screenshot_as_png()
		screenshot = Image.open(BytesIO(screenshot))
		return screenshot

	def get_verify_image(self, name = 'captcha1.png'):
		top, bottom, left, right = self.get_position()
		print('verification img location', top, bottom, left, right)
		screenshot = self.get_screenshot()
		#captcha = screenshot.crop((left, top, right, bottom))
		captcha = screenshot.crop((880, 454, 1480, 754))
		captcha.save(name) 
		return captcha

	def download_bg(self):
		jpg = self.browser.find_element_by_class_name('shumei_captcha_loaded_img_bg')
		link = jpg.get_attribute("src")
		print link
		download = urllib.urlretrieve(link, "captcha2.png")
		#captcha = Image.open(BytesIO(download))
		cwd = os.getcwd()
		print cwd
		print cwd + "/captcha2.png"
		captcha = Image.open(cwd + '/captcha2.png')
		return captcha
		# img = urllib.urlopen(link)
		# image = Image.open

	def is_pixel_equal(self, image1, image2, x, y):
		pixel1 = image1.load()[x,y]
		pixel2 = image2.load()[x,y]
		threshold = 60
		if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
			return True
		else:
			return False

	def get_vertical_base(self, image1, image2):
		for i in range(2,image1.size[0] - 2):
			for j in range(3,image1.size[1] - 3):
				if not self.is_pixel_equal(image1,image2,i,j):
					return (i,j)
		return (0,0)

	def is_smooth_pixel(self, image, x, y):
		pixel = image.load()[x,y]
		pixel_up = image.load()[x, y - 2]
		pixel_left = image.load()[x - 1, y]
		pixel_down = image.load()[x, y + 2]
		threshold = 60
		sum = 0
		if abs(pixel[0] - pixel_up[0]) < threshold and abs(pixel[1] - pixel_up[1]) < threshold and abs(pixel[2] - pixel_up[2]) < threshold:
			sum = sum + 1
		if abs(pixel[0] - pixel_left[0]) < threshold and abs(pixel[1] - pixel_left[1]) < threshold and abs(pixel[2] - pixel_left[2]) < threshold:
			sum = sum + 1
		if abs(pixel[0] - pixel_down[0]) < threshold and abs(pixel[1] - pixel_down[1]) < threshold and abs(pixel[2] - pixel_down[2]) < threshold:
			sum = sum + 1
		if sum > 1:
			return True
		else:
			return False

	def get_gap(self, image, height):
		#mostly gap start from 90
		for i in range(90, image.size[0] -2 ):
			if not self.is_smooth_pixel(image, i, height):
				return i
		return 60

