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

from string import capwords

from dbnav.writer import FormatWriter
from dbnav.formatter import Formatter, DefaultFormatter


class SqlInsertWriter(FormatWriter):
    def __init__(self, options):
        FormatWriter.__init__(
            self,
            u'{0}',
            u'insert into {table} ({columns}) values ({values});')
        Formatter.set(DefaultFormatter())
        self.options = options

    def itemtostring(self, item):
        row = item.row
        exclude = item.exclude
        return self.item_format.format(
            table=self.options.escape_keyword(row.table.name),
            columns=self.create_columns(row, exclude),
            values=self.create_values(row, exclude))

    def create_columns(self, row, exclude):
        return u','.join(
            map(lambda col: self.options.escape_keyword(col.name),
                filter(
                    lambda col: col.name not in exclude,
                    row.table.columns)))

    def create_values(self, row, exclude):
        return u','.join(
            map(lambda col: self.options.format_value(None, row[col.name]),
                filter(
                    lambda col: col.name not in exclude,
                    row.table.columns)))


class SqlUpdateWriter(FormatWriter):
    def __init__(self, options):
        FormatWriter.__init__(
            self, u'{0}', u'update {table} set {values} where {restriction};')
        Formatter.set(DefaultFormatter())
        self.options = options

    def itemtostring(self, item):
        row = item.row
        exclude = item.exclude
        table = row.table
        return self.item_format.format(
            table=self.options.escape_keyword(table.name),
            values=self.create_values(row, exclude),
            restriction=self.create_restriction(
                row,
                filter(lambda col: col.primary_key, table.columns)))

    def create_values(self, row, exclude):
        return u', '.join(map(
            lambda col: self.options.restriction(
                None, col, '=', row[col.name], map_null_operator=False),
            filter(
                lambda col: not col.primary_key and col.name not in exclude,
                row.table.columns)))

    def create_restriction(self, row, pks):
        return u' and '.join(map(
            lambda col: self.options.restriction(
                None, col, '=', row[col.name]),
            pks))


class SqlDeleteWriter(FormatWriter):
    def __init__(self, options):
        FormatWriter.__init__(
            self, u'{0}', u'delete from {table} where {restriction};')
        Formatter.set(DefaultFormatter())
        self.options = options

    def prepare(self, items):
        # Fixes issue #4
        items.reverse()
        return items

    def itemtostring(self, item):
        row = item.row
        table = row.table
        return self.item_format.format(
            table=self.options.escape_keyword(table.name),
            restriction=self.create_restriction(
                row, filter(lambda col: col.primary_key, table.columns)))

    def create_restriction(self, row, pks):
        return u' and '.join(
            map(
                lambda col: self.options.restriction(
                    None, col, '=', row[col.name]),
                pks))


def yaml_format_entity(name):
    return capwords(name, '_').replace('_', '')


def yaml_format_field(name):
    s = yaml_format_entity(name)
    return s[:1].lower() + s[1:]


def yaml_field(col, table):
    if table and col in table.foreign_keys:
        fk = table.foreign_keys[col]
        return yaml_format_field(fk.b['table'])
    return yaml_format_field(col)


def yaml_value(col, table, value):
    if table and col in table.foreign_keys:
        fk = table.foreign_keys[col]
        return u'*{table}_{id}'.format(
            table=fk.b['table'].replace('_', ''),
            id=yaml_value(fk.b['name'], None, value))  # TO-DO!!!
    if value is None:
        return u'!!null null'
    if type(value) is float:
        return u'!!float %f' % value
    if type(value) is int:
        return u'!!int %d' % value
    if type(value) is bool:
        return u'!!bool %s' % unicode(value).lower()
    return value


class YamlWriter(FormatWriter):
    def __init__(self, options=None):
        FormatWriter.__init__(
            self, u'{0}', u"""{prefix}    - &{table}_{id} !!{package}.{model}
        {tuples}""")
        Formatter.set(DefaultFormatter())
        self.package = options.package
        self.last_table = None

    def itemtostring(self, item):
        row = item.row
        exclude = item.exclude
        table = row.table
        tablename = table.name.replace(
            '_', '')
        prefix = ''
        if self.last_table != table:
            if self.last_table:
                prefix = u"""
{0}s:
""".format(tablename)
            else:
                prefix = u"""{0}s:
""".format(tablename)
            self.last_table = table
        return self.item_format.format(
            table=tablename,
            id=row[0],
            prefix=prefix,
            package=self.package,
            model=yaml_format_entity(table.name),
            tuples=self.create_tuples(row, exclude))

    def create_tuples(self, row, exclude):
        return u"""
        """.join(map(
            lambda col: u'{0}: {1}'.format(
                yaml_field(col.name, row.table),
                yaml_value(col.name, row.table, row[col.name])),
            filter(lambda col: col.name not in exclude, row.table.columns)))


class FormattedWriter(FormatWriter):
    def __init__(self, options=None):
        FormatWriter.__init__(self, u'{0}', options.format)
        Formatter.set(DefaultFormatter())

    def itemtostring(self, item):
        d = dict(map(
            lambda col: (col.name, item.row[col.name]),
            item.row.table.columns))
        return self.item_format.format(**d)
