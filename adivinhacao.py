import random
def main():
    game()

def game():
    dificuldade = clamp(intput("Insira o nível de dificuldade (1 a 10): "),1,10)
    chances=10-dificuldade
    aleatorio=random.randint(1,100)
    tentativa = intput("Insira um número aleatório entre 1 e 100: ")
    qd_tentativas=1
    while tentativa != aleatorio and chances>0:
        if tentativa > aleatorio:
            tentativa = intput("Tente um número menor (entre 1 e 100): ")
            qd_tentativas+=1
            chances-=1
        elif tentativa < aleatorio:
            tentativa = intput("tente um número maior (entre 1 e 100): ")
            qd_tentativas+=1
            chances-=1
    if tentativa == aleatorio:
        print("Parabéns! Você acertou com",qd_tentativas,"tentativa(s) e fez",dificuldade*(11-qd_tentativas),"ponto(s)!")
    else:
        print("Game Over")
    replay()

def replay():
    replay_pergunta = input("Quer jogar de novo? (S/N): ")
    if replay_pergunta.lower() == "s":
        game()


def intput(texto):
    intput=input(texto)
    check=False
    while check==False:
        try:
            int(intput)
            check=True
            return int(intput)
        except ValueError:
            check=False
            intput=input(texto)

def clamp(valor, valor_minimo, valor_maximo):
    if valor > valor_maximo:
        valor = valor_maximo
    elif valor < valor_minimo:
        valor = valor_minimo
    return valor


if __name__=="__main__":
    main()