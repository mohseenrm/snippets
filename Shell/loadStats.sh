#!/bin/sh

rm ./temp.stats
find . -name 'dbtable*.csv' -type f | xargs cat | cut -d ',' -f3 | sort | uniq | grep -E 'Forum|MarketPlace|Marketplace' >> temp.stats
cat temp.stats
