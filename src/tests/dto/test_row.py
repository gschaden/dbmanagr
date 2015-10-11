# -*- coding: utf-8 -*-
#
# Copyright © 2014 René Samselnig
#
# This file is part of Database Navigator.
#
# Database Navigator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Database Navigator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Database Navigator.  If not, see <http://www.gnu.org/licenses/>.
#

from tests.testcase import ParentTestCase
from dbmanagr.dto import row


class RowTestCase(ParentTestCase):
    def test_getitem(self):
        """Tests the Row.__getitem__ method"""

        r = row.Row(row=[1, 'a'])

        self.assertIsNone(r[None])
        self.assertIsNone(r[u'table'])
        self.assertEqual(1, r[0])

    def test_from_json(self):
        """Tests the Row.from_json static method"""

        r = row.Row(row=[1, 'a'])

        self.assertEqual(
            r,
            row.Row.from_json({
                'table': None,
                'row': [1, 'a'],
                'autocomplete': None
            })
        )
