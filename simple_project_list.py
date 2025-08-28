#List
#Search  ,  add  , delete

import os
os.system('cls')

lst=['HAMED:09119971553','ALI:0911999999','KAKA:9908888888','Alex:+0115584466']
ans=True
while(ans):
    
    
    
    def search():
        name=input('Type your name to search: ')
        for i in lst:
            if name == i.split(':')[0] :
                print(i)
                break
        else:
            print('We can not find ')
    search()

    print('')
    
    def add():
        name =input('Type Your Name to add: ')
        number=input('Type Your Number to add: ')
        ful=name+':'+number
        lst.append(ful)
        
    add()
    
    print('')
    name=[]
    for i in lst:
        name = i.split(':')[0]
        print(name)
    print('')
    
    
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
    
    
    print('')    
    
    print('would you like to continue? yes or no  ')
    answer=input()
    
    answer_lst=['n','No','no','N']
    for i in answer_lst:
        if i == answer:
            ans=False
    print('good bye!')