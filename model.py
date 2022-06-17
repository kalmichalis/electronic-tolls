import sqlite3
import database as vasi
import tollClasses as klasi

class mainProgramm():
    def __init__(self):
        self.connection = sqlite3.connect("stoixeiaOximatwn.db")
        self.cursor = self.connection.cursor()

# Τα παρακάτω statements είναι queries πρός βάση δεδομένων. Μπορούν να μπουν και σε λίστα ή σε λεξικό
        self.sql = "SELECT * FROM vehicle;"
        self.sqlin = """INSERT INTO report('card_id', 'car_passage', 'tolls', 'account', 'date') VALUES (?,?,?,?,?);"""
        self.sql1 = "SELECT sum(car_passage), sum(tolls) FROM report WHERE date BETWEEN '{}' and '{}'"
        self.sql2 = """SELECT card_id, carPlate, category, sum(car_passage), sum(tolls), avg(car_passage), avg(tolls), avg(account)
FROM report INNER JOIN vehicle ON card_id = id WHERE date BETWEEN "{}" and "{}" GROUP BY card_id"""
        self.sql3 ="""SELECT card_id, carPlate, category, sum(car_passage), sum(tolls), avg(car_passage), avg(tolls), avg(account)
FROM report INNER JOIN vehicle ON card_id = id WHERE card_id = {} AND date BETWEEN "{}" AND "{}";"""
        self.sql4 ="DELETE FROM vehicle WHERE id = {};"
        self.sql5 = "DELETE FROM report;"


# Δημιουργία αντικειμένου κλάσης του αρχείου vasi
        self.data = vasi.DatabaseInterface(self.cursor)
        self.dedomena = self.data.select(self.sql) # Επιστρέφονται τα δεδομένα του πίνακα vehicle της βάσης (id, category κτλ)
        self.ePasslist = []
        self.aisthitiras = klasi.Aisthitiras() #Κλήση κλάσης του αρχείου klasi με ζητούμενες κλάσεις εκφώνησης

# Σ'αυτό το loop, δημιουργείται κάθε φορά αντικείμενο οχήματος ανάλογα με την κατηγορία του.
# Έπειτα δημιουργείται το αντίστοιχο ePass που συνδέεται μαζί του με τα properties kostos, και το ίδιο το αντικείμενο
        for tags in self.dedomena:
            if tags[2] == "Επιβατικό":
                self.oxima = klasi.Epivatiko(*tags)
                self.ePasslist.append(klasi.ePass(self.oxima.kostos, self.oxima))
            elif tags[2] == "Φορτηγό":
                self.oxima = klasi.Fortigo(*tags)
                self.ePasslist.append(klasi.ePass(self.oxima.kostos, self.oxima))
            else:
                self.oxima = klasi.Dikyklo(*tags)
                self.ePasslist.append(klasi.ePass(self.oxima.kostos, self.oxima))

    def anixneysi(self):
        tyxaio_oxima = self.aisthitiras.anixneyei(self.ePasslist)
        message = "ΑΚΥΡΟ! ΤΟ ΥΠΟΛΟΙΠΟ ΤΗΣ ΚΑΡΤΑΣ ΔΕΝ ΕΠΑΡΚΕΙ"
        if tyxaio_oxima:
            self.data.insert(self.sqlin, tyxaio_oxima.split(", "))
            self.connection.commit()
            message = "ΕΓΚΥΡΟ! ΤΟ ΟΧΗΜΑ ΠΕΡΝΑΕΙ"
        return message

    def totalProfits(self, entry1, entry2):
        """ Μέθοδος που επιστρέφει με τη μορφή λίστας συμβολοσειρών έσοδα και διελεύσεις οχημάτων με βάση συγκεκριμένες
            ημερομηνίες (enty1, entry2)"""
        ektypwsi = "{} {:.2f}" # Με format οι επιστρεφόμενες τιμές μπαίνουν στα brackets και μετατρέπονται σε strings
        stringContainer = [] # Κενή λίστα που θα αποθηκεύσει τον συνδυασμό ektypwsi.format(records)
        records = self.data.select(self.sql1.format(entry1, entry2)) # Κλήση database και αποθήκευση επιστρεφόμενων τιμών σε records
        for element in records: stringContainer.append(ektypwsi.format(*element))
        return stringContainer

    def analysiOximatwn(self, entry1, entry2):
        """ Μέθοδος που επιστρέφει με τη μορφή λίστας συμβολοσειρών στοιχεία για κάθε όχημα από πίνακα report της
            database, με βάση συγκεκριμένες ημερομηνίες (enty1, entry2)"""
        ektypwsi = "{} {} {} {} {:.2f} {:.2f} {:.2f} {:.2f}"
        stringContainer = []
        records = self.data.select(self.sql2.format(entry1, entry2))
        for element in records: stringContainer.append(ektypwsi.format(*element))
        return stringContainer

    def analysiOximatos(self, id, entry1, entry2):
        """ Μέθοδος που επιστρέφει με τη μορφή λίστας συμβολοσειρών στοιχεία για μεμονωμένο όχημα (μέσω παραμέτρου id)
            από πίνακα report της database, με βάση συγκεκριμένες ημερομηνίες (enty1, entry2)"""
        ektypwsi = "{} {} {} {} {:.2f} {:.2f} {:.2f} {:.2f}"
        stringContainer = []
        records = self.data.select(self.sql3.format(id, entry1, entry2))
        for element in records: stringContainer.append(ektypwsi.format(*element))
        return stringContainer

    def del_oximatos(self, id):
        """ Μέθοδος που διαγράφει όχημα από πίνακα report της database (μέσω παραμέτρου id). Επιστρέφει μήνυμα επιτυχίας
            ή αποτυχίας της διαγραφής."""
        message = self.data.delete(self.sql4.format(id))
        self.connection.commit()
        return message

    def del_history(self):
        """ Μέθοδος που διαγράφει τις τιμές του πίνακα report της database. Επιστρέφει μήνυμα επιτυχίας ή αποτυχίας της
            διαγραφής."""
        message= self.data.delete(self.sql5)
        self.connection.commit()
        return message








