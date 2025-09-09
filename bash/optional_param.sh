# Run this as `./optional-param.sh param1 param2` to see running with two params and then run with only param1
if [ ! -z $2 ]  # not empty string https://stackoverflow.com/a/6482403/1273751 comment from gcb Feb 26 '14
then
   echo "print two params, print both: " $1 $2
else
   echo "with only one it falls in the else and prints just the first: " $1
fi
