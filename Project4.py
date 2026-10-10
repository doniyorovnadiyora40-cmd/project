# import json
# def jurnalga_yoz(matn):
#     with open("jurnal.txt", "a", encoding="utf-8") as f:
#         f.write(f"[LOG] {matn}\n")
# class Xona:
#     jami = 0                      # klass atributi — nechta xona yaratildi
#
#     def __init__(self, raqam, narx, sigim=2):
#         self.raqam = raqam
#         self.narx = narx
#         self.sigim = sigim
#         self.__band = False        # private: faqat metod orqali o'zgaradi
#         self.mehmon = None
#         Xona.jami += 1
#
#     def band_mi(self):
#         return self.__band
#
#     def band_qil(self, mehmon):
#         if self.__band:
#             return False
#         self.__band = True
#         self.mehmon = mehmon
#         return True
#
#     def boshat(self):
#         self.__band = False
#         self.mehmon = None
#
#     def turi(self):
#         return "Oddiy"
#
#     def __str__(self):
#         holat = f"BAND ({self.mehmon.ism})" if self.__band else "bo'sh"
#         return f"{self.raqam}-xona | {self.turi():7} | {self.narx:>7} so'm | {self.sigim} kishi | {holat}"
#
#     def __gt__(self, other):
#         return self.narx > other.narx
# # 💬 Tekshiruv: x = Xona(101, 200000); print(x) → __str__ formatini solishtiring. x.__band → AttributeError bo'lishi shart.
#
# class Lyuks(Xona):
#     def __init__(self, raqam, narx, sigim=4, nonushta=True):
#         super().__init__(raqam, narx, sigim)
#         self.nonushta = nonushta
#
#     def turi(self):
#         return "Lyuks"
#
#     def __str__(self):
#         qoshimcha = " + nonushta" if self.nonushta else ""
#         return super().__str__() + qoshimcha
#
# class Mehmon:
#     def __init__(self, ism, telefon):
#         self.ism = ism
#         self.telefon = telefon
#
#     def __str__(self):
#         return f"{self.ism} ({self.telefon})"
# # 💬 Polimorfizm: hammasi() siklida if type() yo'q — har xona o'zi to'g'ri chiqadi.
#
# class Mehmonxona:
#     def __init__(self, nom):
#         self.nom = nom
#         self.__xonalar = []
#
#     def __len__(self):
#         return len(self.__xonalar)
#
#     def __getitem__(self, i):
#         return self.__xonalar[i]
#
#     def __str__(self):
#         return f"🏨 {self.nom}: {len(self)} ta xona"
#
#     def xona_qosh(self, xona):
#         self.__xonalar.append(xona)
#         print(f"✅ {xona.raqam}-xona qo'shildi ({xona.turi()})")
#         jurnalga_yoz(f"{xona.raqam}-xona qo'shildi")
#
#     def top(self, raqam):
#         for x in self.__xonalar:
#             if x.raqam == raqam:
#                 return x
#         return None
#
#     def joylash(self, raqam, mehmon):
#         xona = self.top(raqam)
#         if xona is None:
#             print(" Bunday xona yo'q!")
#         elif not xona.band_qil(mehmon):
#             print(f"{raqam}-xona allaqachon band!")
#         else:
#             print(f" {mehmon.ism} {raqam}-xonaga joylashdi")
#             jurnalga_yoz(f"{mehmon.ism} {raqam}-xonaga joylashdi")
#
#     def boshat(self, raqam):
#         xona = self.top(raqam)
#         if xona is None:
#             print("❌ Bunday xona yo'q!")
#         elif not xona.band_mi():
#             print("❌ Bu xona allaqachon bo'sh")
#         else:
#             ism = xona.mehmon.ism
#             xona.boshat()
#             print(f"👋 {ism} {raqam}-xonadan chiqdi")
#             jurnalga_yoz(f"{ism} {raqam}-xonadan chiqdi")
#
#     def hammasi(self):
#         print(self)
#         if not self.__xonalar:
#             print("   (xonalar yo'q)")
#         for x in self.__xonalar:
#             print("  ", x)
#
#     def boshlar(self):
#         return [x for x in self.__xonalar if not x.band_mi()]
#
#     def eng_qimmat(self):
#         if not self.__xonalar:
#             return None
#         return max(self.__xonalar)          # __gt__ orqali ishlaydi
#
#     def daromad(self):
#         return sum(x.narx for x in self.__xonalar if x.band_mi())
#
#     def saqla(self, fayl="mehmonxona.json"):
#         data = []
#         for x in self.__xonalar:
#             data.append({
#                 "raqam": x.raqam, "narx": x.narx, "sigim": x.sigim,
#                 "lyuks": isinstance(x, Lyuks),
#                 "mehmon": None if x.mehmon is None else [x.mehmon.ism, x.mehmon.telefon],
#             })
#         with open(fayl, "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent=2)
#         print(f"💾 {len(data)} ta xona saqlandi → {fayl}")
#         jurnalga_yoz(f"{len(data)} ta xona saqlandi")
#
#     @classmethod
#     def yukla(cls, nom, fayl="mehmonxona.json"):
#         m = cls(nom)
#         try:
#             with open(fayl, "r", encoding="utf-8") as f:
#                 data = json.load(f)
#         except FileNotFoundError:
#             print("ℹ️ Saqlangan fayl topilmadi — bo'sh mehmonxona ochildi")
#             return m
#         for d in data:
#             if d["lyuks"]:
#                 x = Lyuks(d["raqam"], d["narx"], d["sigim"])
#             else:
#                 x = Xona(d["raqam"], d["narx"], d["sigim"])
#             if d["mehmon"]:
#                 x.band_qil(Mehmon(*d["mehmon"]))
#             m.xona_qosh(x)
#         print(f"📂 {len(m)} ta xona yuklandi")
#         jurnalga_yoz(f"{len(m)} ta xona fayldan yuklandi")
#         return m
#
# def menyu():
#     print("""
# === MEHMONXONA ===
# 1. Xona qo'shish
# 2. Barcha xonalar
# 3. Mehmon joylash
# 4. Xonani bo'shatish
# 5. Bo'sh xonalar
# 6. Eng qimmat xona
# 7. Bugungi daromad
# 8. Saqlash
# 9. Jurnalni ko'rish
# 0. Chiqish""")
#
#
# def main():
#     m = Mehmonxona.yukla("Ustudy Hotel")
#     while True:
#         menyu()
#         tanlov = input("Tanlang: ").strip()
#         try:
#             if tanlov == "1":
#                 raqam = int(input("Xona raqami: "))
#                 if m.top(raqam):
#                     print("❌ Bu raqamli xona bor!")
#                     continue
#                 narx = int(input("Narxi: "))
#                 turi = input("Turi (oddiy/lyuks): ").strip().lower()
#                 if turi == "lyuks":
#                     m.xona_qosh(Lyuks(raqam, narx))
#                 else:
#                     m.xona_qosh(Xona(raqam, narx))
#             elif tanlov == "2":
#                 m.hammasi()
#             elif tanlov == "3":
#                 raqam = int(input("Xona raqami: "))
#                 ism = input("Mehmon ismi: ")
#                 tel = input("Telefon: ")
#                 m.joylash(raqam, Mehmon(ism, tel))
#             elif tanlov == "4":
#                 m.boshat(int(input("Xona raqami: ")))
#             elif tanlov == "5":
#                 bosh = m.boshlar()
#                 print(f"Bo'sh xonalar: {len(bosh)} ta")
#                 for x in bosh:
#                     print("  ", x)
#             elif tanlov == "6":
#                 x = m.eng_qimmat()
#                 print("💎", x if x else "Xonalar yo'q")
#             elif tanlov == "7":
#                 print(f"Bugungi daromad: {m.daromad()} so'm")
#             elif tanlov == "8":
#                 m.saqla()
#             elif tanlov == "9":
#                 try:
#                     with open("jurnal.txt", "r", encoding="utf-8") as f:
#                         print(f.read().strip() or "(jurnal bo'sh)")
#                 except FileNotFoundError:
#                     print("(jurnal hali yaratilmagan)")
#             elif tanlov == "0":
#                 m.saqla()
#                 print("Xayr!")
#                 break
#             else:
#                 print("Noto'g'ri tanlov")
#         except ValueError:
#             print("Son kiriting!")
#         finally:
#             print(f"[jami xonalar: {len(m)}]")
#
#
# if __name__ == "__main__":
#     main()
# 💬 finally ni ko'rsatish uchun: harf kiriting → except ishlaydi, lekin baribir [jami xonalar: N] chiqadi.
#
# # 1) Kunlar + @property (Lyuks ichida):
#     @property
#     def narx(self):
#         return self._narx + (50000 if self.nonushta else 0)
#     # Xona.__init__ da self.narx -> self._narx deb yozing, Xona da ham @property qo'ying
#
#     # joylashda: kun = int(input("Necha kun? ")) ; xona.kun = kun
#     def daromad(self):
#         return sum(x.narx * x.kun for x in self.__xonalar if x.band_mi())
#
# # 2) Vaqt bilan log:
# from datetime import datetime
#
# def jurnalga_yoz(matn):
#     vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("jurnal.txt", "a", encoding="utf-8") as f:
#         f.write(f"[{vaqt}] {matn}\n")
#
# # 3) Jurnal statistikasi (9-bo'limga):
#     try:
#         with open("jurnal.txt", "r", encoding="utf-8") as f:
#             kirdi = chiqdi = 0
#             for qator in f:
#                 if "joylashdi" in qator:
#                     kirdi += 1
#                 elif "chiqdi" in qator:
#                     chiqdi += 1
#         print(f"📊 Joylashgan: {kirdi} | Chiqqan: {chiqdi}")
#     except FileNotFoundError:
#         print("(jurnal hali yaratilmagan)")
#
# # 4) Mehmon bo'yicha qidiruv (Mehmonxona ichida):
#     def kim_qayerda(self, ism):
#         for x in self.__xonalar:
#             if x.band_mi() and x.mehmon.ism.lower() == ism.lower():
#                 return x
#         return None
# 💬 Jurnal statistikasi — fayldan O'QISH mashqi: for qator in f — har qatorni tekshirish. 8-darsdagi strip() ni eslating.
#
# 📦 To'liq tayyor kod (mehmonxona.py)
# Hammasi birlashtirilgan holda — dars oxirida solishtirish uchun:
#
# 📋 Nusxalash
# # -*- coding: utf-8 -*-
# """
# Ustudy — 2-modul oylik amaliyot: MEHMONXONA BOSHQARUV TIZIMI
# Mavzular: class/obyekt, meros, super(), private, dunder (__str__, __len__, __getitem__),
#           @classmethod, fayllar ('a', 'w', 'r'), json, with, try/except/finally
# """
# import json
#
#
# # ---------- 1. JURNAL: har bir amalni jurnal.txt ga yozadi ('a' rejim) ----------
# def jurnalga_yoz(matn):
#     with open("jurnal.txt", "a", encoding="utf-8") as f:
#         f.write(f"[LOG] {matn}\n")
#
#
# # ---------- 2. XONA klassi ----------
# class Xona:
#     jami = 0                      # klass atributi — nechta xona yaratildi
#
#     def __init__(self, raqam, narx, sigim=2):
#         self.raqam = raqam
#         self.narx = narx
#         self.sigim = sigim
#         self.__band = False        # private: faqat metod orqali o'zgaradi
#         self.mehmon = None
#         Xona.jami += 1
#
#     def band_mi(self):
#         return self.__band
#
#     def band_qil(self, mehmon):
#         if self.__band:
#             return False
#         self.__band = True
#         self.mehmon = mehmon
#         return True
#
#     def boshat(self):
#         self.__band = False
#         self.mehmon = None
#
#     def turi(self):
#         return "Oddiy"
#
#     def __str__(self):
#         holat = f"BAND ({self.mehmon.ism})" if self.__band else "bo'sh"
#         return f"{self.raqam}-xona | {self.turi():7} | {self.narx:>7} so'm | {self.sigim} kishi | {holat}"
#
#     def __gt__(self, other):
#         return self.narx > other.narx
#
#
# # ---------- 3. LYUKS — meros + override + super() ----------
# class Lyuks(Xona):
#     def __init__(self, raqam, narx, sigim=4, nonushta=True):
#         super().__init__(raqam, narx, sigim)
#         self.nonushta = nonushta
#
#     def turi(self):
#         return "Lyuks"
#
#     def __str__(self):
#         qoshimcha = " + nonushta" if self.nonushta else ""
#         return super().__str__() + qoshimcha
#
#
# # ---------- 4. MEHMON ----------
# class Mehmon:
#     def __init__(self, ism, telefon):
#         self.ism = ism
#         self.telefon = telefon
#
#     def __str__(self):
#         return f"{self.ism} ({self.telefon})"
#
#
# # ---------- 5. MEHMONXONA — konteyner klass ----------
# class Mehmonxona:
#     def __init__(self, nom):
#         self.nom = nom
#         self.__xonalar = []       # private ro'yxat
#
#     # --- dunderlar ---
#     def __len__(self):
#         return len(self.__xonalar)
#
#     def __getitem__(self, i):
#         return self.__xonalar[i]
#
#     def __str__(self):
#         return f"🏨 {self.nom}: {len(self)} ta xona"
#
#     # --- asosiy amallar ---
#     def xona_qosh(self, xona):
#         self.__xonalar.append(xona)
#         print(f"✅ {xona.raqam}-xona qo'shildi ({xona.turi()})")
#         jurnalga_yoz(f"{xona.raqam}-xona qo'shildi")
#
#     def top(self, raqam):
#         for x in self.__xonalar:
#             if x.raqam == raqam:
#                 return x
#         return None
#
#     def joylash(self, raqam, mehmon):
#         xona = self.top(raqam)
#         if xona is None:
#             print("❌ Bunday xona yo'q!")
#         elif not xona.band_qil(mehmon):
#             print(f"❌ {raqam}-xona allaqachon band!")
#         else:
#             print(f"🔑 {mehmon.ism} {raqam}-xonaga joylashdi")
#             jurnalga_yoz(f"{mehmon.ism} {raqam}-xonaga joylashdi")
#
#     def boshat(self, raqam):
#         xona = self.top(raqam)
#         if xona is None:
#             print("❌ Bunday xona yo'q!")
#         elif not xona.band_mi():
#             print("❌ Bu xona allaqachon bo'sh")
#         else:
#             ism = xona.mehmon.ism
#             xona.boshat()
#             print(f"👋 {ism} {raqam}-xonadan chiqdi")
#             jurnalga_yoz(f"{ism} {raqam}-xonadan chiqdi")
#
#     def hammasi(self):
#         print(self)
#         if not self.__xonalar:
#             print("   (xonalar yo'q)")
#         for x in self.__xonalar:
#             print("  ", x)
#
#     def boshlar(self):
#         return [x for x in self.__xonalar if not x.band_mi()]
#
#     def eng_qimmat(self):
#         if not self.__xonalar:
#             return None
#         return max(self.__xonalar)          # __gt__ orqali ishlaydi
#
#     def daromad(self):
#         return sum(x.narx for x in self.__xonalar if x.band_mi())
#
#     # --- fayl bilan ishlash ---
#     def saqla(self, fayl="mehmonxona.json"):
#         data = []
#         for x in self.__xonalar:
#             data.append({
#                 "raqam": x.raqam, "narx": x.narx, "sigim": x.sigim,
#                 "lyuks": isinstance(x, Lyuks),
#                 "mehmon": None if x.mehmon is None else [x.mehmon.ism, x.mehmon.telefon],
#             })
#         with open(fayl, "w", encoding="utf-8") as f:
#             json.dump(data, f, ensure_ascii=False, indent=2)
#         print(f"💾 {len(data)} ta xona saqlandi → {fayl}")
#         jurnalga_yoz(f"{len(data)} ta xona saqlandi")
#
#     @classmethod
#     def yukla(cls, nom, fayl="mehmonxona.json"):
#         m = cls(nom)
#         try:
#             with open(fayl, "r", encoding="utf-8") as f:
#                 data = json.load(f)
#         except FileNotFoundError:
#             print("ℹ️ Saqlangan fayl topilmadi — bo'sh mehmonxona ochildi")
#             return m
#         for d in data:
#             if d["lyuks"]:
#                 x = Lyuks(d["raqam"], d["narx"], d["sigim"])
#             else:
#                 x = Xona(d["raqam"], d["narx"], d["sigim"])
#             if d["mehmon"]:
#                 x.band_qil(Mehmon(*d["mehmon"]))
#             m.xona_qosh(x)
#         print(f"📂 {len(m)} ta xona yuklandi")
#         jurnalga_yoz(f"{len(m)} ta xona fayldan yuklandi")
#         return m
#
#
# # ---------- 6. MENYU ----------
# def menyu():
#     print("""
# === 🏨 MEHMONXONA ===
# 1. Xona qo'shish
# 2. Barcha xonalar
# 3. Mehmon joylash
# 4. Xonani bo'shatish
# 5. Bo'sh xonalar
# 6. Eng qimmat xona
# 7. Bugungi daromad
# 8. Saqlash
# 9. Jurnalni ko'rish
# 0. Chiqish""")
#
#
# def main():
#     m = Mehmonxona.yukla("Ustudy Hotel")
#     while True:
#         menyu()
#         tanlov = input("Tanlang: ").strip()
#         try:
#             if tanlov == "1":
#                 raqam = int(input("Xona raqami: "))
#                 if m.top(raqam):
#                     print("❌ Bu raqamli xona bor!")
#                     continue
#                 narx = int(input("Narxi: "))
#                 turi = input("Turi (oddiy/lyuks): ").strip().lower()
#                 if turi == "lyuks":
#                     m.xona_qosh(Lyuks(raqam, narx))
#                 else:
#                     m.xona_qosh(Xona(raqam, narx))
#             elif tanlov == "2":
#                 m.hammasi()
#             elif tanlov == "3":
#                 raqam = int(input("Xona raqami: "))
#                 ism = input("Mehmon ismi: ")
#                 tel = input("Telefon: ")
#                 m.joylash(raqam, Mehmon(ism, tel))
#             elif tanlov == "4":
#                 m.boshat(int(input("Xona raqami: ")))
#             elif tanlov == "5":
#                 bosh = m.boshlar()
#                 print(f"🟢 Bo'sh xonalar: {len(bosh)} ta")
#                 for x in bosh:
#                     print("  ", x)
#             elif tanlov == "6":
#                 x = m.eng_qimmat()
#                 print("💎", x if x else "Xonalar yo'q")
#             elif tanlov == "7":
#                 print(f"💰 Bugungi daromad: {m.daromad()} so'm")
#             elif tanlov == "8":
#                 m.saqla()
#             elif tanlov == "9":
#                 try:
#                     with open("jurnal.txt", "r", encoding="utf-8") as f:
#                         print(f.read().strip() or "(jurnal bo'sh)")
#                 except FileNotFoundError:
#                     print("(jurnal hali yaratilmagan)")
#             elif tanlov == "0":
#                 m.saqla()
#                 print("👋 Xayr!")
#                 break
#             else:
#                 print("❌ Noto'g'ri tanlov")
#         except ValueError:
#             print("❌ Son kiriting!")
#         finally:
#             print(f"[jami xonalar: {len(m)}]")
#
#
# if __name__ == "__main__":
#     main()
# Ustudy • Python 2-modul oylik amaliyoti • Mehmonxona — o'qituvchi varianti