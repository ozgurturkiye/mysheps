import sqlite3
import time

with sqlite3.connect('ciftligim.sqlite') as vt:
    im = vt.cursor()

    im.execute("""CREATE TABLE IF NOT EXISTS sheeps
        (animal_id, name, date_born, gender, registered)""")

class Animal():

    def __init__(self):
        #Do something when instance created
        print("Yeni örnek oluşturuldu")

    @classmethod
    def show_record(cls):  #This method shows record
        print("Kayit listesi.....")
        #Show record from the file
        with sqlite3.connect("ciftligim.sqlite") as vt:
            im = vt.cursor()

            im.execute("""SELECT * FROM sheeps""")
            sheeps_all_data = im.fetchall()  #data tye is list
            #print(sheeps_all_data)
            for i in sheeps_all_data:
                print(i)

    @classmethod
    def show_record_number(cls):  #this method shows record number
        #Show number of record from file
        with sqlite3.connect("ciftligim.sqlite") as vt:
            im = vt.cursor()

            im.execute("""SELECT COUNT(*) FROM sheeps""")  #result is cursor
            sonuc = im.fetchall() #use fetchall to manipulate cursor object :)
            print("Toplam kayıt sayısı: {} ".format(sonuc[0][0]))

    def add_record(self, animal_id, name, date_born, gender):
        #this method add new record
        #Open and connect database
        with sqlite3.connect("ciftligim.sqlite") as vt:
            im = vt.cursor()

            registered = str(time.ctime()) #registered time
            #We created a tuple to add multiple data
            all_data = (animal_id, name, date_born, gender, registered)
            im.execute("""INSERT INTO sheeps VALUES (?, ?, ?, ?, ?)""", all_data)

            #Commitsiz olmaz :)
            vt.commit()

    def del_record(self, del_animal_id):  #this method delete record
        #Open and connect database
        with sqlite3.connect("ciftligim.sqlite") as vt:
            im = vt.cursor()

            #Burada SELECT ile animal_id var mı kontrol edilmeli

            #Daha sonra varsa DELETE çalıştırılmalı
            #Yoksa uyarı verilmeli
            #Son olarak SELECT ile sorgu atıp silinip silinmediği kontrol edilmeli
            #Ona göre silme başarılı mesajı verilmeli

            im.execute("""DELETE FROM sheeps WHERE animal_id = ?""", (del_animal_id))
            print("Silme işlemi başarılı")




#Make your choice !
intro = """
Seciminizi yapiniz!
1-Kayit Ekle(1)
2-Kayitlari Goster(2)
3-Kayit Sayisini Goster(3)
4-Kayit Sil(4)
Q-Çıkış (Q veya q)
"""
print(intro)

while True:
    answer = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if answer == "q":
        print("çıkılıyor...")
        break

    elif answer == "1":  #Adding record
        animal_id  = input("Eklemek istediğiniz hayvanın numarasını giriniz: ")
        name       = input("Eklemek istediğiniz hayvanın adını giriniz: ")
        date_born  = input("Eklemek istediğiniz hayvanın doğum tarihini giriniz: ")
        gender     = input("Hayvanın cinsiyetini giriniz: ")
        obj1 = Animal()
        obj1.add_record(animal_id, name, date_born, gender)

    elif answer == "2":
        Animal.show_record()

    elif answer == "3":
        Animal.show_record_number()

    elif answer == "4":
        animal_id = input("Silmek istediğiniz hayvanın numarasını giriniz: ")
        obj2 = Animal()
        obj2.del_record(animal_id)

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", intro)
