#!/bin/bash
#hmm
curl -siLk -X OPTIONS "$1" | grep -oiE 'Allow: .+' | cut -d ' ' -f2-
