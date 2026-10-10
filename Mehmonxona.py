import json
def jurnalga_yoz(text):
    with open("jurnal.txt", "a") as f:
        f.write(f"[LOG] {text}\n")
class Xona:
    jami = 0
    def __init__(self, raqam, narx, sigim=2):
        self.raqam = raqam
        self.narx = narx
        self.sigim = sigim
        self.__band = False
        self.mehmon = None
        Xona.jami += 1
    def band_mi(self):
        return self.__band
    def band_qil(self, mehmon):
        if self.__band:
            return False
        self.__band = True
        self.mehmon = mehmon
        return True
    def boshat(self):
        self.__band = False
        self.mehmon = None
    def __str__(self):
        if self.__band:
            holat = f"BAND ({self.mehmon.ism})"
        else:
            holat = "bo'sh"
        return f"{self.raqam}-xona | {self.turi()} | {self.narx} so'm | {self.sigim} kishi | {holat}"
    def __gt__(self, other):
        return self.narx > other.narx
class Lyuks(Xona):
    def __init__(self, raqam, narx, sigim=4, nonushta=True):
        super().__init__(raqam, narx, sigim)
        self.nonushta = nonushta
    def turi(self):
        return "Lyuks"
    def __str__(self):
        if self.nonushta is True:
            a = " + nonushta"
            return super().__str__() + a
        else:
            print("")
class Mehmon:
    def __init__(self, ism, telefon):
        self.ism = ism
        self.telefon = telefon
    def __str__(self):
        return f"{self.ism} ({self.telefon})"
class Mehmonxona:
    def __init__(self, nom):
        self.nom = nom
        self.__xonalar = []
    def __len__(self):
        return len(self.__xonalar)
    def __getitem__(self, i):
        return self.__xonalar[i]
    def __str__(self):
        return f"{self.nom}: {len(self)} ta xona"
    def xona_qosh(self, xona):
        self.__xonalar.append(xona)
        print(f"{xona.raqam} - xona qo'shildi ({xona.turi()})")
        jurnalga_yoz(f"{xona.raqam} - xona qo'shildi")
    def top(self, raqam):
        for xona in self.__xonalar:
            if xona.raqam == raqam:
                return xona
        return None
    def joylash(self, raqam, mehmon):
        xona = self.top(raqam)
        if xona is None:
            print("Bunday xona yo'q!")
        elif not xona.band_qil(mehmon):
            print(f"{raqam} - xona allaqachon band!")
        else:
            print(f"{mehmon.ism} {raqam} - xonaga joylashdi")
            jurnalga_yoz(f"{mehmon.ism} {raqam} - xonaga joylashdi")
    def boshat(self, raqam):
        xona = self.top(raqam)
        if xona is None:
            print("Bunday xona yo'q!")
        elif not xona.band_mi():
            print("Bu xona allaqachon bo'sh")
        else:
            ism = xona.mehmon.ism
            xona.boshat()
            print(f"{ism} {raqam} - xonadan chiqdi")
            jurnalga_yoz(f"{ism} {raqam} - xonadan chiqdi")
    def hammasi(self):
        print(self)
        if not self.__xonalar:
            print("(xonalar yo'q)")
        for i in self.__xonalar:
            print("  ", i)
    def eng_qimmat(self):
        if not self.__xonalar:
            return None
        return max(self.__xonalar)
    def daromad(self):
        return sum(
            xona.narx
            for xona in self.__xonalar
            if xona.band_mi()
        )

def main():
    print("""
=== 🏨 MEHMONXONA ===
1. Xona qo'shish
2. Barcha xonalar
3. Mehmon joylash
4. Xonani bo'shatish
5. Bo'sh xonalar
6. Eng qimmat xona
7. Bugungi daromad
8. Saqlash
9. Jurnalni ko'rish
0. Chiqish""")
    while True:
        tanlov = input("Tanlang: ").strip()
        try:
            if tanlov == "1":
                pass
            elif tanlov == "2":
                pass
            elif tanlov == "3":
                pass
            elif tanlov == "4":
                raqam = int(input("Xona raqami: "))

            elif tanlov == "5":
                pass
            elif tanlov == "6":
                pass
            elif tanlov == "7":
                print(f"Bugungi daromad: {Mehmonxona.daromad()}so'm")
            elif tanlov == "8":
                pass
            elif tanlov == "9":
                pass
            elif tanlov == "0":
                print(f"Xayr")
                break
            else:
                print("Noto'g'ri tanlov")
        except ValueError:
            print("Son kiriting!")
        finally:
            print(f"[jami xonalar: {len()}]")
main()

