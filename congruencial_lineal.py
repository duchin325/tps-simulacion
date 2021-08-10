from decimal import Decimal, ROUND_HALF_UP

def linearMethod(n, x, k, c, g, intervalos):
    a = 1 + 4 * k
    m = pow(2, g)
    lista_valores = []
    tam_interval = 0.9999 / intervalos
    cota_superior = 0
    res = []
    for i in range(0,intervalos):
        cota_superior = tam_interval + cota_superior
        intervalo = Intervalo(i,cota_superior)
        res.append(intervalo)
    if res[-1].cota_superior < 0.9999:
            res[-1].cota_superior = 0.9999
    for i in range(0,n):
        x = ((a * x + c) % m)
        ran = Decimal(x) / Decimal(m - 1)

        output = Decimal(Decimal(ran).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))
        if output > 0.9999:
            output = 0.9999
        for item in range(0, len(res)):
            if output <= res[item].cota_superior:
                res[item].frecuencia += 1
                break
    return res


class Intervalo:
  frecuencia = 0
  def __init__(self, numero_intervalo, cota_superior):
    self.numero_intervalo = numero_intervalo
    self.cota_superior = cota_superior
