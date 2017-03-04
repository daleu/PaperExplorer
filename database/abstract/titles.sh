#! /bin/bash

for year in {1992..2003}; do
    
    echo "Processing $year files"
    
    for file in ./$year/*.abs; do
        echo -n "$(basename $file .abs) "
        cat $file | sed -n -e '/Title/,/Author/ p' | sed \$d | cut -d':' -f2 | paste -sd"\0" -
    done

done

