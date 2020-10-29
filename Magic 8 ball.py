from random import choice

ans = ["Cannot predict now", "Don't count on it", "It is certain", "Most likely", "My reply is no", "Outlook not so good", "Reply hazy,try again", "Very doubtful"]

def answerquestion():
    question = input("Ask the 8 ball a question: ")
    print("In progress")
    print(choice(ans))
answerquestion()

x = input("Do you have another question?[Y/N]: ")
while x.lower() == "y":
    answerquestion()
    x = input("Do you have another question?[Y/N]: ")
else:
    print("Thank you for playing!")



