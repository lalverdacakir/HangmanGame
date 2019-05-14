from random import randint
def adambastirma(wrong_count):
    if(wrong_count==0):
        print("""     _______
    |/      |
    |      
    |      
    |       
    |      
    |
jgs_|___""")
    elif(wrong_count==1):
        print("""     _______
    |/      |
    |      (_)
    |      
    |       
    |      
    |
jgs_|___""")
    elif(wrong_count==2):
        print("""     _______
    |/      |
    |      (_)
    |       |
    |       |
    |       
    |
jgs_|___""")
    elif(wrong_count==3):
        print("""     _______
    |/      |
    |      (_)
    |       |/
    |       |
    |        
    |
jgs_|___""")
    elif(wrong_count==4):
        print("""     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
jgs_|___""")
    elif(wrong_count==5):
        print("""     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
jgs_|___""")
    elif(wrong_count==6):
        print("""     _______
    |/      |
    |      (X)
    |      \|/
    |       |
    |      / \\
    |
jgs_|___""")


print("""This is a two player hangman game """)

kelime=input("Please enter the word: ")
ipucu=input("Please enter hint")


list_kelime=[]
for i in kelime:
    list_kelime.append(i.lower())

word_try=[0]*len(list_kelime)
wrong=int()

while(True):
    adambastirma(wrong)
    if (wrong >= 6):
        print("You failed looser")
        break
    print("\t\tHint: "+str(ipucu))
    print("\t\tWrong count: "+str(wrong))

    for k in word_try:
        if(k==0):
            print("__",end=" ")
        else:
            print(k,end=" ")
    print()


    c=int(input("Try word(0) or letter(1): "))

    if(c==1):
        harf=input("Enter the letter: ")
        harf=harf.lower()
        a=0
        for i in range(len(list_kelime)):
            if(harf==list_kelime[i]):
                word_try[i]=harf
                a=1

        if(a==0):

            wrong+=1

    else:
        tring_word=input()
        if(tring_word.lower()==kelime.lower()):
            print("Harikasın")
            break

        else:
            print("No No No")
            uzunluk=len(list_kelime)
            index=randint(0,uzunluk-1)
            word_try[index]=list_kelime[index]
            wrong+=1
            continue




