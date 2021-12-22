#!/bin/bash
# getdata.sh : Vipin Maurya
# Updates data.txt with station's latitude, longitude, and elevation from embeded links is html file of event
wget -F -i "BiharNepalEQ34.html" -O .temp
sed 's/<[^>]*>//g ; /^$/d' .temp > data.csv
cat data.csv | grep -oP '(?<=Code: ).*?(?=Name)' > .temp
sed 's/Latitude://g;s/Longitude://g;s/Elevation://g;s/Depth://g' .temp > data.csv
awk -F, 'BEGIN {printf "Code \t Latitude \t Longitude \t Elevation \t Depth\n"} {printf "%s \t %s \t %s \t %s \t %s \n", $1, $2, $3, $4, $5}' data.csv > .temp
awk '{lat=$2; long=$3; ele=$4; getline < "data.txt"; print $1","lat","long","ele","$2","$3","$4","$5","$6> "data.csv"}' .temp
