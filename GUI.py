# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Καλαποθαράκος Μιχαήλ και Νικολιάς Μπλέτσας Γεώργιος
#
# This file is part of electronic-tolls.
#
# electronic-tolls is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by
# the Free Software Foundation, either version of the License, or
# (at your option) any later version.
#
# electronic-tolls is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.
#
# You should have received a copy of the MIT License
# along with electronic-tolls.  If not, see <https://opensource.org/licenses/MIT>.

from tkcalendar import Calendar
import tkinter as tk
import tkinter.font as f
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import model as m
class windows(tk.Tk):
    """ Κλάση παραθύρου στην οποία βασίζονται όλες οι υποκλάσεις παραθύρων. Θέτει τα βασικά τεχνικά χαρακτηριστικά
        για κάθε παράθυρο (π.χ. μέγεθος) και κάθε μια από τις μεθόδους του δημιουργεί τα αντίστοιχα αισθητικά
        χαρακτηριστικά για τα widgets που χρησιμοποιούνται"""
    def __init__(self):
        super().__init__()
        self.geometry("950x500") # Ορισμός μήκους (άξονας x) και ύψους (άξονας y)

        # Επιστρέφει από τον φάκελο images το .ico αρχείο και το τοποθετέι σαν εικονίδιο στην αρχή του παραθύρου
        self.iconbitmap("images\logo.ico")
        self.title("eTolls") # Η συμβολοσειρά τοποθετείται ως τίτλος δίπλα στο εικονίδιο στην αρχή του παραθύρου
        self.config(bg="#92bfde") # Μια διαβάθμιση του γαλάζιου ως χρώμα backround
        self.resizable(False, False) #Το παράθυρο δεν μπορεί να μεγαλώσει

    def buttons(self, text):
        font = f.Font(family="calibre", size=10, weight="bold") # Ορισμός χαρακτηριστικών γραμματοσειράς

        # Δημιουργία αντικειμένου κουμπιού με συγκεκριμένα αισθητικά χαρακτηριστικά
        aButton = tk.Button(self, bd=2,  height=1, width=42, text=text, font=font,
                       bg="#016bb5", fg="#ffffff", activebackground="#cbdfed")
        return aButton

    def texts(self, text):
        fonts = f.Font(family="calibre", size=10, weight="bold")

        # Δημιουργία αντικειμένου Label (συγκεκριμένα κειμένου) και ορισμός χαρακτηριστικών
        textLabel = tk.Label(self, font=fonts,bg="#92bfde", text=text)
        return textLabel

    def Entries(self):
        font = f.Font(family="calibre", size=10, weight="bold")

        # Δημιουργία αντικειμένου Entry (εγγραφής) με συγκεκριμένα αισθητικά χαρακτηριστικά
        anEntry = tk.Entry(self, bd=2, font=font, highlightcolor='black', width=10)
        return anEntry

class IntroWindow(windows):
    """ Υποκλάση παραθύρου που εμφανίζεται ως εισαγωγή στην εφαρμογή και καταστρέφεται μετά από ένα συγκεκριμένο
        χρονικό διάστημα"""
    def __init__(self):
        super().__init__()

        # Με τη μέθοδο PhotoImage επιστρέφεται από το φάκελο images μια εικόνα που τοποθετέιται στο κέντο του παραθύρου
        self.photo = PhotoImage(file="images\eTolls.png")
        self.label = tk.Label(self, image=self.photo, anchor="center")
        self.label.pack(fill="both", expand=True)
        self.after(1000, lambda: self.destroy())
        self.mainloop()

