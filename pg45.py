class Mobile:
    pass

mob1 = Mobile()
mob2  = Mobile()

mob1.price = 2000
mob1.brand = "Apple"
mob1.ios_version = 10

mob2.price = 3000
mob2.brand = "samsung"

mob1.ios_version = 11

mob2.android_version = "Marshmallow"

print(mob1.brand,mob1.ios_version)
print(mob2.brand,mob2.android_version)