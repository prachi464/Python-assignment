fr={'fruits':{'fruit1':{'name':'apple','binomial name':'malus domestica'
             ,'major producer':['china','united states','turkey']
             ,'nutrition':{'carbohydrates':'13.81g','fat':'0.17g','protein':26}}
    ,'fruit2':{'name':'mango','binomial name':'malus domestica'
             ,'major producer':['china','united states','turkey']
             ,'nutrition':{'carbohydrates':'13.81g','fat':'0.19g','protein':52}}}}
print(fr)

#print(fr['fruits']['fruit1']['nutrition']['protein'])

#print(fr['fruits']['fruit2']['nutrition']['protein'])

c=[]
for p_id,p_info in fr.items():
    for key,p_id in p_info.items():
        #print(key,p_id)
        for key2,p_id in p_id.items():
            if key2=='nutrition':
                #print(p_id)
                for key3,p_id in p_id.items():
                    if key3=='protein':
                        print(p_id)
                    
                        c.append(p_id)
print("Highest protein",max(c))
            
