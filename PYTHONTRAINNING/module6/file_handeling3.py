def main():
    infile=open('prachi.txt','r')
    line=infile.readline()
    print(line)
    while line !="":
        #amount=float(line)
        line=infile.readline()
    #infile.close()
        print(line)
main()
