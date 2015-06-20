#!/usr/bin/python3

import os
import sys
import argparse
import markdown

from cssextension import CssExtension

def parseArgs():
	parser = argparse.ArgumentParser('Create HTML document from markdown')
	parser.add_argument('input', type=str,
			help='input document')
	parser.add_argument('-o', '--output', type=str,
			help='output file')
	return parser.parse_args()

if __name__ == '__main__':
	args = parseArgs()

	with open(args.input, 'r') as f:
		markdowntext = f.read()

	markdocdir = os.path.dirname(os.path.realpath(__file__))
	cssextension = CssExtension(cssfile=markdocdir+'/default.css')
	htmltext = markdown.markdown(markdowntext, extensions=[cssextension,])

	if args.output:
		with open(args.output, 'w') as f:
			f.write(htmltext)
	else:
		sys.stdout.write(htmltext)
