for i in {0..78}
do
   echo "File $i over 78"
   #if test $i -gt 9
   if (( $i >= 10 )); then
      curl https://placedata.reddit.com/data/canvas-history/2022_place_canvas_history-0000000000$i.csv.gzip -o ~/code/benchmarkingBlockchains/pixelWarData/data/$i.csv.gzip
   else
      curl https://placedata.reddit.com/data/canvas-history/2022_place_canvas_history-00000000000$i.csv.gzip -o ~/code/benchmarkingBlockchains/pixelWarData/data/$i.csv.gzip
   fi
done
