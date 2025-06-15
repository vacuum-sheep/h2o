#!/bin/bash

T=1421

# kv cache budget
# a_list=(0.4 0.6 0.8 1.0)
a_list=(0.01 0.2)

for a in "${a_list[@]}"
do
    # 计算 y = a * T 
    y=$(awk "BEGIN {printf \"%d\", $a * $T}")

    echo "Running with x=$x, y=$y (a=$a)"
    bash scripts/summarization/eval.sh xsum 3 h2o 0 0 $y
done