class reportWin(windows):
    """ Υποκλάση παραθύρου πού όταν καλείται δημιουργεί έναν πίνακα με τα ζητούμενα στατιστικά στοιχεία"""
    def __init__(self, headers, records): # headers = ονόματα στηλών, records= τιμές επιλεγμένων γραμμών από database
        super().__init__()
        self.frame_y = tk.Frame(self) # Πλαίσιο που συγκρατεί κάθετο scrollbar
        self.frame_y.pack(side=RIGHT, fill="y")
        self.frame_x = tk.Frame(self)
        self.frame_x.pack(side=BOTTOM, fill='x') # Πλαίσιο που συγκρατεί οριζόντιο scrollbar

        # Ορισμός αντικειμένου Treeview, που απεικονίζει με μορφή πινάκων τις επιλεγμένες τιμές από database
        self.table = ttk.Treeview(self, columns=headers, show='headings')

        # Σ' αυτόν τον βρόγχο δημιουργούνται οι ονομασίες (headings) κάθε στήλης, σύμφωνα με την παράμετρο headers
        for i in range(len(headers)):
            self.table.heading(headers[i], text=headers[i])

        # Σ' αυτόν τον βρόγχο γεμίζουν οι στήλες του πίνακα με τις τιμές κάθε tuple της records
        for record in records:
            self.table.insert("", tk.END, values= record)

        # Δημιουργία κάθετου scrollbar
        self.yscroll = ttk.Scrollbar(self.frame_y, orient=tk.VERTICAL, command=self.table.yview)
        self.yscroll.pack(expand=True, fill='y')
        # Δημιουργία οριζόντιου scrollbar
        self.xscroll = ttk.Scrollbar(self.frame_x, orient=tk.HORIZONTAL, command=self.table.xview)
        self.xscroll.pack(expand=True, fill='x')
        # Σύνδεση scrollbars με τον πίνακα
        self.table.configure(yscrollcommand=self.yscroll.set, xscrollcommand=self.xscroll.set)
        self.table.pack(fill="both", expand=True)

