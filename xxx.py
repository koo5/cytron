#!/usr/bin/python
#-*- coding: utf-8 -*-




from collections import OrderedDict as d
import os, sys
import pygame
from pygame import gfxdraw










def refresh_palette_window():
    a = c["cytron"]["windows"]["palette"]
    a.clear()
    


c = d([
    windows:
    [
	palette:
	[
	    refresh: refresh_palette_window,
	    items: []
	    draw:   draw_palette_window
	]    
    
	editor:
	[
	    files=d([])
	    draw: draw_editor_window
	    
    ]	    
	    
    palette:d("root":"php file", 
			["root","php file"]:["name", "contents"],
			["root","php file","name"],  ".php"],
			
			

def keypress(x):
	global c
	a = c["windows"]["active"]
	a.keypress(x)




def process_event(event):
	if event.type == pygame.QUIT:
		bye()
	if event.type == pygame.KEYDOWN:
		keypress(event)



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




def draw():
	screen_surface.fill((0,0,0))
	
	pygame.display.update()





def draw_palette_window():
	global c
	a = c["windows"]["active"]

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
	

