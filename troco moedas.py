# Descrição: Pagar um troco em moedas com a menor quantidade possível.
# Autor: Diego Vale do Nascimento - 25/09/2022

vt = float(input('Valor total: '))
vp = float(input('Valor pago: '))
print("=================================")
troco = vp - vt
print('O resto é: R$', troco)
print("=================================")
moedas=0
vca=1
diferenca=troco
while True:
    if vca <= diferenca:
        moedas += 1
        diferenca -= vca
    else:
        if moedas > 0:
            print("%d moeda(s) de R$ %5.2f" % (moedas, vca))
        if diferenca == 0:
            break
        if vca == 1:
            vca = 0.5
        elif vca == 0.5:
            vca = 0.25
        elif vca == 0.25:
            vca = 0.1
        elif vca == 0.1:
            vca = 0.05
        elif vca == 0.05:
            vca = 0.01
        moedas=0