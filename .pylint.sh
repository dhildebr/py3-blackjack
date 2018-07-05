#!/bin/sh

# Disabled PyLint warnings:
# C0301: I prefer lines up to 120 characters long, compared to PyLint's 100
#   (you can blame Eclipse for that habit).
# C0303: Trailing whitespace. Disabled to allow the indenting of empty lines.
# C0326: Whitespace surrounding operators/brackets/commas. Disabled to allow the
#   aligning of elements in long sequences into neat columns.
# W0311: Bad indentation. PyLint expects a four-space soft indent, I prefer two.

pylint --disable=C0301,C0303,C0326,W0311 ./*.py
