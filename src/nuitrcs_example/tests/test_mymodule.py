# -*- coding: utf-8 -*-
# Copyright (C) YOUR NAME (2021)
#
# This file is part of nuitrcs_example.
#
# nuitrcs_example is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nuitrcs_example is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nuitrcs_example.  If not, see <http://www.gnu.org/licenses/>.

"""Unit test for nuitrcs_example.YOURMODULE classes
"""

from ..mymodule.mymodule import MyClass


class TestMyClass(object):
    def test_myclass(self):
        assert 1 == MyClass().return_one()
