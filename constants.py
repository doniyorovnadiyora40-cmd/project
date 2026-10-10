class Author:
    def __init__(self, name):
        self.name = name
class LibraryItem:
    def __init__(self, title, subject="umumiy"):
        self.title = title
        self.subject = subject
    def get_info(self):
        return f'"{self.title}" | mavzu: {self.subject}'
class Book(LibraryItem):
    def __init__(self, title, author, subject="umumiy"):
        super().__init__(title, subject)
        self.author = author
    def get_info(self):
        return f'Kitob: "{self.title}" — {self.author.name} | mavzu: {self.subject}'
class Magazine(LibraryItem):
    def __init__(self, title, issue):
        super().__init__(title, "jurnal")
        self.issue = issue
    def get_info(self):
        return f'Jurnal: "{self.title}" — {self.issue}-son'
class DVD(LibraryItem):
    def __init__(self, title, director, subject="umumiy"):
        super().__init__(title, subject)
        self.director = director
    def get_info(self):
        return f'DVD: "{self.title}" — rej. {self.director} | janr: {self.subject}'
class Catalog:
    def __init__(self):
        self.__items = []
    def add(self, item):
        self.__items.append(item)
        print(f"Katalogga qo'shildi: {item.get_info()}")
    def search(self, soz):
        natija = []
        for item in self.__items:
            if soz.lower() in item.title.lower():
                natija.append(item)
            elif isinstance(item, Book):
                if soz.lower() in item.author.name.lower():
                    natija.append(item)
        return natija
    def hammasi(self):
        return self.__items
    def jami(self):
        return len(self.__items)


    def statistika(self):

        kitob = 0

        jurnal = 0

        dvd = 0

        for item in self.__items:

            if isinstance(item, Book):

                kitob += 1

            elif isinstance(item, Magazine):

                jurnal += 1

            elif isinstance(item, DVD):

                dvd += 1

        print(f"Kitoblar: {kitob} ta")

        print(f"Jurnallar: {jurnal} ta")

        print(f"DVDlar: {dvd} ta")
