class planer:
    def __init__(self, rok, miesiac, dzien, czy_wolne, numer_dnia_w_roku, czy_dzien_handlowy):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien=dzien
        self.czy_wolne=czy_wolne
        self.numer_dnia_w_roku=numer_dnia_w_roku
        self.czy_dzien_handlowy=czy_dzien_handlowy
    def __str__(self):
        return str(self.rok) + " " + self.miesiac+ " " + self.dzien+ " "  +str(self.czy_wolne)+" " +str(self.numer_dnia_w_roku)+ " " +self.czy_dzien_handlowy
    def ile_dni_do_konca_roku(self):
        ile_dni=365-self.numer_dnia_w_roku
        return ile_dni
    def czy_do_pracy(self):
        if self.czy_wolne==1:
            return print("bazunia dzisiaj wolne śpimy do 13")
        else:
            return print("pobudka gościu idziemy podbijać świat i narzekać cały dzień")


dzien_pierwszy= planer(2023, "styczen", "poniedzialek", 0, 2, "nie" )
print(dzien_pierwszy.ile_dni_do_konca_roku())
dzien_pierwszy.czy_do_pracy()


        
    