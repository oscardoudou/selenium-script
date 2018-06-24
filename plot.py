import os
from PIL import Image
import matplotlib.pyplot as plt
#import pylab
# import numpy as np
# from peakutils.peak import indexes

def image (name):
	cwd = os.getcwd()
	png =  Image.open(cwd + '/' + name + '.png')
	return png

def generate_plot (image1, image2, height):
	diff = [0] * image1.size[0]
	for i in range(image1.size[0]):
		diff_count = 0
		for j in range(image1.size[1]):
			if not is_pixel_equal(image1, image2, i, j):
				diff_count  += 1
		diff[i] = diff_count
	x = [0] * image1.size[0]
	for i in range(image1.size[0]):
		x[i] = i
	r = [0] * image1.size[0]
	g = [0] * image1.size[0]
	b = [0] * image1.size[0]
	rgb = [0] * image1.size[0] 
	for i in range(image1.size[0]):
		pixel = image1.load()[i,height]
		r[i] = pixel[0]
		g[i] = pixel[1]
		b[i] = pixel[2] 
		rgb[i] = r[i] + g[i] + b[i]

	#below plt could all changed to pylab
	plt.plot(x, diff, label = 'count of pixel diff vertical' , color = 'brown')
	# plt.xlabel('x - image width')
	# plt.ylabel('y - count of pixel diff vertical')
	plt.plot(x, r, label = 'r', color = 'red')
	plt.plot(x, g, label = 'g', color = 'green')
	plt.plot(x, b, label = 'b', color = 'blue')
	plt.plot(x, rgb, color = 'black')
	plt.title('help me locate crack')
	# dont forget the () after show, otherwise it wont show anything, dont blame your luck
	plt.show()
	# waves = indexes(np.array(diff), thres=7.0/max(diff), min_dist=20)
	# print waves[0], waves[1]
	# !! peak corresponding value make no sense to my case, since I dont't have 3rd and 4th peak, 
	# which mean I can't calculate the distance simply by minus. Moreover, the one who utilize peak is tackling with rectangle crack not irregular rectangle

def is_pixel_equal(image1, image2, x, y):
	#also could use image.getpixel(x,y) compare directly
	pixel1 = image1.load()[x,y]
	pixel2 = image2.load()[x,y]
	threshold = 60
	if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
		return True
	else:
		return False

image1 = image('captcha3')
image2 = image('captcha4')
generate_plot(image1, image2, 110)