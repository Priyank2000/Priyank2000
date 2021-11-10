#!/bin/bash
file_name=$(echo $* | cut --complement -d "/" -f 1 | cut --complement -d "/" -f 1)
echo $file_name
ffmpeg -i $* -vf scale=480:320 output/$file_name