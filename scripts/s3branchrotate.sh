#!/bin/bash
new_list=("$1")
for b in $(cat $2); do
  [[ $b != "$1" ]] && new_list+=("$b")
done;
printf "%s\n" "${new_list[@]}" > $2