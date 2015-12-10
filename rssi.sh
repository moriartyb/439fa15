while true
do
  iw dev wlp1s0 station dump | ./iwparser.py
done
