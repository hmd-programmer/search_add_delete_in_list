#List
#Search  ,  add  , delete

import os
os.system('cls')

lst=['hamed:09119971553','ali:0911999999','kaka:9908888888','Alex:+0115584466']


def search():
        name=input('Type your name to search: ')
        for i in lst:
            if name == i.split(':')[0] :
                print(i)
                break
        else:
            print('We can not find ')
search()


def add():
    name =input('Type Your Name to add: ')
    number=input('Type Your Number to add: ')
    ful=name+':'+number
    lst.append(ful)
    print(lst)
add()


def delete():
        name=input('Type your name to delete: ')
        for i in lst:
            if name == i.split(':')[0] :
                lst.remove(i)
                print(lst)
                break
        else:
            print('We can not find ')
delete()