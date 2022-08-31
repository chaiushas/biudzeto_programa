import pickle

biudzeto_masyvas = []
while True:
    veiksmas = int(input(
        "1 - ivesti pajamas arba islaidas, 2 - paziureti pajamas ir islaidas, 3 - balansas, 0 - uzdaryti programa"))
    if veiksmas == 1:  # ivesti pajamas arba islaidas
        with open("biudzetas.pkl", "wb") as pickle_in:
            paj_isl = float(input("Iveskite suma: "))
            biudzeto_masyvas.append(paj_isl)
            pickle.dump(biudzeto_masyvas, pickle_in)
        with open("biudzetas.pkl", "rb") as pickle_out:
            pickle.load(pickle_out)
    if veiksmas == 2:  # perziureti pajamas ir islaidas
        try:
            with open("biudzetas.pkl", "rb") as pickle_out:
                print(pickle.load(pickle_out))
        except:
            print("Failas neegzistuoja!")
            with open("biudzetas.pkl", "wb") as pickle_in:
                pickle.dump(biudzeto_masyvas, pickle_in)
    if veiksmas == 3:  # balansas
        try:
            with open("biudzetas.pkl", "rb") as pickle_out:
                masyvas_isl_paj = pickle.load(pickle_out)
                balansas = sum(i for i in masyvas_isl_paj)
                print(balansas)
        except:
            print("Failas neegzistuoja!")
            with open("biudzetas.pkl", "wb") as pickle_in:
                pickle.dump(biudzeto_masyvas, pickle_in)
    if veiksmas == 0:  # uzbaigti programa
        break
