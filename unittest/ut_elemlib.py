#!/usr/bin/env python

import elemlib

ret = elemlib.is_element("/home/fpemud/Virtual Machines/common")
assert ret

ret = elemlib.get_element_info("/home/fpemud/Virtual Machines/common")
print "type: " + ret.get_type()
print "name: " + ret.get_name()
print "comment: " + ret.get_comment()
print "source: " + str(ret.get_source())
print "author: " + str(ret.get_author())
print "homepage: " + str(ret.get_homepage())

ret = elemlib.open_element("/home/fpemud/Virtual Machines/common", "ro")
ret.close()

ret = elemlib.open_element("/home/fpemud/Virtual Machines/common", "rw")
ret.close()

