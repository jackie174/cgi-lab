#!/usr/bin/env python3
import os
import json
from templates import login_page
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>CGI LAB</h2>")


#Q2: What environment variable contains the query parameter data?
#print("Content-Type: application/json")
#print()
#print(json.dumps(dict(os.environ), indent=2))
print("question 2: \n")
print(f"<p>QUERY_STRING = {os.environ.get('QUERY_STRING')}</p>")

#Q3: What environment variable contains information about the user’s browser?
print("question 3: \n")
print(f"<p>USER's BROWSER' = {os.environ.get('HTTP_USER_AGENT')}</p>")


#Q1: How do you inspect all environment variables in Python?
print("question 1: \n")
print(f"<p>all environment variables ' = {os.environ}</p>")