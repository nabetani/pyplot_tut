import csv
import math
import random
from matplotlib import pyplot

def line(cond, param, op):
  scond = ["hoge", "fuga"][cond]
  sparam = ["foo", "bar", "baz" ][param]
  sop = ["aap", "noot", "mies", "zus", "jet" ][op]
  ary=[scond,sparam,sop]
  for x in range(100):
    noise = random.normalvariate(1, 0.3)
    v = math.pow( 1.1+math.sin((cond+1.0) * (x*x) * 1e-3), param*2+1) * math.pow(10, param) * noise
    ary.append( v )
  return ary

def two_dim(ary):
  if 0==len(ary):
    return ary
  if type(ary[0])==type([]):
    return ary
  return [ary]

def stack(upper, lower):
  if 0==len(upper):
    return two_dim(lower)
  return two_dim(upper)+two_dim(lower)

def make_data(cond):
  data = []
  for op in range(5):
    for param in range(3):
      data = stack( data, line(cond, param, op) )
  return data

for name, cond in [ [ 'hoge.csv', 0 ], ['fuga.csv', 1] ]:
  with open(name, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(make_data(cond))
