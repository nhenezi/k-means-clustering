#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import math
import sys
from argparse import ArgumentParser

DEBUG = True

def distance(a, b):
  '''Defines distance between two tuples'''
  return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def printData(data, colors = False, centeroids=False):
  removeEmpty = lambda a: filter(lambda x: x, a)
  # finds highest x and y values in data
  xmax = max(map(lambda x: max(map(lambda y: y[0], x) or 0), removeEmpty(data))) + 1
  ymax = max(map(lambda x: max(map(lambda y: y[1], x) or 0), removeEmpty(data))) + 1
  '''Displays data in user friendly way'''
  out = [[" " for _ in xrange(ymax)] for _ in xrange(xmax)]
  for i, color in enumerate(data):
    # if colors == False paint everything white
    startColor = (colors and 31) or 37
    for d in color:
      out[d[0]][d[1]] = '\033[1;' + str((startColor + i)) + 'm·\033[1;m'
  if centeroids:
    for i, c in enumerate(centeroids):
      out[int(round(c[0]))][int(round(c[1]))] = '\033[1;' + str(31 + i) + 'm×\033[1;m'

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
  print data
  xmax = max(map(lambda x: x[0], data))
  ymax = max(map(lambda x: x[1], data))
  centeroids = [(random.randint(0, xmax - 1),
                 random.randint(0, ymax - 1)) for _ in xrange(k)]
  
  print "Inital structure:"
  printData([data], centeroids=centeroids)
  change = True
  cnt = 0
  while change and cnt < maxIter:
    clusters = [[] for i in xrange(k)]
    for i in xrange(len(data)):
      minDist = False
      color = False
      for j in xrange((len(centeroids))):
        '''find closest centeroid for each data'''
        dist = distance(data[i], centeroids[j])
        if minDist == False or dist < minDist:
          minDist = dist
          color = j

      clusters[color].append(data[i])
    newPos = map(avg, clusters)
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
      printData(clusters, colors=True, centeroids=centeroids)
    centeroids = newPos
    cnt = cnt + 1
  return clusters

def parse():
  parser = ArgumentParser(description='K-means clustering algotihm visualization')
  parser.add_argument('--in-file', help='Input file', dest='infile', metavar='f')
  parser.add_argument('-pm', '--marker', default='1', metavar='p',
                      help='How are data points marked in matrix. Default 1.')
  parser.add_argument('-cs', '--separator', default=' ', metavar='$',
                      help='How are columns separated. Default is one space " ".')
  parser.add_argument('-k', '--means', dest='k', type=int, metavar='k',
                      help='Number of clusters', action='store')
  parser.add_argument('--max-iter', dest='maxIter', metavar='n', default='30',
                      type=int,
                      help='Maximum number of iterations. Default 30')
  parser.add_argument('-v', '--verbose', help="Displays midsteps")


  options = parser.parse_args()
  if options.k == None:
    print "Invalid usage, try -h for help"
    sys.exit()
  if options.infile:
    f = open(options.infile, 'r')
    data = [line.split(options.separator) for line in f ]
    options.data = []
    for i, row in enumerate(data):
      for j, elem in enumerate(row):
        if str(elem) == str(options.marker):
          options.data.append((i,j))
    options.xmax = i + 1
    options.ymax = j + 1

  return options

def run(options):
  clusters = cluster(options.k, options.data, maxIter=options.maxIter)
  printData(clusters, colors=True)

if __name__ == '__main__':
  run(parse())
