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
        a = " + nonushta" if self.nonushta else ""
        return super().__str__() + a
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
        print(f"{xona.raqam}-xona qo'shildi ({xona.turi()})")
        jurnalga_yoz(f"{xona.raqam}-xona qo'shildi")

    def top(self, raqam):
        for i in self.__xonalar:
            if i.raqam == raqam:
                return i
        return None

    def joylash(self, raqam, mehmon):
        xona = self.top(raqam)

        if xona is None:
            print("Bunday xona yo'q!")
        elif not xona.band_qil(mehmon):
            print(f"{raqam}-xona allaqachon band!")
        else:
            print(f"{mehmon.ism} {raqam}-xonaga joylashdi")
            jurnalga_yoz(f"{mehmon.ism} {raqam}-xonaga joylashdi")

    def boshat(self, raqam):
        xona = self.top(raqam)

        if xona is None:
            print("Bunday xona yo'q!")
        elif not xona.band_mi():
            print("Bu xona allaqachon bo'sh")
        else:
            ism = xona.mehmon.ism
            xona.boshat()
            print(f"{ism} {raqam}-xonadan chiqdi")
            jurnalga_yoz(f"{ism} {raqam}-xonadan chiqdi")

    def hammasi(self):
        print(self)
        if not self.__xonalar:
            print("  (xonalar yo'q)")

        for xona in self.__xonalar:
            print("  ", xona)

    def boshlar(self):
        return [xona for xona in self.__xonalar if not xona.band_mi()]

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

    def saqla(self, fayl="mehmonxona.json"):
        data = []

        for xona in self.__xonalar:
            data.append({
                "raqam": xona.raqam,
                "narx": xona.narx,
                "sigim": xona.sigim,
                "lyuks": isinstance(xona, Lyuks),
                "mehmon": None if xona.mehmon is None else [
                    xona.mehmon.ism,
                    xona.mehmon.telefon
                ]
            })

        with open(fayl, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"💾 {len(data)} ta xona saqlandi")
        jurnalga_yoz(f"{len(data)} ta xona saqlandi")

    @classmethod
    def yukla(cls, nom, fayl="mehmonxona.json"):
        m = cls(nom)

        try:
            with open(fayl, "r", encoding="utf-8") as f:
                data = json.load(f)

        except FileNotFoundError:
            print("ℹ️ Saqlangan fayl topilmadi")
            return m

        for d in data:
            if d["lyuks"]:
                xona = Lyuks(
                    d["raqam"],
                    d["narx"],
                    d["sigim"]
                )
            else:
                xona = Xona(
                    d["raqam"],
                    d["narx"],
                    d["sigim"]
                )

            if d["mehmon"]:
                xona.band_qil(
                    Mehmon(
                        d["mehmon"][0],
                        d["mehmon"][1]
                    )
                )

            m.xona_qosh(xona)

        print(f"📂 {len(m)} ta xona yuklandi")
        return m


def main():
    m = Mehmonxona.yukla("Ustudy Hotel")

    while True:
        menyu()
        tanlov = input("Tanlang: ").strip()

        try:
            if tanlov == "1":
                raqam = int(input("Xona raqami: "))

                if m.top(raqam):
                    print("❌ Bu raqamli xona bor!")
                    continue

                narx = int(input("Narxi: "))
                turi = input("Turi (oddiy/lyuks): ").strip().lower()

                if turi == "lyuks":
                    m.xona_qosh(Lyuks(raqam, narx))
                else:
                    m.xona_qosh(Xona(raqam, narx))

            elif tanlov == "2":
                m.hammasi()

            elif tanlov == "3":
                raqam = int(input("Xona raqami: "))
                ism = input("Mehmon ismi: ")
                telefon = input("Telefon: ")

                mehmon = Mehmon(ism, telefon)
                m.joylash(raqam, mehmon)

            elif tanlov == "4":
                raqam = int(input("Xona raqami: "))
                m.boshat(raqam)

            elif tanlov == "5":
                bosh = m.boshlar()

                print(f"🟢 Bo'sh xonalar: {len(bosh)} ta")

                for xona in bosh:
                    print("  ", xona)

            elif tanlov == "6":
                xona = m.eng_qimmat()

                if xona:
                    print("💎", xona)
                else:
                    print("Xonalar yo'q")

            elif tanlov == "7":
                print(f"💰 Bugungi daromad: {m.daromad()} so'm")

            elif tanlov == "8":
                m.saqla()

            elif tanlov == "9":
                try:
                    with open("jurnal.txt", "r", encoding="utf-8") as f:
                        text = f.read().strip()

                        if text:
                            print(text)
                        else:
                            print("(jurnal bo'sh)")

                except FileNotFoundError:
                    print("(jurnal hali yaratilmagan)")

            elif tanlov == "0":
                m.saqla()
                print("👋 Xayr!")
                break

            else:
                print("❌ Noto'g'ri tanlov")

        except ValueError:
            print("❌ Son kiriting!")

        finally:
            print(f"[jami xonalar: {len(m)}]")


if __name__ == "__main__":
    main()