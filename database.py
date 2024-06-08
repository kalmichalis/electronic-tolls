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
import sqlite3
from datetime import date


"""Η λογική πάει ως εξής: Θες μια κλάση που να λειτουργεί ως διεπαφή προγράμματος και βάσης δεδομένων. Κάθε μέθοδος επιτελεί
μια από τις λειτουργίες της sqlite3, προσαρμοσμένες στις ανάγκες του προγράμματος. Προσοχή στον κώδικα της insert() και της
update(). Κάθε φορά που πάει να γίνει εισαγωγή στο ιστορικό ελέγχεται αν έχει ήδη καταγραφεί το όχημα, όπότε γίνεται
απλά επικαιροποίηση στοιχείων με την update(). Αυτό συνδέεται και με τον λόγο που καταγράφεται η ημερομηνία. Η λογική
λέει ότι ο χρήστης θα θέλει να δει τα διάφορα στατιστικά (σύνολο πληρωμών, διελεύσεων, μέσους όρους κτλ) για ένα
συγκεκριμένο διάστημα, για ένα όχημα ή για όλα. Διαφορετικά θέλει να δει διαχρονικά έσοδα και διελεύσεις. Όλα αυτά
φαίνονται και στα queries του main.py"""

class DatabaseInterface():
    def __init__(self, cursor):
        self.cursor = cursor

    def insert(self,command, data):
        try:
            time = date.today()
            data.append(time)
            sq = "SELECT card_id, date FROM report WHERE card_id = {} AND date = '{}'"
            self.cursor.execute(sq.format(data[0], data[len(data)-1]))
            if self.cursor.fetchall(): self.update(data)
            else: self.cursor.execute(command, data)
        except sqlite3.Error as error:
            print("Σφάλμα! Η εισαγωγή δεν ολοκληρώθηκε ", error)


    # Εδώ αναγκαστικά πρέπει το id να βγεί από τη λίστα και να προστεθεί στο τέλος για να μπορεί να εκτελεστεί το query command
    def update(self, data):
        try:
            kwdikos = data.pop(0)
            data.append(kwdikos)
            command = """UPDATE report SET car_passage = car_passage + ?, tolls = tolls + ?, account = ?, date = ? 
            WHERE card_id = ?"""
            self.cursor.execute(command, data)
        except sqlite3.Error as error:
            print("Σφάλμα! Η εισαγωγή δεν ολοκληρώθηκε ", error)




    def delete(self, command):
        statement = ""
        try:
            self.cursor.execute(command)
            if self.cursor.rowcount == 0: raise sqlite3.Error
            else: statement = "Η διαγραφή ολοκληρώθηκε!"
        except sqlite3.Error as error:
            print(f"Σφάλμα! Η διαγραφή δεν ολοκληρώθηκε {error}")
        return statement



    def select(self, command):
        records = self.cursor.execute(command).fetchall()
        return records
