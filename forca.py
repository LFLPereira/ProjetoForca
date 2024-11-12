import random
from getpass import getpass
def main():
    game()

def game():
    multiplayer=input("Multiplayer? (S/N): ")
    if multiplayer.lower() == "s":
        palavra_chave=getpass("Digite a Palavra Chave: ").lower()
    else:
        palavras=["abelha","baleia","cachorro","dromedario","elefante","foca","gato","hiena","iguana","jacare","kiwi","lagarto","macaco","ovelha","quati","rato","sardinha","tartaruga","urso","vaca","Zebra"]
        palavra_chave=random.choice(palavras)
    palavra_escondida=[]
    chances=7
    numero_letras=len(palavra_chave)
    while numero_letras > 0:
        palavra_escondida.append("_")
        numero_letras-=1
    print("".join(palavra_escondida))

    while chances > 0 and "".join(palavra_escondida)!=palavra_chave:
        tentativa = input("Escolha uma letra: ").lower()
        match chances:
            case 7:
                print(" /----")
                print("     |")
                print("     |")
                print("     |")
            case 6:
                print(" /----")
                print("     |")
                print("     |")
                print("|    |")
            case 5:
                print(" /----")
                print("     |")
                print("     |")
                print("| |  |")
            case 4:
                print(" /----")
                print("     |")
                print(" |   |")
                print("| |  |")
            case 3:
                print(" /----")
                print("     |")
                print("/|   |")
                print("| |  |")
            case 2:
                print(" /----")
                print("     |")
                print("/|\  |")
                print("| |  |")
        if len(tentativa)>1:
            chances-=1
        elif tentativa in palavra_chave:
            contador=0
            for letra in palavra_chave:
                if letra == tentativa:
                    palavra_escondida[contador] = tentativa
                    contador+=1
                else:
                    contador+=1
        else:
            chances-=1
        print("".join(palavra_escondida))
    if "".join(palavra_escondida) == palavra_chave:
        print("Parabéns!")
    else:
        print(" /----")
        print(" o   |")
        print("/|\  |")
        print("| |  |")
        print("Game Over")
    replay()

def replay():
    replay_pergunta = input("Quer jogar de novo? (S/N): ")
    if replay_pergunta.lower() == "s":
        game()

if __name__=="__main__":
    main()