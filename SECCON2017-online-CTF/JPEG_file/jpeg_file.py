#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# Open image file on GIMP
# you can see GIMP message : 'Corrupt JPEG data: premature end of data segment Unsupported marker type 0xfc' 
# So, try to find '\xff\xfc'

data = open('problem.jpeg', 'rb').read()
data_list = list(data)

broken_spot = data.find('\xff\xfc')
data_list[broken_spot] = '\xfe'

open('flag.png', 'wb').write(''.join(data_list))
