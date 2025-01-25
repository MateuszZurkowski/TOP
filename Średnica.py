#Czy lepiej kupić diwe małe pizze czy jedną dużą

name = "Witaj głodomorku"
print('Witaj głodomorku, sprawdźmy która pizza jest dla Ciebie przeznaczona')
pizzaduża_średnica = float(input("Podaj średnicę dużej pizzy: "))
pizzaduża_cena = float(input("Podaj cenę dużej pizzy: "))
pizzamała1_średnica = float(input("Podaj średnicę małej pizzy nr.1: "))
pizzamała1_cena = float(input("Podaj cenę pizzy małej pierwszej: "))
pizzamała2_średnica = float(input("Podaj średnicę małej pizzy nr.2: "))
pizzamała2_cena = float(input("Podaj cenę małej pizzy nr.2: "))

# Opłacalność: średnica/cena

'Opłacalność_pizzy_dużej = (pizzaduża_średnica/2) / pizzaduża_cena'
'Opłacalność_pizzy_małej_1 + Opłacalność_pizzy_małej_2 == (pizzamała1_średnica/2 + pizzamała2_średnica/2) / pizzamała1_cena + pizzamała2_cena'


if 'opłacalność_pizzy_dużej' > 'opłacalność_pizzy_małej_1 + opłacalność_pizzy_małej_2' :
    print ("Pizza duża jest bardziej opłacalna")

elif 'opłacalność_pizzy_dużej'  == 'opłacalność_pizzy_małej_1 + opłacalność_pizzy_małej_2' :
    print ("Pizze są jednakowo opłacalne")

else:
    print ("Dwie małe pizze są bardziej opłacalne")