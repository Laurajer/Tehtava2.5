#pituus = float(input("Kuinka pitkä olet?"))
#if 1.5 <= pituus <= 2.0:
    #print("Olet normaalimittainen")

#if pituus >= 1.5 and pituus <=2.0:
    #print("olet normaalipituinen.")

#if pituus <1.5 or pituus > 2.0:
    #print("Et ole normaalimittainen.")

#mjono1 = input("anna eläinlaji")
#mjono2 = input("anna eläinlaji")

#if mjono1 == mjono2:
    #print("annoit saman eläinlajin")

#muuttuja1 = 5
# int-tyyppinen, koska sinne sijoitettii kokonaisluku 5

#muuttuja2 = 1.49
# float/double-tyyppinen, koska sinne sijoitettiin desimaaliluku

#muuttuja3 = "Rakas"
# String-tyyppinen, koska sinne sijoitettiin merkkijono

#muuttuja4 = input("Kirjoita numero")
# String tyyppinen, jos halutaan vertailla

#ika = int(input("Anna ikäsi"))
#if ika >= 15 and ika <18:
   # paino = float(input("Anna painosi"))
#if ika >= 18 or (ika >= 15 and paino >= 55):
    #print("Lääkkeen käyttö sallittu.")

#if ika >= 15 and ika <18:
    #paino = float(input("Anna painosi"))
#if ika >= 18 or (ika >= 15 and paino >= 55):
    #print("Lääkkeen käyttö sallittu.")
#else:
    #print("Lääkkeen käyttö ei sallittu.")


# Ei kaadu koska ika testataan ennen kuin paino ja jos ikä ei yli 15 niin painoa ei ikinä päädytä vertaamaan.

#if ika >= 15 and ika <18:
    #paino = float(input("Anna painosi"))
#if ika >= 18:
    #print("Lääkkeen käyttö sallittu.")
#if ika >=25 and ika <18:
    #if paino >= 55:
        #print("Lääkkeen käyttö sallittu.")
# Ei yhtään kikkaa versio, uutena asiana kaksisisäkkäistä if-rakennetta"

ika= int(input("Anna ikäsi"))
if ika >= 18:
    print("Lääkkeen käyttö sallittu")
elif ika < 15:
    print("lääkkeen käyttö ei sallittua")
else:
    paino = float("Anna painosi")
    if paino >= 55:
        print("Lääkkeen käyttö sallittu")
    else:
        print("Lääkkeen käyttö ei sallittu")