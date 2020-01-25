import pickle
phonebook={'chris':'555-222','kaite':'7777-86868','jone':'837579'}
out_file=open('phonebook.dat','wb')
pickle.dump(phonebook,out_file)
out_file.close()
