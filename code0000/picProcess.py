#!/usr/bin/python
#coding=utf-8
#@Author	: prefree
#@Date  	: 2016/5/20
#@Func		: 将你的QQ头像右上角加上一个红色数字, 类似微信未读消息数量类似的效果

from PIL import Image, ImageDraw, ImageFont
import os

class my_image(object):
	def __init__(self):
		self.im = None
		self.font = None
		self.w = None
		self.h = None
		return
	
	def open(self, name):
		self.im = Image.open(name)
		self.draw = ImageDraw.Draw(self.im)
		self.w = self.im.width
		self.h = self.im.height
		print "format:%r, mode:%r, w:%r, h:%r" %(self.im.format, self.im.mode, self.im.width, self.im.height)

	def setFont(self, font, size):
		#get a font, ttf format
		self.font = ImageFont.truetype(font, size)
		
	def drawText(self, pos, str, color):
		self.draw.text(pos, str, fill=color, font=self.font)
		self.im.show()
		self.im.save(str+'.jpg')


picName = raw_input("Input your picture name: ")
if not os.path.isfile(picName):
	print "Error: Your picture not exist"
	exit(0) 
img = my_image()
img.open("prefree.jpg");
img.setFont("DejaVuSansMono.ttf", 180)
img.drawText((img.w-180, 20), "4", (255, 0, 0))
