#! /bin/bash
avail="$(python macbook.py)"    
echo $avail
if [[ "$avail" =~ unavailable ]] ; then
    echo "Pickup is still not available"
else
    echo "Pickup is available now"
fi