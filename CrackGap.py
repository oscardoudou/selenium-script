import os
from PIL import Image

class CrackGap():
	def run(self):
		image1 = self.get_image('captcha3')
		image2 = self.get_image('captcha4')
		base = self.get_vertical_base(image1, image2)
		print base[1]
		# gap = self.get_gap(image1, base[1])
		# print gap

	def get_image(self, name):
		cwd = os.getcwd()
		png = Image.open(cwd + '/' + name + '.png')
		return png

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
		pixel_right = image.load()[x + 1, y]
		threshold = 120
		threshold2 = 60
		cnt = 0
		right = 0
		if abs(pixel[0] - pixel_up[0]) < threshold and abs(pixel[1] - pixel_up[1]) < threshold and abs(pixel[2] - pixel_up[2]) < threshold:
			cnt = cnt + 1
		if abs(pixel[0] - pixel_left[0]) < threshold and abs(pixel[1] - pixel_left[1]) < threshold and abs(pixel[2] - pixel_left[2]) < threshold:
			cnt = cnt + 1
		if abs(pixel[0] - pixel_down[0]) < threshold and abs(pixel[1] - pixel_down[1]) < threshold and abs(pixel[2] - pixel_down[2]) < threshold:
			cnt = cnt + 1
		if abs(pixel[0] - pixel_right[0]) < threshold and abs(pixel[1] - pixel_right[1]) < threshold and abs(pixel[2] - pixel_right[2]) < threshold:
			right = right + 1
		# sim = 0	
		# i = x
		# while i < 60  + x:
		# 	i = x + 3
		# 	pixel_right = image.load()[i, y]
		# 	if abs(pixel[0] - pixel_right[0]) < threshold2 and abs(pixel[1] - pixel_right[1]) < threshold2 and abs(pixel[2] - pixel_right[2]) < threshold2:
		# 		sim = sim + 1
		# print x , cnt, sim
		if cnt >= 3 and right == 1:
			return False
		else:
			return True

	def get_gap(self, image, height):
		#mostly gap start from 90
		for i in range(90, image.size[0] - 2 ):
			if not self.is_smooth_pixel(image, i, height):
				return i
		return 90