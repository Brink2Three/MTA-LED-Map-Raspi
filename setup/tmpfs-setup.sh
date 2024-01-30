#!/bin/bash

mkdir /tmp/nyct-temp

mv /usr/local/lib/python3.9/dist-packages/nyct_gtfs/*  /tmp/nyct-temp/ 

mount -t tmpfs -o size=50m tmpfs /usr/local/lib/python3.9/dist-packages/nyct_gtfs
mv /tmp/nyct-temp/* /usr/local/lib/python3.9/dist-packages/nyct_gtfs/
