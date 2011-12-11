#!/bin/sh

node router-nocache.js &
pid1=$!
node router.js &
pid2=$!
python ../abop.py conf.json

kill $pid1 $pid2
