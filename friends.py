friends = []

for _ in range(3):
    friend = input("Enter name of your friend: ")
    friends.append(friend)

persons = []

people = open('people.txt', 'r')
people_content = people.readlines()
people.close()

for person in people_content:
    persons.append(person[0:-1])

nearby_friends = []

for friend in friends:
    if friend in persons:
        nearby_friends.append(friend)

nearby_friends_file = open('nearby_friends', 'w')
for nearby_friend in nearby_friends:
    nearby_friends_file.write(f'{nearby_friend}\n')

nearby_friends_file.close()
