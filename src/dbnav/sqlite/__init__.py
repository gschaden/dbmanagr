#!/usr/bin/env python
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

__all__ = ["databaseconnection", "sources"]

from os.path import expanduser
from os import getenv
from collections import OrderedDict

from dbnav import __drivers__
from dbnav.utils import module_installed
from dbnav.sources import Source
from .sources import DBExplorerSQLiteSource, NavicatSQLiteSource
from dbnav.options import Options
from .options import SQLiteOptionsParser

DRIVERS = OrderedDict([
    ('sqlite3', 'sqlite+pysqlite:///{file}')
])


def init_sqlite(uri, dbexplorer_config, navicat_config1, navicat_config2=None):
    Source.sources.append(DBExplorerSQLiteSource(uri, dbexplorer_config))
    Source.sources.append(NavicatSQLiteSource(uri, navicat_config1))
    if navicat_config2:
        Source.sources.append(NavicatSQLiteSource(uri, navicat_config2))


def init():
    module = module_installed(*DRIVERS.keys())
    if not module:
        return

    __drivers__.append(module)
    init_sqlite(
        DRIVERS[module],
        getenv(
            'DBEXPLORER_CFG',
            expanduser('~/.dbexplorer/dbexplorer.cfg')),
        getenv(
            'NAVICAT_CFG',
            expanduser('~/Library/Application Support/PremiumSoft CyberTech'
                       '/preference.plist')),
        getenv(
            'NAVICAT_CFG',
            expanduser('~/Library/Containers/com.prect.'
                       'NavicatEssentialsForSQLite/Data/Library/'
                       'Application Support/PremiumSoft CyberTech/'
                       'preference.plist'))
    )

    Options.parser['sqlite'] = SQLiteOptionsParser()
