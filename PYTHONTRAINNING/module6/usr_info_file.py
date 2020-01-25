def usr_info():
    data=open('usr_data.txt','a')
    Id=input("Enter your Id")
    name=input("Enter your name")
    age=input("Enter your age")
    data.write('Id :'+Id)
    data.write('\nname :'+name)
    data.write('\nage :'+age)
    print('\n')
    data.close()
usr_info()

    
    
