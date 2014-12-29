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
from dbnav.model import database
from dbnav.model.databaseconnection import UriDatabaseConnection


class DatabaseTestCase(ParentTestCase):
    def test_init(self):
        """Tests the Database init method"""

        self.assertEqual(
            'db',
            database.Database(None, 'db').name
        )

    def test_autocomplete(self):
        """Tests the Database autocomplete method"""

        self.assertEqual(
            'user@host/db/',
            database.Database(
                UriDatabaseConnection(user='user', host='host'),
                'db').autocomplete()
        )
