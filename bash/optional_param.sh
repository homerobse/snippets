# Run this as `./optional-param.sh param1 param2` to see running with two params and then 
if [ ! -z $2 ]  # not empty string https://stackoverflow.com/a/6482403/1273751 comment from gcb Feb 26 '14
then
   echo "print two params " $1 $2
else
   echo "also works with only one " $1
fi
