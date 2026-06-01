import random 


lst = ["pan","can","fan","ran","pat","fat","bat"]

count = 0

sample_lst = ["_","_","_"]

while True:
    if count >6:
        print("Game Over You Lose!!")
        break

    if "_" not in sample_lst:
        print("You guessed the correct word !😍")
        break

    print("Welcome to Hungman Game You have to guess the Word in 6 attemts")

    picked_word = random.choice(lst)

    user_input = input("Enter a character :")

    

    if user_input in picked_word:
        print("This character is in the word.")
        index = picked_word.index(user_input)
        sample_lst[index] = picked_word[index]
        for i in sample_lst:
            print(i,end=" ")
        print()
    else:
        print("This character is not in the word")
        for i in sample_lst:
            print(i,end=" ")
        print()

    count += 1