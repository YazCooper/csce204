#author-yazmin cooper

month = input("Enter Your Birth Month: ").strip().lower()
day = int(input("Enter Your Birth Day: "))

if month == "january" or month == "jan" and day <=21:
    print("Capricorn: Ruby")
elif month == "december" and day <=22:
    print("Capricorn: Ruby")
elif month == "january" and day >= 22:
    print("Aquarius: Garnet")
elif month == "february" and day <= 21:
    print("Aquarius: Garnet")
elif month == "february" and day >= 22:
    print("Pisces: Amethyst")
elif month == "march" and day <= 21:
    print("Pisces: Amethyst")
elif month == "march" and day >= 22:
    print("Aries: Bloodstone")
elif month == "april" and day <= 20:
    print("Aries: Bloodstone")
elif month == "april" and day >= 21:
    print("Taurus: Sapphire")
elif month == "may" and day <=21:
    print("Taurus: Sapphire")
elif month == "may" and day >= 22:
    print("Gemini: Agate")
elif month == "june" and day <= 21:
    print("Gemini: Agate")
elif month == "june" and day >= 22:
    print("Cancer: Emerald")
elif month == "july" and day <= 22:
    print("Cancer: Emerald")
elif month == "july" and day >= 23:
    print("Leo: Onyx")
elif month == "august" and day <= 22:
    print("Leo: Onyx")
elif month == "august" and day >=23:
    print("Virgo: Carnelian")
elif month == "september" and day <= 22:
    print("Virgo: Carnelian")
elif month == "september" and day >= 23:
    print("Libra: Peridot")
elif month == "october" and day <= 23:
    print("Libra: Peridot")
elif month == "october" and day >= 24:
    print("Scorpio: Emerald")
elif month == "november" and day <= 21:
    print("Scorpio: Emerald")
elif month == "november" and day >=22:
    print("Sagittarius: Topaz")
elif month == "december" and day <= 21:
    print("Sagittarius: Topaz")
else:
    print("Have a Nice Day!") 
print("Have a Nice Day!")