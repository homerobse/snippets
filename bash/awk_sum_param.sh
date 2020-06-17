# match regular expression and sum or subtract according to which match it was
awk '$1 ~ /credit|gain/ { sum += $2 }
$1 ~ /debit|loss/  { sum -= $2 }
END { print sum }' awk_sum_param.data
