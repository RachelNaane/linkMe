#!/bin/bash

url=${1:-http://localhost:3000}
echo $url

response=$(curl -s -o /dev/null -w "%{http_code}" $url/health)
echo $response

if [ $response -eq 200 ]; then
  exit 0
else
  exit 1
fi