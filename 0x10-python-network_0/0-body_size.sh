#!/bin/bash
# takes in a URL, sends a request
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
