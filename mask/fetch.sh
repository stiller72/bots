#!/bin/bash

curl  -s -k -X $'POST' \
    -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json; charset=utf-8' -H $'Host: zeapi.yandex.net' -H $'Connection: close' -H $'User-Agent: Paw/3.2.2 (Macintosh; OS X/11.4.0) GCDHTTPRequest' \
    --data-binary $"{\"query\": \"$1\", \"intro\": $2, \"filter\": 1}" \
    $'https://zeapi.yandex.net/lab/api/yalm/text3' | jq -r '.text'