class Root(windows):
    """ Υποκλάση παραθύρου που αποτελεί και το βασικό παράθυρο της εφαρμογής. Κάθε κουμπί συνδέεται με μια λειτουργία
        (συνάρτηση). Περίπου στο κέντρο εμφανίζεται το αποτελέσμα/μήνυμα του 'Ελέγχου οχήματος'. Αριστερά και δεξιά
        τοποθετούνται οι εγγραφές (Entries) που αφορούν την ημερομηνία και τον Αριθμό Κάρτας."""

    def __init__(self):
        super().__init__()

        # Δημιουργία αντικειμένου της κλάσης mainProgramm του αρχείου model που φέρει τα απαραίτητα data από database
        self.amodel = m.mainProgramm()
        self.count=0 # Μετρητής που θα χρησιμεύσει στη μέθοδο elegxos(), ώστε να ανανεωθούν τα οχήματα που ελέγχονται

        # Κουμπί που τερματίζει το πρόγραμμα με τη μέθοδο quitProgramm
        self.quitApp = self.buttons("ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ")
        self.quitApp.config(command=self.quitProgramm)
        self.quitApp.pack(side= BOTTOM)

        # Κουμπί που επιστρέφει στοιχεία για συγκεκριμένο έγκυρο όχημα της database με τη μέθοδο analysi_oxima.
        self.aVehicle = self.buttons("ΑΝΑΛΥΣΗ ΣΤΟΙΧΕΙΩΝ ΜΕΜΟΝΩΜΕΝΟΥ ΟΧΗΜΑΤΟΣ")
        self.aVehicle.config(command=self.analysi_oxima)
        self.aVehicle.pack(side=BOTTOM)

        # Κουμπί που επιστρέφει στοιχεία για κάθε έγκυρο όχημα της database με τη μέθοδο analysi_oximatwn.
        self.allVehicles = self.buttons("ΑΝΑΛΥΣΗ ΣΤΟΙΧΕΙΩΝ ΓΙΑ ΚΑΘΕ ΟΧΗΜΑ")
        self.allVehicles.config(command=self.analysi_oximatwn)
        self.allVehicles.pack(side=BOTTOM)

        # Κουμπί που επιστρέφει συνολικά έσοδα και διελεύσεις οχημάτων για κάθε έγκυρο όχημα της database με τη μέθοδο analysi_oxima.
        self.totalProfits = self.buttons("ΣΥΝΟΛΙΚΑ ΕΣΟΔΑ-ΔΙΕΛΕΥΣΕΙΣ")
        self.totalProfits.config(command=self.sunolikaesoda)
        self.totalProfits.pack(side=BOTTOM)

        # Κουμπί που διαγράφει όχημα από την database με τη μέθοδο del_oximatos
        self.delVehicle = self.buttons("ΔΙΑΓΡΑΦΗ ΟΧΗΜΑΤΟΣ")
        self.delVehicle.config(command=self.del_oximatos)
        self.delVehicle.pack(side=BOTTOM)

        # Κουμπί που διαγράφει όλες τις τιμές του πίνακα reports της database με τη μέθοδο history
        self.delReports = self.buttons("ΕΚΚΑΘΑΡΙΣΗ ΙΣΤΟΡΙΚΟΥ ΠΡΟΓΡΑΜΜΑΤΟΣ")
        self.delReports.config(command=self.history)
        self.delReports.pack(side=BOTTOM)

        # Κουμπί που ελέγχει αν ένα όχημα περνάει ή όχι με τη μέθοδο elegxos
        self.nextCar= self.buttons("ΔΙΕΛΕΥΣΗ ΟΧΗΜΑΤΟΣ")
        self.nextCar.config(command=self.elegxos)
        self.nextCar.pack(side= BOTTOM)


        # Στοίχιση Entries ημερομηνίας και αριθμού κάρτας και των αντίστοιχων επεξηγήσεών τους
        # Στοίχιση Entries ημερομηνίας και αριθμού κάρτας και των αντίστοιχων επεξηγήσεών τους
        self.timeLabel = self.texts(
            "Καταχώρησε το διάστημα, για το οποίο\nεπιθυμείς την ανάκτηση στοιχείων:\nYYYY-MM-DD").place(x=30, y=60)
        self.apo = self.texts("AΠΟ:").place(x=30, y=140)
        self.apo = self.texts("ΜΕΧΡΙ:").place(x=30, y=170)
        self.arEpass = self.texts("ΑΡΙΘΜΟΣ ΚΑΡΤΑΣ:").place(x=650, y=140)
        self.idLabel = self.texts("Καταχώρησε τον αριθμό ePass\nτου οχήματος αναζήτησης ή διαγραφής:").place(x=650,
                                                                                                             y=60)

        self.datetime_apo = self.Entries()
        self.datetime_apo.place(x=110, y=140)
        self.datetime_mexri = self.Entries()
        self.datetime_mexri.place(x=110, y=170)
        self.carId = self.Entries()
        self.carId.place(x=800, y=140)

        # Προσθήκη κουμπιών για επιλογή ημερομηνίας
        self.apo_button = ttk.Button(self, text="Επιλέξτε Ημερομηνία", command=lambda: self.cal_window(self.datetime_apo))
        self.apo_button.place(x=220, y=140)
        self.mexri_button = ttk.Button(self, text="Επιλέξτε Ημερομηνία", command=lambda: self.cal_window(self.datetime_mexri))
        self.mexri_button.place(x=220, y=170)

        # Αντικείμενο Label που εμφανίζει μήνυμα για το αν ένα όχημα περνάει ή όχι.Τοποθετείται περίπου στο κέντρο
        self.result=self.texts('')
        self.result.place(x=305, y=210)

        self.mainloop()


    def elegxos(self):
        """ Αν πατηθεί το αντίστοιχο κουμπί καλείται η μέθοδος anixneysi του αντικειμένου amodel και εμφανίζεται
            η επιστρεφόμενη συμβολοσειρά ως μήνμα στο παράθυρο. Μετά από 20 επαναλήψεις, ορίζεται εκ νέου το
            αντικείμενο amοdel, ώστε να δημιουργηθούν πάλι τα αντικείμενα ePass της ePasslist με νέους λογαριασμούς
            κάρτας."""

        self.count += 1
        aString = self.amodel.anixneysi()
        if self.count > 20:
            self.count = 0
            aString = "ΑΝΑΝΕΩΣΗ ΟΧΗΜΑΤΩΝ..."
            self.amodel = m.mainProgramm()
        self.result['text']= aString

    def quitProgramm(self):
        """Έξοδος από το πρόγραμμα με την επιλογή του αντίστοιχου κουμπιού"""
        quit()

    def history(self):
        """Αν πατηθεί το αντίστοιχο κουμπί καλείται η μέθοδος del_history του amodel και διαγράφεται ο πίνακας
           report της database. Αν είναι ήδη κενός εμφανίζεται messagebox που ενημερώνει τον χρήστη για σφάλμα"""

        records = self.amodel.del_history()
        if records: messagebox.showinfo("Πληροφορίες", records)
        else: messagebox.showerror("Σφάλμα!", "Το ιστορικό είναι άδειο!")


    def sunolikaesoda(self):
        """Αν πατηθεί το αντίστοιχο κουμπί καλείται η μέθοδος totalProfits του amodel με παραμέτρους τις τιμές του χρήστη
           στα Entries της ημερομηνίας. Αν υπάρχουν επιστρεφόμενες τιμές εμφνίζεται το παράθυρο που δείχνει σε μορφή
           πίνακα τα στατιστικά στοιχεία (εδώ συνολικά έσοδα και διελεύσεις). Διαφορετικά εμφανίζεται messagebox που
           ενημερώνει τον χρήστη για σφάλμα"""

        ektypwseis = ["Συνολικός αριθμός διευλεύσεων οχημάτων","Συνολικά έσοδα(€)"]
        try:
            records = self.amodel.totalProfits(self.datetime_apo.get(), self.datetime_mexri.get())
            if records[0][0] == None: raise BaseException
            else: reportWin(ektypwseis, records)
        except BaseException:
            messagebox.showerror("Σφάλμα!", "Τα στοιχεία ημερομηνίας είναι λανθασμένα ή δεν υπάρχουν καταγεγραμμένα οχήματα!")

    def analysi_oximatwn(self):
        """Αν πατηθεί το αντίστοιχο κουμπί καλείται η μέθοδος analysiOximatwn του amodel με παραμέτρους τις τιμές του χρήστη
           στα Entries της ημερομηνίας. Αν υπάρχουν επιστρεφόμενες τιμές εμφνίζεται το παράθυρο που δείχνει σε μορφή
           πίνακα τα στατιστικά στοιχεία (εδώ στοιχεία για κάθε όχημα). Διαφορετικά εμφανίζεται messagebox που
           ενημερώνει τον χρήστη για σφάλμα"""

        ektypwseis = ["Αριθμός κάρτας:","Αριθμός κυκλοφορίας","Κατηγορία","Αριθμός διελεύσεων","Πληρωμές(€)",
                      "Μέσος όρος διελεύσεων","Μέσος όρος πληρωμών(€)","Μέσος όρος λογαριασμού κάρτας(€)"]
        try:
            records = self.amodel.analysiOximatwn(self.datetime_apo.get(), self.datetime_mexri.get())
            if records[0][0] == None: raise BaseException
            else: reportWin(ektypwseis,records)
        except BaseException:
            messagebox.showerror("Σφάλμα!", "Τα στοιχεία ημερομηνίας είναι λανθασμένα ή δεν υπάρχουν καταγεγραμμένα οχήματα!")

    def analysi_oxima(self):
        """Αν πατηθεί το αντίστοιχο κουμπί καλείται η μέθοδος analysiOximatos του amodel με παραμέτρους τις τιμές του χρήστη
           στα Entries του Αριθμού κάρτας και της ημερομηνίας. Αν υπάρχουν επιστρεφόμενες τιμές εμφνίζεται το παράθυρο
           που δείχνει σε μορφή πίνακα τα στατιστικά στοιχεία (εδώ στοιχεία για μεμονωμένο όχημα). Διαφορετικά
           εμφανίζεται messagebox που ενημερώνει τον χρήστη για σφάλμα"""

        ektypwseis = ["Αριθμός κάρτας:","Αριθμός κυκλοφορίας","Κατηγορία","Αριθμός διελεύσεων","Πληρωμές(€)",
                      "Μέσος όρος διελεύσεων","Μέσος όρος πληρωμών(€)","Μέσος όρος λογαριασμού κάρτας(€)"]
        try:
            records = self.amodel.analysiOximatos(self.carId.get(), self.datetime_apo.get(), self.datetime_mexri.get())
            if records[0][0] == None:
                raise BaseException
            else:
                reportWin(ektypwseis, records)
        except BaseException:
            messagebox.showerror("Σφάλμα!", "Tα στοιχεία ημερομηνίας ή Αριθμού Κάρτας είναι λανθασμένα!")

    def del_oximatos(self):
        """Αν πατηθεί το αντίστοιχο κουμπί καλείται η μέθοδος del_oximatos του amodel με παραμέτρους τις τιμές του χρήστη
           στα Entries του Αριθμού κάρτας. Αν υπάρχουν επιστρεφόμενες τιμές εμφανίζεται διαγράφεται το συγκεκριμένο
           όχημα από τους πίνακες της database. Διαφορετικά εμφανίζεται messagebox που ενημερώνει τον χρήστη για σφάλμα"""

        records = self.amodel.del_oximatos(self.carId.get())
        if records: messagebox.showinfo("Πληροφορίες", records)
        else: messagebox.showerror("Σφάλμα!", "Ο Αριθμός Κάρτας είναι λανθασμένος ή δεν υπάρχει καταγεγραμμένο όχημα"
                                              " με τον συγκεκριμένο Αριθμό Κάρτας!")

    def cal_window(self, date_entry):
        top = tk.Toplevel(self)
        top.title("Ημερολόγιο")

        global cal
        cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.grid(row=0, column=0, padx=10, pady=10)

        ok_button = ttk.Button(top, text="OK", command=lambda: [self.get_date(cal, date_entry), top.destroy()])
        ok_button.grid(row=1, column=0, padx=10, pady=10)

    def get_date(self, cal, date_entry):
        date = cal.selection_get()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, date.strftime("%Y-%m-%d"))



begin = IntroWindow()
root = Root()




