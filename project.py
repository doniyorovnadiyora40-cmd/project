order = []
sum1 = 0
while True:
    zakaz = int(input("""
         MENU
1. Osh
2. Shashlik
3. Somsa
4. Ichimliklar
5. Desertlar
0. Stop
Tanlang: """))

    if zakaz == 0:
        break

    elif zakaz == 1:
        zakaz1 = int(input("""
1. To'y oshi = 35 000
2. Choyxona Palov = 50 000
3. Zig'ir Osh = 70 000
0. Orqaga
Tanlang: """))

        if zakaz1 == 0:
            continue

        elif zakaz1 >= 1 and zakaz1 <= 3:
            count = int(input("Nechta: "))

            if count > 0:
                if zakaz1 == 1:
                    order.append(f"To'y osh - {count} ta")
                    sum1 += 35000 * count

                elif zakaz1 == 2:
                    order.append(f"Choyxona Palov - {count} ta")
                    sum1 += 50000 * count

                elif zakaz1 == 3:
                    order.append(f"Zig'ir osh - {count} ta")
                    sum1 += 70000 * count
            else:
                print("Noto'g'ri raqam.")
        else:
            print("Noto'g'ri raqam.")

    elif zakaz == 2:
        zakaz2 = int(input("""
1. Qiyma shashlik = 22 000
2. Tovuq shashlik = 22 000
3. Jaz shashlik = 28 000
4. Jigar shashlik = 22 000
0. Orqaga
Tanlang: """))

        if zakaz2 == 0:
            continue

        elif zakaz2 >= 1 and zakaz2 <= 4:
            count = int(input("Nechta: "))

            if count > 0:
                if zakaz2 == 1:
                    order.append(f"Qiyma shashlik - {count} ta")
                    sum1 += 22000 * count

                elif zakaz2 == 2:
                    order.append(f"Tovuq shashlik - {count} ta")
                    sum1 += 22000 * count

                elif zakaz2 == 3:
                    order.append(f"Jaz shashlik - {count} ta")
                    sum1 += 28000 * count

                elif zakaz2 == 4:
                    order.append(f"Jigar shashlik - {count} ta")
                    sum1 += 22000 * count
            else:
                print("Noto'g'ri raqam.")
        else:
            print("Noto'g'ri raqam.")

    elif zakaz == 3:
        zakaz3 = int(input("""
1. Kartoshkali somsa = 9 000
2. Tovuqli somsa = 10 000
3. Go'shtli somsa = 17 000
4. Qovoqli somsa = 9 000
5. Go'sht va sabzavotli somsa = 18 000
6. Sous = 10 000
0. Orqaga
Tanlang: """))

        if zakaz3 == 0:
            continue

        elif zakaz3 >= 1 and zakaz3 <= 6:
            count = int(input("Nechta: "))

            if count > 0:
                if zakaz3 == 1:
                    order.append(f"Kartoshkali somsa - {count} ta")
                    sum1 += 9000 * count

                elif zakaz3 == 2:
                    order.append(f"Tovuqli somsa - {count} ta")
                    sum1 += 10000 * count

                elif zakaz3 == 3:
                    order.append(f"Go'shtli somsa - {count} ta")
                    sum1 += 17000 * count

                elif zakaz3 == 4:
                    order.append(f"Qovoqli somsa - {count} ta")
                    sum1 += 9000 * count

                elif zakaz3 == 5:
                    order.append(f"Go'sht va sabzavotli somsa - {count} ta")
                    sum1 += 18000 * count

                elif zakaz3 == 6:
                    order.append(f"Sous - {count} ta")
                    sum1 += 10000 * count
            else:
                print("Noto'g'ri raqam.")
        else:
            print("Noto'g'ri raqam.")

    elif zakaz == 4:
        zakaz4 = int(input("""
1. Choy = 10 000
2. CocaCola/Fanta/Sprite/Pepsi(0.5) = 10 000
3. CocaCola/Fanta/Sprite/Pepsi(1l) = 17 000
4. CocaCola/Fanta/Sprite/Pepsi(1.5) = 20 000
5. Kompot(1l) = 15 000
6. Suv(0.5) = 5 000
0. Orqaga
Tanlang: """))

        if zakaz4 == 0:
            continue

        elif zakaz4 >= 1 and zakaz4 <= 6:
            count = int(input("Nechta: "))

            if count > 0:
                if zakaz4 == 1:
                    order.append(f"Choy - {count} ta")
                    sum1 += 10000 * count

                elif zakaz4 == 2:
                    order.append(
                        f"CocaCola/Fanta/Sprite/Pepsi(0.5) - {count} ta"
                    )
                    sum1 += 10000 * count

                elif zakaz4 == 3:
                    order.append(
                        f"CocaCola/Fanta/Sprite/Pepsi(1l) - {count} ta"
                    )
                    sum1 += 17000 * count

                elif zakaz4 == 4:
                    order.append(
                        f"CocaCola/Fanta/Sprite/Pepsi(1.5) - {count} ta"
                    )
                    sum1 += 20000 * count

                elif zakaz4 == 5:
                    order.append(f"Kompot(1l) - {count} ta")
                    sum1 += 15000 * count

                elif zakaz4 == 6:
                    order.append(f"Suv(0.5) - {count} ta")
                    sum1 += 5000 * count
            else:
                print("Noto'g'ri raqam.")
        else:
            print("Noto'g'ri raqam.")

    elif zakaz == 5:
        zakaz5 = int(input("""
1. San-sebastian = 50 000
2. Chizkeyk = 50 000
3. Tiramisu = 40 000
4. Kruassan = 35 000
5. Rulet = 40 000
0. Orqaga
Tanlang: """))

        if zakaz5 == 0:
            continue

        elif zakaz5 >= 1 and zakaz5 <= 5:
            count = int(input("Nechta: "))

            if count > 0:
                if zakaz5 == 1:
                    order.append(f"San-sebastian - {count} ta")
                    sum1 += 50000 * count

                elif zakaz5 == 2:
                    order.append(f"Chizkeyk - {count} ta")
                    sum1 += 50000 * count

                elif zakaz5 == 3:
                    order.append(f"Tiramisu - {count} ta")
                    sum1 += 40000 * count

                elif zakaz5 == 4:
                    order.append(f"Kruassan - {count} ta")
                    sum1 += 35000 * count

                elif zakaz5 == 5:
                    order.append(f"Rulet - {count} ta")
                    sum1 += 40000 * count
            else:
                print("Noto'g'ri raqam.")
        else:
            print("Noto'g'ri raqam.")

    else:
        print("Noto'g'ri raqam.")

