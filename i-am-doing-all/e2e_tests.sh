#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

# Install necessary tools
apt-get update
apt-get install -y curl jq

BASE_URL="http://nginx:80"

# Function to make HTTP requests
function http_request {
    local method=$1
    local endpoint=$2
    local data=$3
    # echo "Request: $method $endpoint $data"
    if [ -z "$data" ]; then
        curl -s -X "$method" "${BASE_URL}${endpoint}" -H "Content-Type: application/json"
    else
        curl -s -X "$method" "${BASE_URL}${endpoint}" -H "Content-Type: application/json" -d "$data"
    fi
}

# Test CREATE mission
echo "Testing CREATE mission"
response=$(http_request POST "/mission" '{"title": "Test Mission", "description": "This is a test mission"}')
echo "Response: $response"
mission_id=$(echo "$response" | jq -r '.id')
if [ -z "$mission_id" ] || [ "$mission_id" == "null" ]; then
    echo "Failed to create mission"
    exit 1
fi
echo "Mission created with ID: $mission_id"

# Test GET all missions
echo "Testing GET all missions"
response=$(http_request GET "/mission")
echo "Response: $response"
mission_count=$(echo "$response" | jq '. | length')
if [ "$mission_count" -le 0 ]; then
    echo "Unexpected number of missions"
    exit 1
fi
echo "Successfully retrieved all missions"

# Test GET mission
echo "Testing GET mission"
response=$(http_request GET "/mission/$mission_id")
echo "Response: $response"
if [ -z "$response" ] || [ "$response" == "null" ]; then
    echo "Failed to get mission: response is null or empty"
    exit 1
fi
echo "Successfully retrieved mission"

# Test UPDATE mission
echo "Testing UPDATE mission"
http_request PUT "/mission/$mission_id" '{"title": "Updated Mission", "description": "This mission has been updated"}'
response=$(http_request GET "/mission/$mission_id")
echo "Response: $response"
updated_title=$(echo "$response" | jq -r '.title')
if [ "$updated_title" != "Updated Mission" ]; then
    echo "Failed to update mission"
    exit 1
fi
echo "Successfully updated mission"

# Test DELETE mission
echo "Testing DELETE mission"
http_request DELETE "/mission/$mission_id"
response=$(http_request GET "/mission/$mission_id")
echo "Response: $response"
if [ "$(echo "$response" | jq -r '.error')" != "Mission not found" ]; then
    echo "Failed to delete mission"
    exit 1
fi
echo "Successfully deleted mission"

# Test GET all missions
echo "Testing GET all missions"
response=$(http_request GET "/mission")
echo "Response: $response"
mission_count=$(echo "$response" | jq '. | length')
if [ "$mission_count" -ne 0 ]; then
    echo "Unexpected number of missions"
    exit 1
fi
echo "Successfully retrieved all missions"

echo "All tests passed successfully!"