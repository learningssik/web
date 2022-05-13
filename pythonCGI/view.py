import os
def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr += '<li><a href="index.py?id={items}">{items}</a></li>'.format(items=item)
    return listStr
