#!/usr/bin/python

#-*- coding: utf-8 -*-


import os, sys, signal, codecs, re, optparse
import pygame
from pygame import gfxdraw, font

pygame.init()

def init_screen():
    screen_surface = pygame.display.set_mode((800,300))
    screen_surface.fill((0,0,0))
    pygame.display.flip()

init_screen()

lives = 1
bits = [0 for bits in range(0, 8)]


""""""

colemak={}
colemak['top']  =  "qwfpgjluy;[]"
colemak['mid']  =  "arstdhneio'\\"
colemak['low']  =  "zxcvbkm,./"
colemak['low_shit']  = ['COMMA', 'PERIOD', 'SLASH']

key=colemak


""""""
""""""

radius = 40

""""""

font = font.SysFont('monospace', 8)

def kkk(key):
    return pygame.__dict__['K_'+key]

while lives:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lives = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            lives-=1

    row=key['low']


    for col in range(0, min(len(bits),len(row))):
        char = row[col]
        try:
            pygakey = kkk(char)
            print pygakey
        except Exception:
            try:
                pygakey = kkk(key['low_shit'][0])
            except Exception:
                pygakey = None
                print 'add '+char
        if pygakey and pygame.key.get_pressed()[pygakey]:
            bits[col] = not bits[col]
            x = radius+col*radius
            pygame.gfxdraw.circle(screen_surface, x,radius,radius, (0,100 if bits[col] else 0,0))
            txt = font.render(pygame.key.name(pygakey),False,(120,120,120))
            screen_surface.blit(txt,(x,radius))
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_LSHIFT:
            print "left shift pressed"
    pygame.display.flip()



