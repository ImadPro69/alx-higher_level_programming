#!/bin/bash

# Get the URL from the user input
URL=$1

# Send a request to the URL using curl
RESPONSE=$(curl -sL "$URL")

# Get the size of the response body in bytes
BODY_SIZE=$(wc -c <<< "$RESPONSE")

# Display the size of the response body
echo "$BODY_SIZE"
