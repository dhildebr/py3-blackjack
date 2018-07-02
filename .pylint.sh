#!/bin/sh

# Disabled PyLint warnings:
# C0303: Trailing whitespace. Disabled to allow the indenting of empty lines.
# C0326: Whitespace surrounding operators/brackets/commas. Disabled to allow the
#   aligning of elements in long sequences into neat columns.
# W0311: Bad indentation. PyLint expects a four-space soft indent, I prefer two.

pylint --disable=C0303,C0326,W0311 ./*.py
