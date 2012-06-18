#!/usr/bin/python
#-*- coding: utf-8 -*-







import os, sys, signal, codecs, re, optparse
import pygame
from pygame import gfxdraw






#this is here because the world is a big trashbin, i mean, notepad
#[x for x in S if P(x)]
def any(S):
	for x in S:
		if x:
		   return True
	return False

def all(S):
	for x in S:
		if not x:
		   return False
	return True







options = [
u"↑\"story\" by author",
"file of ... (owned by another project) is called \"...\".",
"... is ... that varies",
"[  ]"
]
options.reverse()
menu = options
lines = [l.rstrip() for l in open("idit.py").readlines()]



scrh = 600
vshift = 0#lines
lives = 1
linenum = 0
llm = 10 # lines left margin
cursorx = 0



pygame.init()
pygame.display.set_caption("idit")
pygame.key.set_repeat(300,30)
screen_surface = pygame.display.set_mode((1000,scrh))



font = pygame.font.SysFont('monospace', 16)
bold = pygame.font.SysFont('monospace', 16, True)
f= font.render(" ",False,(0,0,0)).get_rect()
fonth = f.height
fontw = f.width
screenlines = scrh / fonth
f=None



def getline(l):
	if l<0:
		return ""
	if l>=len(lines):
		return ""
	return lines[l]

def setline(text,l):
	global lines
	if l<0:
		for i in range(-1,l-1,-1):
			lines.insert(0,"")
			l+=1
	lines[l] = text

def gettext():
	return getline(linenum)

def settext(text):
	global lines
	lines[linenum] = text






def edit(event):
	global cursorx
	if event.key==pygame.K_BACKSPACE:
		if cursorx > 0 and cursorx <= len(gettext()):
			settext(gettext()[0:cursorx-1]+gettext()[cursorx:])
			cursorx -=1
	elif event.key==pygame.K_DELETE:
		if cursorx >= 0 and cursorx < len(gettext()):
			settext(gettext()[0:cursorx]+gettext()[cursorx+1:])
	if event.unicode:
		settext(gettext()[0:cursorx]+event.unicode+gettext()[cursorx:])
		cursorx +=1




def bye():
	pygame.display.iconify()
	exit()
	
	
def save():
	out = lines
	story = open("story.ni", "w")
	sys.stdout.write( "sav" )
	for text in out[:]:
		if len(text) and text[0] == u"↑":
			story.write(text[1:]+"\n")
			out.remove(text)
	print "ing..."
	for text in out[:]:
		if len(text) and text[0] != u"↑" or not len(text):
			story.write(text+"\n")
			out.remove(text)









def control(event):
	global linenum,cursorx,vshift,lives


	# up & down
	if event.key == pygame.K_DOWN:
		linenum+=1
		if linenum > vshift + screenlines: vshift +=1
	if event.key == pygame.K_UP:
		linenum-=1
		if linenum < vshift: vshift -=1

	# pg up & down
	if event.key == pygame.K_PAGEDOWN:
		linenum+=10
		while linenum > vshift + screenlines:
			vshift +=1
	if event.key == pygame.K_PAGEUP:
		linenum-=10
		while linenum < vshift:
			vshift -=1

	# left & right
	if event.key == pygame.K_LEFT:
		if len(gettext()) and gettext()[0] == u"×":
			for x in lines[:]:
				if len(x) and x[0] == u"×":
					lines.remove(x)
		else:
			cursorx -= 1
	if event.key == pygame.K_RIGHT:
		if len(gettext()) == 0:
			for x in  menu:
				lines.insert(linenum,u"×"+x)
		else:
			cursorx += 1
			
			



	if event.key == pygame.K_HOME:
		cursorx = 0
	if event.key == pygame.K_END:
		cursorx = len(getline())




	if pygame.key.get_mods() & pygame.KMOD_RSHIFT:
		# œææºª¢º¡ª¢€ħðþ‘’–×
		l = getline()
		m = None
		if event.key == pygame.K_F1:
			if l[:1] != u"↑":
				m = u"↑"+l
			else:
				m = l[1:]
		if m: setline(m)




	if event.key == pygame.K_F8:
	        del lines[linenum]




	if event.scancode == 151 or event.key == pygame.K_F12:
	        #exit
		save()
		bye()
	if event.key == pygame.K_ESCAPE:
 		bye()
	if event.scancode == 37:#run?
		pass









def keypress(event):
	global cursorx
	control(event) or edit(event)









def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		keypress(event)








def damn_tabs():
        res = 0
        text = gettext()
        for i in range(0, cursorx):
                if i<len(text) and text[i] == '\t': res+=4
                else: res +=1
        return res

def draw():
	screen_surface.fill((0,0,0))
	
	for l in range(vshift,vshift+screenlines):
		h = l-vshift
		text = getline(l).replace("\t", "    ")
		if l==linenum:
			#cursor
			pygame.gfxdraw.circle(screen_surface, llm+int((damn_tabs()+0.5)*fontw), int((h+0.5)*fonth),5, (30,100,200))
			if not len(text) or not len(filter(lambda x:x != ' ',text)):
				pygame.gfxdraw.circle(screen_surface, llm+int(0.5*fontw), int((h+0.5)*fonth),5, (200, 200, 0))
			to_blit=bold.render(text,True,(255,255,255))
		else:
			to_blit=font.render(text,True,(255,255,255))#(220,255,220))

		screen_surface.blit(to_blit,(llm, h*fonth))
	
	pygame.display.update()









def loop():
	process_event(pygame.event.wait())
	draw()


while 1:
	try:
		loop()
	except KeyboardInterrupt() as e:
		pygame.display.iconify()
		raise e
	except Exception() as e:
		pass



