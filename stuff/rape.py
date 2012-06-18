#!/usr/bin/python
#-*- coding: utf-8 -*-


from visual import *
from visual.text import *
import time
import random
import string

scene.fullscreen=1
scene.background = (0,0,0)
scene.center = (0,0,0)




class node:
	def show():
		self.vis = box(pos=(0,0,0), radius=1)
		x,y,z=position
		self.text_vis = label(pos =(x,y,z-1), text =type(self), height=4, depth=2, color =(255,255,255))

class _container(node):
	def __init__(self, codes):
		self.codes = codes
	def run(self):
		for code in self.codes:
			code.run()
	def show():
		super()
		x,y,z = self.vis.pos
		pos = (x+100,y,z)
		for c in self.codes:
			pos[1] += 100
			c.show()
			c.vis.pos = pos
#
class _print (node):
	def __init__(self, text):
		self.what = what
	def run(self):
		if type(self.what) == String:
			print node.what
		elif type(node.what) == _expression:
			print

#
class _comment (node):
	def __init__(self, text):
		self.text = text

#
class node_list (node):
	def __init__(self, list):
		self.list = list

#
class node_foreach (node):
	def __init__(self, data, command):
		self.data = data
		self.command = command
	def run():
		pass
#		for x in self.data:
#
class _python_expression (node):
	def __init__(self, expression):
		self.expression = expression
	def run():
		return eval(self.expression)



def process(node):
	if (type(node) == "foreach"):
		if not generating:
			for x in node.data.list:
			    process(node.command.with_data(x))

	elif (type(node) == "expression"):
		if not generating:
			pass


program = [
_comment("lalala"),
_print("hello"),
_foreach(
 _list([' ','w','o','r','l','d']),
 _print(None)
),
_print(token_expression("int(time.time())"))
]

generating = None

for token in program:
	process(token)
