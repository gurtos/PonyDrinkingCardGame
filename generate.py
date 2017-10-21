#!/usr/bin/python

import os
import json

#TODO Pozbyc sie tego importu
import inspect

CARDSDIR = 'cards'

IMAGEMAGICK = 'convert templates/c-%s.png \
	-page +38+181  "cards/%04d.png"\'[752x421!]\' \
	-page +164+44 -gravity center -size 640x80 -background transparent -font Equestria -pointsize %d caption:"%s" -gravity none \
	-page +44+660 -size 740x360 -font Noto-Sans-Display-Regular -pointsize %d caption:"%s" \
	-page +720+1100 -size 100x60 -pointsize 44 caption:"%04d" \
	-page +44+1068 -size 740x66 -font Z003-MediumItalic -pointsize %d caption:"%s" \
	-layers flatten out/%04d.png'

files = [x for x in os.scandir(CARDSDIR) if x.is_file() and x.name.endswith('.pc')]
os.system('mkdir -p out')
for file in files:
	file = open(file, 'r')
	#TODO Obsluga blendow
	card = json.loads( file.read() )
	file.close()
	os.system(IMAGEMAGICK % ( card['type'], card['number'], card['name-fs'], card['name'], card['text-fs'], card['text'], card['number'], card['quote-fs'], card['quote'], card['number']))
	print('Card ' + ( '%04d' % card['number'] ) + ' done' )