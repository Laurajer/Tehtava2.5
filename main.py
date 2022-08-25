# 2.5
# 1 leiviskä on 20 naulaa
# 1 naula on 32 luotia
# 1 luoti on 13,3g

leiviska_string = input("Anna leiviskät: ")
naula_string = input("Anna naulat: ")
luoti_string = input("Anna luodit: ")
leiviska = float(leiviska_string) * 8512
naula = float(naula_string) * 425.6
luoti = float(luoti_string) * 13.3
# Luoti = 13,3g
# Naula = 13,3g * 32 = 425,6g
# Leiviskä = 425,6g * 20 = 8512g
massa = luoti + naula + leiviska
yhteispaino = massa / 1000
yhteispaino_int = int(yhteispaino)
ylijaama = int((yhteispaino - int(yhteispaino)) * 1000)

print("Massa nykymittojen mukaan on " + str(yhteispaino_int) + " kilogrammaa ja " + str(ylijaama) + " grammaa.")
