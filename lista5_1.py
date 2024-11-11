def main():
    conversao()

def conversao():
    hora24=input("Hora em formato 24:00: ")
    hora=hora24.split(":")
    aoup=""
    
    if int(hora[0])>12:
        hora[0]=int(hora[0])-12
        hora[1]=int(hora[1])
        aoup="PM"
        print(str(hora[0])+":"+str(hora[1]),aoup)
    else:
        hora[0]=int(hora[0])
        hora[1]=int(hora[1])
        aoup="AM"
        print(str(hora[0])+":"+str(hora[1]),aoup)
    conversao()

if __name__=="__main__":
    main()