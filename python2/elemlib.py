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
import fcntl
import errno
from gi.repository import GLib

__author__ = "fpemud@sina.com (Fpemud)"

__version__ = "0.0.1"


class ElementError(Exception):
	pass

class ElementValidateError(ElementError):
	pass

class ElementAccessError(ElementError):
	pass

class ElementInfo:

	def __init__(self):
		self.kf = None

	def load(self, elem_path):
		# check element file
		elemFile = os.path.join(elem_path, "element.ini")
		if not os.path.exists(elemFile):
			raise ElementValidateError("no element file")

		# read element file
		self.kf = GLib.KeyFile()
		self.kf.load_from_file(elemFile, GLib.KeyFileFlags.NONE)
		if not self.kf.has_group("Element Entry"):
			raise ElementValidateError("no [Element Entry] section in element file")
		if self.kf.get_value("Element Entry", "Name") is None:
			raise ElementValidateError("no Name property in element file")
		if self.kf.get_value("Element Entry", "Type") is None:
			raise ElementValidateError("no Type property in element file")
		if self.kf.get_value("Element Entry", "Format") is not None:
			s = self.kf.get_string("Element Entry", "Format")
			if s != "simple" and s != "full":
				raise ElementValidateError("invalid Format property in element file")

	def get_type(self):
		return self.kf.get_string("Element Entry", "Type")

	def get_name(self):
		return self.kf.get_locale_string("Element Entry", "Name", None)

	def get_comment(self):
		try:
			return self.kf.get_locale_string("Element Entry", "Comment", None)
		except:
			return None

	def get_source(self):
		try:
			return self.kf.get_locale_string("Element Entry", "Source", None)
		except:
			return None

	def get_author(self):
		try:
			return self.kf.get_locale_string("Element Entry", "Author", None)
		except:
			return None

	def get_homepage(self):
		try:
			return self.kf.get_string("Element Entry", "Homepage")
		except:
			return None

	def _get_format(self):
		value = self.kf.get_string("Element Entry", "Format")
		if value is None:
			return "simple"
		else:
			return value

class Element:

	def __init__(self):
		# should prevent call from places other than openElement function
		pass

	def _init(self, path, mode):
		self.path = path
		self.open_mode = mode
		self.elem_info = None
		self.elem_fp = None

		if not os.path.isdir(path):
			raise ElementValidateError("not a directory")

		self.elem_info = ElementInfo()
		self.elem_info.load(self.path)

		# lock element, the lock will auto released if the process exits
		elemFile = os.path.join(path, "element.ini")
		self.elem_fp = open(elemFile, "r")
		try:
			if mode == "ro":
				fcntl.flock(self.elem_fp, fcntl.LOCK_SH | fcntl.LOCK_NB)
			elif mode == "rw":
				fcntl.flock(self.elem_fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
			else:
				assert False
		except Exception as e:
			self.elem_fp.close()			
			if isinstance(e, IOError) and (e.errno == errno.EAGAIN or e.errno == errno.EACCES):
				raise ElementAccessError("not accessible using mode \"%s\""%(mode))
			else:
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

	def get_data_dir(self):
		if self.elem_info._get_format() == "full":
			return os.path.join(self.path, "data")
		else:
			return self.path

	def get_cache_dir(self):
		if self.elem_info._get_format() == "full":
			return os.path.join(self.path, "cache")
		else:
			return None

	def get_revision_dirs(self):
		"""Returns directory list, the revision should be applied one by one"""

		ret = []
		if self.elem_info._get_format() == "full":
			ret.append(os.path.join(self.path, "revision"))
		return ret

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

	ret = Element()
	ret._init(path, mode)
	return ret

