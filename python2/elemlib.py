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


class ElementError(Exception):
	pass

#class ElementChooserDialog:
#	pass

class Element:

	def __init__(self):
		# should prevent call from places other than openElement function
		pass

	def _init(self, path, mode):
		self.path = path
		self.open_mode = mode
		self.nameDict = []
		self.commentDict = []
		self.elem_type = ""
		self.elem_fp = None

		# check element file
		elemFile = os.path.join(path, os.path.basename(path) + ".elem")
		if not os.path.exists(elemFile):
			raise ElementError("Invalid element, no element file")

		# read element file
		cfg = ConfigParser.SafeConfigParser()
		cfg.read(elemFile)
		if not cfg.has_section("Element Entry"):
			raise ElementError("Invalid element, no [Element Entry] section in element file")

		# parse element file, ignore unknown properties
		for name, value in cfg.items("Element Entry"):
			m = re.match("^Name(\\[(.*)\\])?$", name)
			if m is not None:
				if m.group(1) == "":
					self.nameDict["C"] = value
				else:
					self.nameDict[m.group(2)] = value
				continue

			m = re.match("^Comment(\\[(.*)\\])?$", name)
			if m is not None:
				if m.group(1) == "":
					self.commentDict["C"] = value
				else:
					self.commentDict[m.group(2)] = value
				continue

			if name == "Type":
				self.elem_type = value
				continue


		if "C" not in self.nameDict:
			raise ElementError("Invalid element, no Name property in element file")
		if "C" not in self.commentDict:
			raise ElementError("Invalid element, no Comment property in element file")
		if self.elem_type == "":
			raise ElementError("Invalid element, no Type property in element file")

		# lock element, the lock will auto released if the process exits
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

	def get_name(self):
		return self.nameDict["C"]

	def get_comment(self):
		return self.commentDict["C"]

	def get_type(self):
		return self.elem_type

def is_element(path):
	assert os.path.isabs(path)

	if not os.path.isdir(path):
		return False

	elemFile = os.path.join(path, os.path.basename(path) + ".elem")
	if not os.path.exists(elemFile):
		return False

	return True

def open_element(path, mode):
	assert os.path.isabs(path)
	assert mode == "ro" or mode == "rw"

	if not os.path.isdir(path):
		raise ElementError("Invalid element, not a directory")

	ret = Element()
	ret._init(path, mode)
	return ret


