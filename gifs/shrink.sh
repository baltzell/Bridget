#!/bin/sh
for rank in 2 3 4 5 6 7 8 9 t j q k a
do
    for suit in c d h s
    do
        oldgif="$rank$suit.gif"
        newgif="small_$rank$suit.gif"
        convert -scale 50 $oldgif $newgif
    done
done
