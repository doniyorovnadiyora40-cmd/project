class Avto:
    __jami = 0

    def __init__(self, model, narx, rang="oq", egasi=None):
        self.model = model
        self.narx = narx
        self.rang = rang
        self.egasi = egasi
        Avto.__jami += 1

    def get_info(self):
        if self.egasi:
            holat = f"egasi: {self.egasi.ism}"
        else:
            holat = "sotuvda"
        return f"{self.rang} {self.model} - {self.narx}$ ({holat})"

    def __str__(self):
        return self.get_info()

    def __gt__(self, other):
        return self.narx > other.narx

    @classmethod
    def jami_yaratilgan(cls):
        return cls.__jami


class ElektroAvto(Avto):
    def __init__(self, model, narx, rang, zaryad_km, egasi=None):
        super().__init__(model, narx, rang, egasi)
        self.zaryad_km = zaryad_km

    def get_info(self):
        if self.egasi:
            holat = f"egasi: {self.egasi.ism}"
        else:
            holat = "sotuvda"
        return f"{self.rang} {self.model} - {self.narx}$ | zaryad: {self.zaryad_km} km ({holat})"


class Mijoz:
    def __init__(self, ism, tel):
        self.ism = ism
        self.tel = tel

    def get_info(self):
        return f"{self.ism} | tel: {self.tel}"


class Salon:
    def __init__(self, nom):
        self.nom = nom
        self.__avtolar = []

    def add(self, avto):
        self.__avtolar.append(avto)
        return f"✅ Salonga qo'shildi: {avto}"

    def hammasi(self):
        return self.__avtolar

    def sotuvda(self):
        return [a for a in self.__avtolar if a.egasi is None]

    def __len__(self):
        return len(self.__avtolar)

    def __getitem__(self, index):
        return self.__avtolar[index]

    def eng_qimmat(self):
        sotuvdagi = self.sotuvda()
        if len(sotuvdagi) == 0:
            return None
        eng_qimmat = sotuvdagi[0]
        for i in sotuvdagi:
            if i > eng_qimmat:
                eng_qimmat = i
        return eng_qimmat

    def sotish(self, raqam, mijoz):
        if raqam < 0 or raqam >= len(self.__avtolar):
            print("Xato")
            return
        avto = self.__avtolar[raqam]
        if avto.egasi is not None:
            print("Allaqachon sotilgan")
            return
        avto.egasi = mijoz
        print(f"SOTILDI! {avto.model} -> {mijoz.ism}")

    def saqla(self):
        with open("salon.txt", "w") as fayl:
            for i in self.__avtolar:
                fayl.write(i.get_info() + "\n")
        print(f"{len(self.__avtolar)} ta avto faylga saqlandi")

    def yukla(self):
        try:
            with open("salon.txt", "r") as fayl:
                print("Saqlangan salon: ")
                for i in fayl:
                    print(i.strip())
        except FileNotFoundError:
            pass


def main():
    salon = Salon("Ustudy Motors")
    while True:
        print("""===== Ustudy Motors | avtolar: 3 =====
1. Avto qo'shish
2. Elektromobil qo'shish
3. Hammasini ko'rish
4. Sotish
5. Eng qimmat avto
6. Faylga saqlash
7. Fayldan yuklash
0. Chiqish""")
        tanlov = input("Tanlang: ")
        if tanlov == "1":
            model = input("Model: ")

            try:
                narx = int(input("Narx: "))
            except ValueError:
                print("Xato: Son kiriting")

            rang = input("Rang: ")
            if rang == "":
                rang = "oq"
            avto = Avto(model, narx, rang)
            print(salon.add(avto))
        elif tanlov == "2":
            model = input("Model: ")
            try:
                narx = int(input("Narx: "))
            except ValueError:
                print("Xato: Son kiriting!")
                continue
            rang = input("Rang: ")
            if rang == "":
                rang = "oq"
            try:
                zaryad = int(input("Zaryad (km): "))
            except ValueError:
                print("Xato: Son kiriting!")
                continue
            avto = ElektroAvto(model, narx, rang, zaryad)
            print(salon.add(avto))
        elif tanlov == "3":
            if len(salon) == 0:
                print("Salonda avto yo'q")
                continue
            raqam = 1
            for avto in salon.hammasi():
                print(f"{raqam}. {avto}")
                raqam += 1
            print(f"Jami yaratilgan avtolar: {Avto.jami_yaratilgan()} ta")
        elif tanlov == "4":
            try:
                raqam = int(input("Avto raqami: "))
            except ValueError:
                print("Xato: Son kiriting!")
                continue
            ism = input("Mijoz ismi: ")
            tel = input("Mijoz telefoni: ")
            mijoz = Mijoz(ism, tel)
            salon.sotish(raqam, mijoz)
        elif tanlov == "5":
            avto = salon.eng_qimmat()
            if avto:
                print(f"Eng qimmati: {avto}")
            else:
                print("Sotuvda avto yo'q!")
        elif tanlov == "6":
            salon.saqla()
        elif tanlov == "7":
            salon.yukla()
        elif tanlov == "0":
            print("Dastur tugadi.")
            break
        else:
            print("Xato")


main()
