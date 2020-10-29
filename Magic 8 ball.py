from random import choice

question = input("Ask the 8 ball a question: ")

ans = ["Cannot predict now", "Don't count on it", "It is certain", "Most likely", "My reply is no", "Outlook not so good", "Reply hazy,try again", "Very doubtful"]

ball = True

while ball:
    print(choice(ans))
    x = input("Do you have another question?[Y/N]: ")
    if x.lower() == "y":
        question = input("Ask the 8 ball a question: ")
    elif x.lower() == "n":
        print("Thank you for playing!")
        break



