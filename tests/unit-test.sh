#!/bin/bash

url=${1:-http://localhost:3000}

echo "UNIT TEST==============="
echo "app at $url"
echo "starting test..."

response=$(curl -s -o /dev/null -w "%{http_code}" $url/health)
echo "got response $response"

if [ $response -eq 200 ]; then
  echo "succes, app healthy"
  exit 0
else
  echo "test failed" 
  exit 1
fi