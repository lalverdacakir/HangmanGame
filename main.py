
print("""This is a two player hangman game """)

kelime=input("Please enter the word: ")
list_kelime=[]
for i in kelime:
    list_kelime.append(i.lower())

word_try=[0]*len(list_kelime)
wrong=int()

while(True):
    print("Wrong count: "+str(wrong))
    if(wrong>5):
        print("You failed looser")
        break
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
            wrong+=1
            continue




