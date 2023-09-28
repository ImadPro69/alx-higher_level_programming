#!/bin/bash
#hmm
curl -s -w "%{response_code}" -o /dev/null "$1"