if len(order) == 0:
    print("\nSiz hech qanday ovqat tanlamadingiz.")

else:
    print("\n        CHEK       ")

    for i in order:
        print(i)

    print("")
    print(f"Jami summa: {sum1:} so'm bo'ldi")

    confirm = input("\nBuyurtmangiz to'g'rimi? (ha/yo'q): ").lower()

    if confirm == "ha":
        first_sum = sum1
        discount = 0
        discount1 = 0

        if sum1 > 350000:
            discount = sum1 * 10 // 100
            sum1 -= discount

            print(
                f"\n350 000 so'mdan oshgani uchun "
                f"10% chegirma berildi: {discount:} so'm"
            )

        else:
            print("\n10% chegirma uchun summa 350 000 so'mdan oshishi kerak.")

        promokod = input(
            "\nPromokodingiz bormi? (ha/yo'q): "
        ).lower()

        if promokod == "ha":
            promokod1 = input("Promokodni kiriting: ").upper()

            if promokod1 == "AJOYIB":
                discount1 = sum1 * 10 // 100
                sum1 -= discount1

                print(
                    f"Promokod qabul qilindi. "
                    f"Yana 10% chegirma: {discount1:} so'm"
                )

            else:
                print("Promokod noto'g'ri.")

        elif promokod == "yo'q" or promokod == "yoq":
            print("Promokod ishlatilmadi.")

        else:
            print("Noto'g'ri javob. Promokod ishlatilmadi.")

        print("\n            CHEK           ")

        for i in order:
            print(i)

        print("")
        print(f"Boshlang'ich summa: {first_sum:} so'm")

        if discount > 0:
            print(f"10% chegirma: {discount:} so'm")

        if discount1 > 0:
            print(f"Promokod bilan chegirma: {discount1:} so'm")

        print("")
        print(f"Jami to'lov: {sum1:} so'm")
        print("Buyurtmangiz qabul qilindi. Yoqimli ishtaha!")

    elif confirm == "yo'q" or confirm == "yoq":
        print("Buyurtma bekor qilindi.")

    else:
        print("Noto'g'ri javob kiritildi. Buyurtma tasdiqlanmadi.")
