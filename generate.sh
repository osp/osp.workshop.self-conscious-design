#!/bin/bash
# Script to generate epubs for all source folders in epub_content

echo "Generating all epubs:"
for i in $( ls public/epub_content/ | grep -v epub_library.json ); do
    echo "Generating $i";
    bash zip.sh $i;
done;
echo "Done"
