# Kiril Krushkov
# 2.22.2017
# Skilaverkefni 3
#----------------------------------------------------------------------------------------------------------------------#
from random import *
#----------------------------------------------------------------------------------------------------------------------#
JA = 0
while JA == 0:
    print("Dans félagar")
    print("Nöfn og Símanúmer")
    print("Nöfn, aldur og símanúmer")
    print("Hætta")
    vs=int(input("Sláðu inn númer liðs frá 1-4: "))
    if vs == 1:
        Karlmenn = ("Karl","Geir","Magnús","Sigurjón","Guðjón","Ágúst")
        Kvenmenn = ("Guðrún","Ása","Sigrún","Anna","Finna","Jónína")
        print("")
        for x in Karlmenn:
            print(x,end=" ")
        print("")
        for x in Kvenmenn:
            print(x,end =" ")
        print("\n")

        listi = []
        herrar = []
        konur = []
        listi2 = []
        #First male with the first female, another male with another female.
        teljari = 0
        for x in range(6):
            print(Karlmenn[teljari], " og ", Kvenmenn[teljari])
            teljari = teljari + 1
        print("")
        while len(listi)<6:#<<< #This loop matches one male and one female and adds to the list.
            herr = Karlmenn[randint(0,5)]
            kon = Kvenmenn[randint(0,5)]
            if herr not in herrar and kon not in konur:
                herrar.append(herr)
                konur.append(kon)
                par = herr+" og " + kon
                listi.append(par)
        skoda = sample(range(6),6)
        skoda2 = sample(range(6),6)

        for x in range(6):    #The loop prints out double.
            print(herrar[skoda[x]]," og ",konur[skoda2[x]])

        stafur = input("Sláðu inn staf ").lower()

        teljari = 0
        for w in herrar:
            if stafur in w or stafur.upper() in w:
                print("Það er",stafur,"er í nafninu",w)
                teljari = teljari + 1

        for w in konur:
            if stafur in w or stafur.upper() in w:
                print("Það er",stafur,"er í nafninu",w)
                teljari = teljari + 1

        if teljari == 0:
            print("Þessi stafur er ekki í neinum af þessum nöfnum")
        stafur ="n"

        for w in herrar:
            if w.count(stafur)>=2:
                print(w)
# ----------------------------------------------------------------------------------------------------------------------#
    elif vs == 2:
        #List of names and phone numbers.
        nofn = {"Kiril": 7831122, "Kalli": 6851555, "Ómar": 6184047, "Jens": 6664455, "Haldor": 7770055,
                "Stefán": 6916571, "Eyjólfur": 1231234, "Binni": 7654321, "Gunnar": 5556621, "Sigurjón:": 7770011}
        nafn = input("Sláðu inn nafn til að fá upplýsingar um hann: ")
        #Find what names are with (X) and phone number with (W).
        #Whenever a name from the list is printed numbers.
        for x,w in nofn.items():
            if x == nafn:
                print(w)
        #If the chosen name is not in the list is printed the ind. sent..
        if nafn not in nofn:
            print("Nafnið sem þú valdir er ekki í listanum. Sorry :(")
# ----------------------------------------------------------------------------------------------------------------------#
    elif vs == 3:
        teljari = 0
        bekkur = {"Jenni": 17, "Eyfi": 15, "Ísar": 22, "Kolli": 16, "Krissi": 16, "Stebbi": 13, "Andri": 12, "Skúli": 16, "Kuba": 1, "Einar": 16, "Bergur": 17, "Eiríkur": 46,
                  "Brynjar": 21, "Maggi": 18, "Sigurjón": 27}
        print(" ")
        for x in bekkur:
        #Prints entire list.
            print(x, "=> ", bekkur[x])
        print(" ")
        #Find those who are 18 or older and prints how many they are.
        for x in bekkur:
            if bekkur[x] >= 18:
                print(x)
                teljari = teljari + 1
        if teljari == 1:
            print("það er", teljari, "persóna 18 eða eldri")
        else:
            print("það eru", teljari, "persónur 18 eða eldri")
        teljari2 = 0
        print(" ")
        sum = 0
        #Calculates and prints the average and total figures.
        for key, value in bekkur.items():
            sum = sum + value
        medaltal = sum / len(bekkur)
        print("Medaltalið er",round(medaltal,2))
        print("Heildaraldurinn er:",sum)
        #Search for name.
        staf = input("Sláðu inn staf: ").upper()
        teljari = 0
        sum = 0
        #Found the average age of all names beginning with the selected letter and print it out.
        for key,value in bekkur.items():
            if key[0] == staf:
                sum = sum + value
                teljari = teljari + 1
                print(key,value)
        medaltal = sum / teljari
        print("Meðalaldur þeirra sem byrja á",staf,"eru",round(medaltal,2))
# ----------------------------------------------------------------------------------------------------------------------#
    elif vs == 4:
        print("Bless!")
        break
    else:
        break
#----------------------------------------------------------------------------------------------------------------------#
print("og Takk fyrir!:)")
#----------------------------------------------------------------------------------------------------------------------#