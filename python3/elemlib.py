#!/usr/bin/env python

# elemlib.py - library for element operation
# Copyright (c) 2005-2013 Fpemud <fpemud@sina.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
elemlib

@author: Fpemud
@license: GPLv3 License
@contact: fpemud@sina.com
"""

import os
import re
import fcntl
import ConfigParser


__author__ = "fpemud@sina.com (Fpemud)"

__version__ = "0.0.1"


class InvalidElementError(Exception):
	pass

#class ElementChooserDialog:
#	pass

class ElementIniBuilderError(Exception):
	pass

class ElementIniBuilder:

	def __init__(self):
		self.etype = None
		self.name_dict = dict()
		self.comment_dict = dict()
		self.source = None
		self.author = None
		self.homepage = None

	def set_type(self, etype):
		assert isinstance(etype, str) and etype != ""
		self.etype = etype

	def set_name(self, lang, name):
		assert isinstance(lang, str) and lang != ""
		assert isinstance(name, str)
		self.name_dict[lang] = name

	def set_comment(self, lang, comment):
		assert isinstance(lang, str) and lang != ""
		assert isinstance(comment, str)
		self.name_dict[lang] = comment

	def set_source(self, source):
		assert source is None or isinstance(source, str)
		self.source = source

	def set_author(self, author):
		assert author is None or isinstance(author, str)
		self.author = author

	def set_homepage(self, homepage):
		assert homepage is None or isinstance(homepage, str)
		self.homepage = homepage

	def save(self, filename):
		assert os.path.basename(filename) == "element.ini"

		# do checking
		if self.etype is None:
			raise ElementIniBuilderError("no Type property")
		if "C" not in self.name_dict:
			raise ElementIniBuilderError("no Name property")
		if "C" not in self.comment_dict:
			raise ElementIniBuilderError("no Comment property")

		# write file
		f = open(filename, "w")
		f.write("[Element Entry]\n")

		f.write("Name=%s\n"%(self.name_dict["C"]))
		for k, v in self.name_dict.items():
			f.write("Name[%s]=%s\n"%(k, v))

		f.write("Comment=%s\n"%(self.comment_dict["C"]))
		for k, v in self.comment_dict.items():
			f.write("Comment[%s]=%s\n"%(k, v))

		f.write("Type=%s\n"%(self.etype))

		if self.source is not None:
			f.write("Source=%s\n"%(self.source))
		if self.author is not None:
			f.write("Author=%s\n"%(self.author))
		if self.homepage is not None:
			f.write("Homepage=%s\n"%(self.homepage))

		f.close()

class ElementInfo:

	def __init__(self):
		self.etype = None
		self.name_dict = dict()
		self.comment_dict = dict()
		self.source = None
		self.author = None
		self.homepage = None

	def load(self, elem_path):
		# check element file
		elemFile = os.path.join(elem_path, "element.ini")
		if not os.path.exists(elemFile):
			raise InvalidElementError("no element file")

		# read element file
		cfgparser = ConfigParser.SafeConfigParser()
		cfgparser.optionxform = str				# make option names case-sensitive
		cfgparser.read(elemFile)
		if not cfgparser.has_section("Element Entry"):
			raise InvalidElementError("no [Element Entry] section in element file")

		# parse element file, ignore unknown properties
		for name, value in cfgparser.items("Element Entry"):
			m = re.match("^Name(\\[(.*)\\])?$", name)
			if m is not None:
				if m.group(2) is None:
					self.name_dict["C"] = value
				else:
					self.name_dict[m.group(2)] = value
				continue

			m = re.match("^Comment(\\[(.*)\\])?$", name)
			if m is not None:
				if m.group(2) is None:
					self.comment_dict["C"] = value
				else:
					self.comment_dict[m.group(2)] = value
				continue

			if name == "Type":
				self.etype = value
				continue

			if name == "Source":
				self.source = value
				continue

			if name == "Author":
				self.author = value
				continue

			if name == "Homepage":
				self.homepage = value
				continue

		if "C" not in self.name_dict:
			raise InvalidElementError("no Name property in element file")
		if "C" not in self.comment_dict:
			raise InvalidElementError("no Comment property in element file")
		if self.etype is None:
			raise InvalidElementError("no Type property in element file")

	def get_type(self):
		return self.etype

	def get_name(self):
		return self.name_dict["C"]

	def get_comment(self):
		return self.comment_dict["C"]

	def get_source(self):
		return self.source

	def get_author(self):
		return self.author

	def get_homepage(self):
		return self.homepage

class Element:

	def __init__(self):
		# should prevent call from places other than openElement function
		pass

	def _init(self, path, mode):
		self.path = path
		self.open_mode = mode
		self.elem_info = None
		self.elem_fp = None

		self.elem_info = ElementInfo()
		self.elem_info.load(self.path)

		# lock element, the lock will auto released if the process exits
		elemFile = os.path.join(path, "element.ini")
		self.elem_fp = open(elemFile, "r")
		try:
			if mode == "ro":
				fcntl.flock(self.elem_fp, fcntl.LOCK_SH | fcntl.LOCK_NB)
			else:
				fcntl.flock(self.elem_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
		except:
			self.elem_fp.close()			
			raise

	def close(self):
		# unlock element
		fcntl.flock(self.elem_fp, fcntl.LOCK_UN)
		self.elem_fp.close()

	def get_path(self):
		return self.path

	def get_open_mode(self):
		return self.open_mode

	def get_info(self):
		return self.elem_info

def is_element(path):
	assert os.path.isabs(path)

	if not os.path.isdir(path):
		return False

	elemFile = os.path.join(path, "element.ini")
	if not os.path.exists(elemFile):
		return False

	return True

def get_element_info(path):
	assert os.path.isabs(path)

	elemInfo = ElementInfo()
	elemInfo.load(path)
	return elemInfo

def open_element(path, mode):
	assert os.path.isabs(path)
	assert mode == "ro" or mode == "rw"

	if not os.path.isdir(path):
		raise InvalidElementError("not a directory")

	ret = Element()
	ret._init(path, mode)
	return ret

