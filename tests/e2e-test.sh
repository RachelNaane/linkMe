#!/bin/bash

url=${1:-http://localhost:80}

echo ""
echo "TEST 1 - HEALTH ==============================================="
echo "starting test..."
response=$(curl -s -o /dev/null -w "%{http_code}" $url/health)
echo "got status code response ${response}"

if [ $response -eq 200 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi

echo ""
echo "TEST 2 - ADD LINK ==============================================="
echo "starting test..."
response=$(curl -X POST -s -o /dev/null -w "%{http_code}" $url \
  -H "Content-Type: application/x-www-form-urlencoded"  \
  -d "url=test&tag=test&description=test")
echo "got status code response ${response}"

if [ $response -eq 200 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi

echo ""
echo "TEST 3 - GET LINK ==============================================="
echo "starting test..."
response=$(curl $url/get-links)
echo "got response ${response}"
count=$(grep -o "test" <<< "$response" | wc -l)
echo "found 'test' ${count} times"

if [ $count -eq 3 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi

echo ""
echo "TEST 4 - DELETE LINK ==============================================="
echo "starting test..."
id=$(echo $response | jq -r '.[0]._id."$oid"')
echo "link id is ${id}"
response=$(curl -s -o /dev/null -w "%{http_code}" $url/delete-link/${id})
echo "got status code response ${response}"

if [ $response -eq 302 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi