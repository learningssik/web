#!C:\Users\wonsik\anaconda3\python.exe
print('content-type: text/html; charset=UTF-8')
print()
import cgi, os, view

form = cgi.FieldStorage()
# pageId = form.getvalue("id")
if 'id' in form:
    pageId = form["id"].value

    description = open('data/'+pageId,'r').read()

    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action ='''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = "Hello"
    description = "Hello web"
    update_link =""
    delete_action=""

print('''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <title>WEB1 - welcome</title>
    <meta charset="utf-8">

  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>

    <ol>
        {listStrs}
    </ol>

    <a href="create.py">create</a>
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>

  </body>
</html>

'''.format(
title=pageId,
desc=description,
listStrs=view.getList(),
update_link=update_link,
delete_action=delete_action))
