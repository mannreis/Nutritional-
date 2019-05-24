#!/usr/bin/env bash
curl -s 'https://www.sas.ulisboa.pt/index.php' -c cookies > /dev/null

curl -s 'https://www.sas.ulisboa.pt/index.php' \
	-b cookies \
	--data 'opt=4%3B4H1&chvP=116%3B'$(date +"%Y-%m-%d")'%3B1&dia=&other=&searchbox=' \
	--compressed > request.html

grep -Pzo 'Menu Vegetariano</h2>(.*)*\n(.*)<div(.*)*\n(.*)*\n(.*)<h3(.*)*\n' request.html | \
	sed -e 's/<[^>]*>//g' | \
	tr -d '\n' ; echo | \
	#sed -e 's/\x09*//g' | \
	#sed -e 's/^M//g' | \
	#cat -v | \
	grep -bv '(.*)*' | \
	#cat -v | \
	#awk -F '^M' '{$1=$2=$3=$4=$5="x";print $0}'
echo 
sed '1,/Menu Vegetariano/d' request.html | \
	grep -Pzo '"data":(.*)*\n' | \
	cat -v | \
	grep -o '\[[^>]*]' | \
	jq -r '.[] as $k | "\($k.label), \($k.value)"' | \
	awk -F ', ' '{print $1, $2}'

grep -o '[0-9]*\.[0-9]* kCal' request.html | awk '{print $1, "kCal"} '
rm request.html 
rm cookies
