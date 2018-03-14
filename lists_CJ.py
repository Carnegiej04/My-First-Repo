name = "Carnegie"
subjects = ["Science","History","Math","English"]
print ("my name is " + name)

#print (subjects)

for i in subjects:
    print ("One of my classes is " + i)

players = ["Alvin Kamara", "Drew Brees", "Micheal Thomas", "Marshon Lattimore"]

for i in players:
    if i == "Alvin Kamara":
        print(i + " becuase he is one of the best players on our team")
    elif i == "Drew Brees":
        print(i + " Becuase he carries our team and is our franchise")
    elif i == "Marshon Lattimore":
        print(i + " Because he won DPOY and Locked up")
    else:
        print("one of my favorite players on the Saints is " + i)


players = []

while True:
    print("Who are your favorite players? Type'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        players.append(answer)

for i in players:
    print("One of your favorite players is " + i)
