#author-yaz c

def get_mood(color):
    mood_chart = {
        "red":"angry",
        "blue":"sad",
        "purple":"complicated",
        "yellow":"happy",
        "green":"sickly",
        "orange":"annoyed",
        "violet":"inspired",
    }
    color = color.lower().strip()

    if color not in mood_chart:
        return "Not Feeling Right Now"
    else:
        return mood_chart[color]


print("Lets find your Mood")

moody = input("Enter Color: ").lower().strip()
moods = get_mood(moody)


print (f"You are feeling {moods}")