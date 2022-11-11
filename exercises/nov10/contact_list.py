#author yaz c

#from filename import className

from  person   import Person
# friend = Person("Tttt","iii","324-434-4234")
# friend_2 = Person("freaf","freaf","320-230-2934")

# friend.display()
# friend_2.display()
def display_people(people):
    for friend in people:
        friend.display()
people = []
people.append(Person("sre","vsrgtf","930-329-3294"))
people.append (Person("freaf","freaf","320-230-2934"))

display_people(people)

first = input("enter first: ").strip()
last = input("enter last: ").strip()

#loop and find match

for person in people:
    if person.first.lower() == first.lower():
        print(person.get_phone())
