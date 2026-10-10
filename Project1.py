class Author:
    def __init__(self,name):
        self.name = name
class LibraryItem:
    def __init__(self,title,subject="umumiy"):
        self.title = title
        self.subject = subject
    def get_info(self):
        return f"{self.title} | mavzu: {self.subject}"
class Book(LibraryItem):
    def __init__(self,title,author,subject="umumiy"):
        super().__init__(title,subject)
        self.author = author
    def get_info(self):
        return f"Kitob: {self.title} - {self.author} | mavzu: {self.subject}"
class Magazine(LibraryItem):
    def __init__(self,title,number):
        super().__init__(title)
        self.number = number
    def get_info(self):
        return f"Jurnal: {self.title} - {self.number}-son"
class DVD(LibraryItem):
    def __init__(self,title,author,subject):
        super().__init__(title,subject)
        self.author = author
    def get_info(self):
        return f"DVD: {self.title} - rej.{self.author} | janr: {self.subject}"
class Catalog:
    def __init__(self):
        self.__items=[]
    def add(self, item):
        self.__items.append(item)
        return f"✅ Katalogga qo'shildi: {item.get_info()}"
    def get_info(self):
        return self.__items
    def search(self,soz):
        for i in self.__items:
            if i.lower()==soz.lower():
                return i
    def hammasi(self):
        return self.__items
    def jami(self):
        return len(self.__items)
def main():
    catalog=Catalog()
    while True:
        print("""===== USTUDY KUTUBXONA (OOP) =====
1. Kitob qo'shish
2. Jurnal qo'shish
3. DVD qo'shish
4. Qidirish
5. Hammasini ko'rsatish
0. Chiqish""")

        try:
            tanlov=int(input("Tanlang: "))
        except ValueError:
            print("Bunday bo'lim yo'q!")
            continue
        if tanlov == 1:
            title=input("Kitob nomi: ")
            author=input("Muallifi: ")
            subject=input("Mavzu (Enter = umumiy): ")
            if subject == "":
                subject = "umumiy"
            book=Book(title,author,subject)
            print(catalog.add(book))
        elif tanlov == 2:
            title = input("Jurnal nomi: ")
            try:
                number = int(input("Nechanchi son? "))
                magazine = Magazine(title,number)
                print(catalog.add(magazine))
            except ValueError:
                print("Xato: Son kiriting!")
        elif tanlov == 3:
            title = input("DVD nomi: ")
            author = input("Rejissor: ")
            subject = input("Janri: ")
            dvd = DVD(title, author,subject)
            print(catalog.add(dvd))
        elif tanlov == 4:
            soz = input("Qidirish: ")
            catalog.search(soz)
        elif tanlov == 5:
            catalog.hammasi()
        elif tanlov == 0:
            print("Dastur tugadi!")
            break
        else:
            print("Xato")
main()
