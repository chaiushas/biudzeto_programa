class PajamuIrasas():
    def __init__(self, suma, siuntejas, papildoma_informacija):
        self.suma = suma
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija


class IslaiduIrasas():
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        self.suma = suma
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


class Biudzetas:
    def __init__(self):
        self.masyvas = []


    def prideti_pajamas(self, suma, siuntejas, papildoma_informacija):
        pridetos_pajamos = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.masyvas.append(pridetos_pajamos)


    def prideti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        pridetos_islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.masyvas.append(pridetos_islaidos)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.masyvas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas = balansas - irasas.suma
        return balansas

    def gauti_ataskaita(self):
        for irasas in self.masyvas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma}, Siuntejas: {irasas.siuntejas}, Papildoma info: {irasas.papildoma_informacija}")
            if isinstance(irasas, IslaiduIrasas):
                print (f"Islaidos: {irasas.suma}, Atsiskaitymo budas: {irasas.atsiskaitymo_budas}, Preke arba Paslauga: {irasas.isigyta_preke_paslauga}")

naujas_irasas = Biudzetas()
while True:
    veiksmas = int(input("1 - ivesti pajamas, 2 - ivesti islaidas, 3 - perziureti balansa, 4 - perziureti ataskaita, 5 - uzbaigti programa"))
    if veiksmas == 1:
        suma = float(input("Iveskite pajamas: "))
        siuntejas = str(input("Iveskite siunteja: "))
        papildoma_informacija = str(input("Iveskite papildoma info: "))
        pajamos1 = naujas_irasas.prideti_pajamas(suma, siuntejas, papildoma_informacija)
    if veiksmas == 2:
        suma = float(input("Iveskite islaidas: "))
        atsiskaitymo_budas = str(input("Iveskite atsiskaitymo buda: "))
        isigyta_preke_paslauga = str(input("Iveskite isigyta preke ar paslauga: "))
        islaidos1 = naujas_irasas.prideti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    if veiksmas == 3:
        print(f"{naujas_irasas.gauti_balansa()}")
    if veiksmas == 4:
        naujas_irasas.gauti_ataskaita()
    if veiksmas == 5:
        break