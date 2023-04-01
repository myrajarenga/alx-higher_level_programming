#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sS -H "X-School-User-Id: 98" "$1" | awk '/^\s*$/{flag=1;next} {if(flag)print}'
