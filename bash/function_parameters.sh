#!/bin/bash

var_list="1 2 30 4 5"

function f(){
  for x in $var_list; do 
    echo $1
    echo hey! $x
  done
}
f '23'
