#!/usr/bin/python

import matplotlib.pyplot as plt
import subprocess
from matplotlib import rc
import json
import sys


def error_message(message, e=False):
  print  "\033[91m" + "Error: "+ message + "\n \033[0m"
  if (e):
    exit(1)

def warning_message(message):
  print  "\033[93m" + "Warning: " + message + "\n \033[0m"

def ok_message(message):
  print  "\033[92m" + message + "\n \033[0m"


rc('font',**{'family':'serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

colors_data=["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]

def get_data(file):
  k = list()
  v = list()
  f = open(file, 'r')
  lines = f.readlines()

  lines = lines[1:-1]

  for i in lines:
    i = i[0:-1]
    i = i.split(',')
    k.append(i[0])
    v.append(float(i[1]))
  return [k,v]


def bench(name, url):
  command = '/usr/bin/ab -n %d -c %d -k -e %s.csv %s %s' % (requests, concurrency, name, ab_flags, url)
  ok_message("Executing : " + command)
  command = command.split()
  ret = subprocess.call(command)

if len(sys.argv) == 2:
  config_file = sys.argv[1]
else:
  config_file = "config.json"

try:
    f = open(config_file)
except:
    error_message("cannot open " + config_file, True)

try:
  d = json.load(f)
except Exception as e:
  error_message(config_file + " : JSON parse error", True)
  print e
  exit(1)

if "urls" in d.keys():
  servers = d["urls"];
else:
  error_message("Need urls to hit, see example configuration file.")
  exit(1)

if "requests" in d.keys():
  requests = int(d["requests"])
else:
  warning_message("No request count. Assuming 10000.")
  requests = 10000;

if "concurrency" in d.keys():
  concurrency = int(d["concurrency"])
else:
  warning_message("No concurrency value. Assuming 100.")
  concurrency = 100

if "args" in d.keys():
  ab_flags = d["args"];
  ok_message("Custom arguments : " + ab_flags)
else:
  ab_flags = ""

for i in servers.keys():
  bench(i, servers[i])

data = dict()
color_index=0
for i in servers.keys():
  data[i] = get_data(i+".csv")
  plt.plot(data[i][0],data[i][1], 'k-', color=colors_data[color_index], label=i)
  color_index=color_index +1

plt.legend(data.keys(), loc=2)

zero = [0 for i in range(len(data[i][0]))]

color_index=0
for i in servers.keys():
  plt.fill_between(data[i][0], zero, data[i][1], facecolor=colors_data[color_index], alpha=0.3)
  color_index=color_index+1

plt.title('Response time, repartition. \\ ~  \small %d request, concurrency level : %d ' % (requests, concurrency))
plt.xlabel('Percentage of time')
plt.ylabel('Time in $\mu{}s$')
name = ""
for i in servers.keys():
  name += i + "_vs_"
name = name[:-4] + ".pdf"
plt.savefig(name)
