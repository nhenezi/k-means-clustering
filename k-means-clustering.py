#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import math
import sys
from argparse import ArgumentParser

xmax = 9
ymax = 9
DEBUG = True

def distance(a, b):
  '''Defines distance between two tuples'''
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def printData(data, colors = False, centeroids=False):
  '''Displays data in user friendly way'''
  out = [[" " for _ in xrange(ymax)] for _ in xrange(xmax)]
  if colors:
    for i, color in enumerate(data):
      for d in color:
        out[d[0]][d[1]] = '\033[1;' + str((31 + i)) + 'm·\033[1;m'
    if centeroids:
      for i, c in enumerate(centeroids):
        out[int(c[0])][int(c[1])] = '\033[1;' + str(31 + i) + 'm×\033[1;m'
  else:
    for d in data:
      out[d[0]][d[1]] = '·'
    if centeroids:
      for i, c in enumerate(centeroids):
        out[int(c[0])][int(c[1])] = '\033[1;' + str(31 + i) + 'm×\033[1;m'

  print ''
  print ''
  for row in out:
    for elem in row:
      print elem,
    print ''
  print ''
  print ''

def avg(tuples):
  '''Defines average position of list of tuples
  Returns False if list is empty'''
  if not tuples:
    return False
  a = b = 0.0

  for t in tuples:
    a = a + t[0]
    b = b + t[1]
  a = a / len(tuples)
  b = b / len(tuples)
  return (a, b)


def cluster(k, data, maxIter=30):
  
  centeroids = [(random.randint(0, xmax - 1),
                 random.randint(0, ymax - 1)) for _ in xrange(k)]
  
  print "Inital structure:"
  printData(data, colors=False, centeroids=centeroids)


  change = True
  cnt = 0
  while change and cnt < maxIter:
    colors = [[] for i in xrange(k)]
    for i in xrange(len(data)):
      minDist = False
      color = False
      for j in xrange((len(centeroids))):
        '''find closest centeroid for each data'''
        dist = distance(data[i], centeroids[j])
        if minDist == False or dist < minDist:
          minDist = dist
          color = j

      colors[color].append(data[i])
    newPos = map(avg, colors)
    for i in xrange(len(centeroids)):
      if newPos[i] == False:
        newPos[i] = centeroids[i]
    for i in xrange(len(centeroids)):
      changed = False
      if centeroids[i] != newPos[i]:
        changed = True
    if not changed:
      change = False
    if DEBUG:
      printData(colors, colors=True, centeroids=centeroids)
    centeroids = newPos
    cnt = cnt + 1
  return colors

def parse():
  parser = ArgumentParser(description='K-means clustering algotihm visualization')
  parser.add_argument('-k', '--means', help='Number of clusters', action='store', dest='k', type=int)
  parser.add_argument('--max-iter', help='Maximum number of iterations. Default 30', dest='maxIter')

  options = parser.parse_args()
  if options.k == None :
    print "Invalid usage, try -h for help"
    sys.exit()

  return options

def run(options):
  data = [(2,2), (1,2), (3,2), (4,1), (1,4), (6,6), (5,5), (4,4), (8,6), (6,8), (8,7)]
  colors = cluster(options.k, data)
  printData(colors, True)

if __name__ == '__main__':
  run(parse())
