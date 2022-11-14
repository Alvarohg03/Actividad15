#3. Crea otro archivo python que pida una frase y
#responda cuántas veces está la letra que hayas elegido

frase = input("Dime una frase ")
letra = input("Dime la letra que quieres buscar ")
veces = 0
for i in frase:
    if i == letra:
        veces = veces+1

print(f'La letra {letra} aparece {veces} veces')
