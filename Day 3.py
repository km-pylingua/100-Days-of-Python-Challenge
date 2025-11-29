print('''
                    __
`       `          .^o ~\  `        `   `                `
         ``  `    Y /'~) }      _____          `        `` `
          `       l/  / /    ,-~     ~~--.,_    `         `    ``
     `           `   ( (    /  ~-._         ^.
     ``      `        \ "--'--.    "-._       \       `    `
       `           `   "-.________     ~--.,__ ^.             `
               `    `            \"~r-.,___.-'-. ^.
      `    `                 `    YI    \\      ~-.\     `      `
            `             `       ||     \\        `\
        `                  `      ||     //
  `           `                   ||    //
   `           `          `       ()   //
                `          `      ||  //     `   `
           `                      || ( c      `
            `        ___._ __  ___I|__`--__._ __  _
                   "~     ~  "~  ""   ~~"    ~  ~~
''')

print("Welcome to Python Island. Your mission is to find the rare new breed of flamingo.")

choice_1 = input("Your ship is stranded on the shore of the river. You gather your backpack and head towards the head of the woods. Upon entering the woods you hear a nosie to your right. Which way do you go: right or left? ")
if choice_1 == "right":
    print("Game over.")
elif choice_1 == "left":
    choice_2 = input("You push past the brush, through the bushes and fall into a swamp. Do you try to swim to the other side or wait to find a branch to pull yourself out? ")
    if choice_2 == "swim":
        print("Game over.")
    elif choice_2 == "wait":
        choice_3 = input("You find a branch and pull yourself out. You wonder around the swamp and find several cabins with different colored doors. Do you go through the blue, red, or yellow door? ")
        if choice_3 == "red":
            print("Game over.")
        elif choice_3 == "blue":
            print("Game over.")
        elif choice_3 == "yellow":
            print("You win! You found the rare Python Island flamingo in the cabin with the yellow door!")