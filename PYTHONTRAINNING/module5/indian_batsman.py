Info={1:{'player_type':'Batsman','player_name':'virat_kohli','matches':'200','runs':'15000','average':'12','Highest_score':'200'}
      ,2:{'player_type':'Batsman','player_name':'Rohit_Sharma','matches':'250','runs':'20000','average':'20','Highest_score':'250'}
      ,3:{'player_type':'Bowler','player_name':'Jasmeet_bumrah','matches':'100','runs':'200','average':'10','Highest_score':'80'}
      ,4:{'player_type':'Allrounder','player_name':'ravindra_jadeja','matches':'100','runs':'1500','average':'8','Highest_score':'100'}
      ,5:{'player_type':'Bowler','player_name':'Mohammad_shami','matches':'300','runs':'500','average':'15','Highest_score':'70'}}
print(Info)
print("\n")
for p_id,p_info in Info.items():
    print("\n player",p_id)
    for key in p_info:
        if key==['Highest_score']:
            print(key)
        print(key+':',p_info[key])
Info={'Batsman':{'virat_kohli':{'matches':'200','runs':'15000','average':'12','Highest_score':'200'},
      'Rohit_Sharma':{'matches':'250','runs':'20000','average':'20','Highest_score':'250'}},
      'Bowler':{'Jasmeet_bumrah':{'matches':'100','runs':'200','average':'10','Highest_score':'80'}},
      'Allrounder':{'ravindra_jadeja':{'matches':'100','runs':'1500','average':'8','Highest_score':'100'}}}

for p_id,p_info in Info.items():
    print("\n player",p_id)
    for key,p_id in p_info.items():
        print(key,p_id)
        for k in p_id.items():
            print(k)
print(Info['Batsman']['virat_kohli']['runs'])
c=[]
for p_id in Info.keys():
    for key in Info[p_id].keys():
        c.append(Info[p_id][key]['Highest_score'])
print("Highest score",max(c))
            
        


        
