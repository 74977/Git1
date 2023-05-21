import datetime
class planer:
    def __init__(self, rok, miesiac, dzien, dzien_tygodnia, nazwa_miesiaca, spotkanie):
        self.rok = rok
        self.miesiac = miesiac
        self.dzien=dzien
        self.dzien_tygodnia=dzien_tygodnia
        self.nazwa_miesiaca=nazwa_miesiaca
        self.spotkanie=spotkanie
    
    def __str__(self):
        return str(self.rok) + " " + str(self.miesiac)+ " " + str(self.dzien)+ " "  +self.nazwa_miesiaca +" "+ self.spotkanie
    
    def dzien_w_roku(self):
        data_1=datetime.date(self.rok,self.miesiac,self.dzien)
        day_of_year = data_1.timetuple().tm_yday
        #return print(data_1)
        return print("Dzień roku: "+ str(day_of_year))
    
    def ile_dni_do_konca_roku(self):
        data_1=datetime.date(self.rok,self.miesiac,self.dzien)
        day_of_year = data_1.timetuple().tm_yday
        ile_dni=365-day_of_year
        return print("Dni do końca roku zostało: " +str(ile_dni))
    
    def czy_wolne(self):
        if self.spotkanie=="":
           return  print("Masz wolne, żadnych planów.")
        else:
           return print("Plany na ten dzień: "+self.spotkanie)

    def ile_miesiecy_do_konca_roku(self):
        if self.miesiac!=12:
            liczba=12-self.miesiac
            return print("Do końca roku zostało miesięcy w liczbie: " + str(liczba) )
        else:
            return print("To już ostatni miesiąc! zaraz zaczynamy nowy rok!")
        


dzien_pierwszy= planer(2023, 1, 2,"poniedziałek","styczeń","Idziemy z Olą na kawę" )
dzien_pierwszy.ile_dni_do_konca_roku()
dzien_pierwszy.dzien_w_roku()
dzien_pierwszy.ile_miesiecy_do_konca_roku()
dzien_pierwszy.czy_wolne()

        
    