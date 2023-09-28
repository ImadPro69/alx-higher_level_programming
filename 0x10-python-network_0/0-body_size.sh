#!/bin/bash

curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
