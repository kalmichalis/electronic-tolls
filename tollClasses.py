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


import random

"""Η λογική είναι η εξής: Ο αιθητήρας συνδέεται με το ταμείο φτιάχνοντας ένα αντικείμενο της κλάσης. Στην anixneyei()
διαλέγει τυχαία ένα αντικείμενο της ePasslist από τo main.py και καλεί την elegxei() για να δει αν το όχημα που ήδη
έχει συνδεθεί με το ePass (self.oxima = oxima) όταν αρχικοποιήθηκε η ePasslist, έχει υπόλοιπο λογαριασμού μεγαλύτερο
από την τιμή κάθε κατηγ. (self.kostos). Εφόσον συμβαίνει αυτό καλείται η xrewnei() του ePass και μετά του oximaτος. Γινονται
οι διάφορες αλλαγές που νομίζω φαίνονται εύκολα και επιστρέφεται στην anixneyei() η τιμή της xrewsi. Ανάλογα με την τιμή 
της, εκτυπώνεται αν περνάει ή όχι. Το μνμ μπορεί να αλλάξει, αλλά σκέφτομαι μήπως συνδεθεί με κάποιο γραφικό εδώ. Εφόσον
λοιπόν η detection  δεν είναι 0 ενημερώνεται η addAxiaDieleysis() του ταμείου και αποθηκεύεται το κοστος πληρωμής
εκεί axia και οι διελεύσεις. Έτσι, όπως είναι διαμορφωμένος ο κώδικας η κλάση Tameio() μπορεί και να μη χρειάζεται
καθόλου. Με τον πίνακα report και queries, μπορείς να υπολογίσεις ότι θέλεις.Το κράτησα επειδή το λέει στην εκφώνηση.

Tώρα ο λόγος που οι properties του ePass() και του Oxima() είναι έτσι μοιρασμένες είναι λόγω της εκφώνησης της
άσκησης. Λέει καθαρά ότι το ypoloipoLogariasmoy είναι ιδιότητα της ePass. Και το self.code, το id δλδ της κάρτας θα
έπρεπε να είναι property της ePass και μπορεί να γίνει, απλά θα πρέπει να αλλάξει λίγο ο κώδικας στο main.py.
Όλα τα υπόλοιπα properties είναι λογικά τοποθετημένα. Κάτι τελευταίο. Σκόπιμα, επειδή δεν βόλευε τη σύνδεση με τον κώδικα
της βάσης το αντικείμενο της ePass και του οχήματος αποθηκεύει μόνο το νέο ypoloipoLogariasmoy. Θα μπορούσε να αποθηκεύεται και
ο arDieleysewn και οι plirwmes, αλλά τότε θα έπρεπε να αλλάξει ριζικά ο κώδικας του database.py"""


class Aisthitiras():

    def __init__(self):  # auth h klash prepei na sundeetai me tin klash Tameio
        self.tameio = Tameio()
        self.detection = 0

    def anixneyei(self, ePasslist):
        # με τυχαιο τροπο  anixneuei apo tin ePassList ena ePass kai typwnei ton arithmo tou epass 3.a
        ePass = ePasslist[random.randrange(len(ePasslist))]
        self.detection = ePass.elegxei()
        if self.detection != 0:
            self.tameio.addAxiaDieleysis(self.detection)
            return ePass.__str__()


    def __str__(self, invoice=False):
        s1 = "ΆΚΥΡΟ! Το υπόλοιπο της κάρτας δεν επαρκεί"
        s2 = "ΈΓΚΥΡΟ! Το όχημα περνάει"
        if invoice==False: return s1
        else: return s2


class ePass():

    def __init__(self,kostos, oxima):
        self.kostos = kostos
        self.oxima = oxima
        self.ypoloipoLogariasmoy = random.randrange(1, 5)


    def elegxei(self):
        xrewsi = 0
        if self.kostos <= self.ypoloipoLogariasmoy:
            xrewsi = self.xrewnei()
        return xrewsi

    def xrewnei(self):
        self.oxima.xrewnei()
        self.ypoloipoLogariasmoy -= self.kostos
        return self.kostos

    def __str__(self):
        s = f"{self.oxima}, {self.ypoloipoLogariasmoy}"
        return s

class Oxima():
    def __init__(self, code, pinakida, typosoximatos):
        self.code = code
        self.pinakida = pinakida
        self.typosoximatos = typosoximatos
        self.plirwmes = 0
        self.arDieleysewn = 0
        self.kostos = 0

    def xrewnei(self):
        self.arDieleysewn = 1
        self.plirwmes = self.kostos

    def __str__(self):
        s = f"{self.code}, {self.arDieleysewn}, {self.plirwmes}"
        return s

class Epivatiko(Oxima):
    def __init__(self,  code, pinakida, typosoximatos):
        super().__init__(code, pinakida, typosoximatos)
        self.kostos = 1.50


class Dikyklo(Oxima):
    def __init__(self,  code, pinakida, typosoximatos):
        super().__init__(code, pinakida, typosoximatos)
        self.kostos = 0.60


class Fortigo(Oxima):
    def __init__(self,  code, pinakida, typosoximatos):
        super().__init__(code, pinakida, typosoximatos)
        self.kostos = 3.20


class Tameio():

    def __init__(self):
        self.arDieleysewn = 0
        self.esodaDieleysewn = 0

    def addAxiaDieleysis(self, axia):
        self.arDieleysewn += 1
        self.esodaDieleysewn += axia

    def __str__(self):
        s = f"{self.arDieleysewn}, {self.esodaDieleysewn}"
        return s