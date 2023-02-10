#!/bin/bash

url=${1:-http://localhost:80}

echo ""
echo "TEST 1 - HEALTH ==============================================="
echo "starting test..."
response=$(curl -s -o /dev/null -w "%{http_code}" $url/health)

if [ $response -eq 200 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi

echo ""
echo "TEST 2 - GET ==============================================="
echo "starting test..."
response=$(curl -s -o /dev/null -w "%{http_code}" $url/register)

if [ $response -eq 200 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi

echo ""
echo "TEST 3 - POST ==============================================="
echo "starting test..."
response=$(curl -X POST -s -o /dev/null -w "%{http_code}" $url/register \
  -H "Content-Type: application/x-www-form-urlencoded"  \
  -d "email=test@gmail.com&name=test&password1=123456&password2=123456")

if [ $response -eq 302 ]; then
  echo "success"
else
  echo "test failed"
  exit 1
fi