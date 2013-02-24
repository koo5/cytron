#!/usr/bin/python
#-*- coding: utf-8 -*-







import os, sys
import pygame
from pygame import gfxdraw






left_margin = 10
screen_height = 480







pygame.init()
pygame.display.set_caption("777")
pygame.key.set_repeat(300,30)
screen_surface = pygame.display.set_mode((640,screen_height))








font = pygame.font.SysFont('monospace', 16)
f= font.render(" ",False,(0,0,0)).get_rect()
fonth = f.height
fontw = f.width
screenlines = screen_height / fonth
f=None
left_margin = 12








code = [[["sin",None], ["5",None]],[["cos",None],["12",None]]]
cursorx = 0
wordx = 0
wordy = 0
#dictionary = [["thing",None], ["is a kind of",None], ["isaac newton",None], ["banana",None]]
hardcoded = [[a,a] for a in ["thing","is a kind of","is"]]
hardcoded +=[["a", "particle"],["an","particle"]]
dictionary = hardcoded
#todo: synonyma, struktury, #word
menu = []
menu_sel = 0



patterns={"kind declaration": ["something new", "is a kind of", "kind"],
"object declaration": ["something new", "is", "particle", "kind"]}
#command, print, expression

def matches(code, pattern):
	print "matching ",code," with ",pattern
	counter = 0
	for i in pattern:
		if code[counter][1] <> i:
			return False
		counter += 1
	return True

def update_dictionary():
	global dictionary
	dictionary = hardcoded
	for line in code:
		if matches(line, patterns["kind declaration"]):
			dictionary.append([line[0][0], "kind"])
		if matches(line, patterns["object declaration"]):
			dictionary.append([line[0][0], line[3][0]])
	print "dictionary is ", dictionary

def update_menu():
	global menu
#	make a list of all dictionary words beginning with the edited word
	menu = [i for i in dictionary if get_text() in i[0]]
	print "todays menu:", menu




def update_menu_sel():
	global menu_sel
	menu_sel = -1
	counter = 0
	for i in menu:
		if i[0] == get_text():
			menu_sel = counter
		counter += 1 


def set_meaning(x):
	code[wordy][wordx][1] = x
	print "meaning set to ", x



def set_text(w):
	global code
	code[wordy][wordx][0] = w

def get_text():
	return code[wordy][wordx][0]

def snapwordx():
	global wordx
	wordx = min(len(code[wordy]), wordx)
	if len(code[wordy]) == wordx:
		code[wordy].insert(0, ["",None])


def moveup():
	global wordy, code, wordx
	if wordy == 0:
		code = [] + code
		print "wut"
	else:
		wordy-=1
	snapwordx()

def movedown():
	global wordy, code, wordx
	wordy+=1
	if wordy >= len(code):
		code.append([])
	snapwordx()		

def moveright():
	global cursorx
	if cursorx < len(code[wordy][wordx]):
		cursorx += 1
	else:
		wordright()
def wordright():
	global wordx, code, cursorx
	wordx += 1
	if wordx >= len(code[wordy]):
		code[wordy].append("")
	cursorx = 0

def moveleft():
	global cursorx
	if cursorx > 0:
		cursorx -= 1
	else:	
		wordleft()

def wordleft():
	global wordx, cursorx
	if wordx > 0:
		wordx -= 1
		cursorx = len(code[wordy][wordx])







def initiate_new_word():
	menu_sel = 0













def getletters():
	letters = 0
	for i in range(0, wordx):
		letters += len(code[wordy][i][0])+1
	return letters




def draw():
	screen_surface.fill((0,0,0))

#text
	y = 0
	wy = 0
	for l in code:
		x = 0
		wx = 0
		for w in l:
			if (wx == wordx) and (wy == wordy):
				to_blit=font.render(w[0],True,(255,255,255))
			else:
				to_blit=font.render(w[0],True,(122,255,122))
			screen_surface.blit(to_blit,(left_margin+x, y))
			x = x + to_blit.get_width() + 10
			wx += 1
		y += fonth
		wy += 1

#cursor
	letters = getletters() + cursorx
	#print "cursorx is ",cursorx,", drawing cursor at ",letters," letters"	
	startpos = (left_margin+(letters*fontw), wordy*fonth)
	endpos   = (left_margin+(letters*fontw), (wordy+1)*fonth)
	pygame.draw.aaline(screen_surface, (200, 200, 0), startpos, endpos,3)

#menu
	letters = getletters()
	#wordy * fonth is the y position of the current word
	counter = 0
	for i in menu:
		if counter == menu_sel:
			color = (255,0,0)
		else:
			color = (200,0,0)
		to_blit=font.render(i[0],True,color)
		y = (wordy+counter+1) * fonth
		x = left_margin + letters * fontw
		screen_surface.blit(to_blit,(x, y))
		counter += 1





	pygame.display.update()












def control(event):
	global menu_sel,cursorx,code, wordx


	# up & down
	if event.key == pygame.K_DOWN:
		movedown()
	if event.key == pygame.K_UP:
		moveup()

	# pg up & down
	if event.key == pygame.K_PAGEDOWN:
		menu_sel +=1
	if event.key == pygame.K_PAGEUP:
		menu_sel -=1

	# left & right
	if event.key == pygame.K_LEFT:
		moveleft()
	if event.key == pygame.K_RIGHT:
		moveright()




	if event.key == pygame.K_HOME:
		cursorx = 0
		wordx = 0
	if event.key == pygame.K_END:
		wordx = -1+len(code[wordy][0])
		cursorx = len(get_text())



	if event.key == pygame.K_F8:
	        del code[wordy]



	if event.scancode == 151 or event.key == pygame.K_F12:
	        #exit
#		save()
		bye()
	if event.key == pygame.K_F10:
 		bye()

#	print "scancode ", event.scancode
	
	if event.unicode == ' ':
		if menu_sel <> -1:
			set_meaning(menu[menu_sel][1])
				

	update_menu()




def edit(event):
	global cursorx
	if event.key==pygame.K_BACKSPACE:
		print "backspace"
		if cursorx > 0 and cursorx <= len(get_text()):
			newtext = get_text()[0:cursorx-1]+get_text()[cursorx:]
			#print get_text(), "->", newtext
			set_text(newtext)
			cursorx -=1
	elif event.key==pygame.K_DELETE:
		if cursorx >= 0 and cursorx < len(get_text()):
			set_text(get_text()[0:cursorx]+get_text()[cursorx+1:])
	elif event.unicode:
		set_text(get_text()[0:cursorx]+event.unicode+get_text()[cursorx:])
		cursorx +=1
	else:
		return

	update_dictionary()
	update_menu()
	update_menu_sel()



def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		control(event) or edit(event)





def loop():
	process_event(pygame.event.wait())
	draw()








update_menu()









while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass













"""
todo:

pixel position of wordy is wordy * fonth

on drawing:
	draw menu:
		from pixel y of wordy down:

"""			