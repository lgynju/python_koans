#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass

def triangle(a, b, c):
    data = [a, b, c]

    for i in data:
        if i<=0:
            raise(TriangleError)
    if (a + b <= c or a + c <= b or b + c <= a):
        raise(TriangleError)
    data =set(data)
    if len(data) == 1:
        return 'equilateral'
    if len(data) == 2:
        return 'isosceles'
    return 'scalene'
    # DELETE 'PASS' AND WRITE THIS CODE
    #pass
