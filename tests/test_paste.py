# Copyright (c) 2013 Martin Abente Lahaye. - martin.abente.lahaye@gmail.com
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA.

import sys

from gi.repository import GObject

sys.path.append("..")
from gpaste.paste import Paste


def __phase3_failed_cb(paste, info):
    print '[FAILED] phase3: with %s' % str(info)
    loop.quit()


def __phase2_failed_cb(paste, info):
    print '[FAILED] phase2: with %s' % str(info)
    loop.quit()


def __phase1_failed_cb(paste, info):
    print '[FAILED] phase1: with %s' % str(info)
    loop.quit()


def __phase3_completed_cb(paste, info):
    print '[OK] phase3: with %s' % str(info)
    loop.quit()


def __phase2_completed_cb(paste, info):
    print '[OK] phase2: with %s' % info['result']['data']

    paste = Paste()
    paste.connect('completed', __phase3_completed_cb)
    paste.connect('failed', __phase3_failed_cb)
    paste.lists('tch', 1)


def __phase1_completed_cb(paste, info):
    print '[OK] phase1: with %s' % paste.id

    paste = Paste(paste.id)
    paste.connect('completed', __phase2_completed_cb)
    paste.connect('failed', __phase2_failed_cb)
    paste.show()


paste = Paste()
paste.connect('completed', __phase1_completed_cb)
paste.connect('failed', __phase2_failed_cb)
paste.create('import os', 'python', 'tch')

loop = GObject.MainLoop()
loop.run()
