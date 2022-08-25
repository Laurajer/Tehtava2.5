# 2.5
# 1 leiviskä on 20 naulaa
# 1 naula on 32 luotia
# 1 luoti on 13,3g

leiviska_string = input("Anna leiviskät:")
naula_string = input("Anna naulat:")
luoti_string = input("Anna luodit:")
leiviska = float(leiviska_string)
naula = float(naula_string)
luoti = float(luoti_string)
# Luoti = 13,3g
# Naula = 13,3g * 32 = 425,6g
# Leiviskä = 425,6g * 20 = 8512g
area = luoti * 13.3
area1 =

print(f"Massa nykymittojen mukaan on {area: .3f} ")