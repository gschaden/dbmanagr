#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import glob
import codecs
from dbnav.writer import Writer

def params(dir, testcase):
    with codecs.open(path.join(dir, 'resources/%s' % testcase), encoding='utf-8', mode='r') as f:
        return map(lambda line: line.strip(), f.readlines())

def expected(dir, testcase):
    with codecs.open(path.join(dir, 'resources/expected/%s' % testcase), encoding='utf-8', mode='r') as f:
        return f.read()

def update_expected(dir, testcase, content):
    with codecs.open(path.join(dir, 'resources/expected/%s' % testcase), encoding='utf-8', mode='w') as f:
        return f.write(content)

def test_generator(f, command, dir, tc):
    def test(self):
        p, e = params(dir, tc), expected(dir, tc)
        items = f.run([command,
            '-l', 'debug',
            '-f', 'target/dbnavigator.log'] + p)
        actual = Writer.write(items)

        # WARNING: this is code that creates the expected output - only uncomment when in need!
        #update_expected(dir, tc, actual)

        self.assertEqual(e, actual)
    return test