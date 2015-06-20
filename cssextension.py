import markdown
import xml.etree.ElementTree as ET
from markdown.treeprocessors import Treeprocessor

headerTemplate = '''
<head>
<style>
{css}
</style>
</head>
'''

class CssTreeProcessor(Treeprocessor):
	def __init__(self, md, cssfile):
		self.cssfile = cssfile
		super().__init__(md)

	def run(self, root):
		# get a title
		titleText = None;
		for i in range(1, 7):
			h = root.find('h{0}'.format(i))
			if h != None:
				titleText = h.text
				break

		# add the css
		css = open(self.cssfile, 'r').read()
		header = ET.SubElement(root, 'head')
		style = ET.SubElement(header, 'style')
		style.text = css
		title = ET.SubElement(header, 'title')
		title.text = titleText

class CssExtension (markdown.Extension):
	def __init__(self, **kwargs):
		self.cssfile = kwargs['cssfile']
		del(kwargs['cssfile'])
		super().__init__(**kwargs)

	def extendMarkdown(self, md, md_globals):
		treeprocessor = CssTreeProcessor(md, cssfile=self.cssfile)
		treeprocessor.ext = self
		md.treeprocessors['css'] = treeprocessor
		md.stripTopLevelTags = 0
