#!C:\Users\wonsik\anaconda3\python.exe

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

opened_tile = open('data/'+title,'w')
opened_tile.write(description)
opened_tile.close()

#Redirection
print("Location: index.py?id="+title)
print()
