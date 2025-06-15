#!/bin/bash

T=1421
scale=0.5

# kv cache budget
a_list=(0.4 0.6 0.8 1.0)

for a in "${a_list[@]}"
do
    # 计算 x = a * T * 0.5
    x=$(awk "BEGIN {printf \"%d\", $a * $T * $scale}")
    y=$x

    echo "Running with x=$x, y=$y (a=$a)"
    bash scripts/summarization/eval.sh xsum 3 h2o 0 $x $y
done
