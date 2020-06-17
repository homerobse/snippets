# the examples below should help to give an idea of how I have found awk being used.
# In awk man page, check the beginning of AWK PROGRAM EXECUTION
# and in PATTERNS AND ACTIONS sections Pattern and Actions
 
# awk to split with separator through option -F
echo "firstsepsecond" | awk -F 'sep' '{ print $1}'
echo "firstsepsecond" | awk -F 'sep' '{ print $2}'

# using with regular expression
echo 'word1 word2 word3,word4'| awk '/word1/{ print $1}'
echo 'word1 word2 word3,word4'| awk '/word1/{ print $2}'
echo 'word1 word2 word3,word4'| awk '/word1/{ print $3}'
echo 'word1word2 word3,word4'| awk '/word1/ {print $1}'
echo 'word1word2 word3,word4'| awk '/word1/ {print $2}'
