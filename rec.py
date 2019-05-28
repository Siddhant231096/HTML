#!/usr/bin/python3

import cgi

print("Content-type:text/html")
print("")

#extacting all code of html
web=cgi.FieldStorage()
#now extracting only form data
username=web.getvalue('x')
password=web.getvalue('y')

print("we got the username",username)
print("we got the password",password)






