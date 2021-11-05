"""
Question Bank is my personal program which i had created to save my data and time, by not searching 
one question again & again. I'll write different questions and answer them when i find perfect 
answer to write, also I'll catagorize questions in [answered] & [unanswered] form. Also i'll 
create two different files for acessing questions and answers.
"""

# TODO: Correct the displayCatagory() function

class QuestionBank:

    @staticmethod
    def addQuestions():
        newQuestion = input("\n\t\t\tEnter your Question here: \n\n\t")
        catagory = input("\t\t\t\tCatagory: ")
        # catagory = "GitHub"

        f = open("questions.txt", "a")
        f.write(newQuestion)
        f.write("?\n")
        f.close()
        f = open("catagory.txt", "a")
        f.write(catagory)
        f.write(".\n")
        f.close()

    @staticmethod
    def addAnswers():
        newAnswer = input("\n\t\t\tEnter your Answer here: \n\n\t")

        f = open("answers.txt", "a")
        f.write(newAnswer)
        f.write(".\n")
        f.close()

    @staticmethod
    def display():
        f = open("questions.txt", "r")
        allQuestions = f.read()
        myQuestions = allQuestions.split("?\n")
        f.close()
        f = open("answers.txt", "r")
        allAnswers = f.read()
        myAnswers = allAnswers.split(".\n")
        f.close()

        for index, value in enumerate(myQuestions):
            if index+2 > len(myQuestions):
                break;
            else:
                print(f"  {index+1}. ", end="")
                question = value.split(" ")
                for iindex, vaalue in enumerate(question):
                    if iindex%8==0:
                        print("\n\t", end="")
                    print(f"{vaalue} ", end="")
                print("?\n  Ans-", end="")

                answer = myAnswers[index].split(" ")
                for aiindex, avaalue in enumerate(answer):
                    if aiindex%8==0:
                        print("\n\t", end="")
                    print(f"{avaalue} ", end="")
                print(".\n\n", end="")

    @staticmethod
    def search():
        questions = input("\n\t\t\tEnter your Question below for search\n\n\t\t\t")
        f = open("questions.txt", "r")
        allQuestions = f.read()
        myQuestions = allQuestions.split("?\n")
        f.close()
        f = open("answers.txt", "r")
        allAnswers = f.read()
        myAnswers = allAnswers.split(".\n")
        f.close()
        
        status = "Sorry, Question Doesn't exists!"
        for index, value in enumerate(myQuestions):
            if questions.lower() == value.lower():
                status = "found!"

                question = value.split(" ")
                print("  Ques.", end="")
                for iindex, vaalue in enumerate(question):
                    if iindex%8==0:
                        print("\n\t", end="")
                    print(f"{vaalue} ", end="")
                    if iindex+1==len(question):
                        answer = myAnswers[index].split(" ")
                        print("?\n  Ans-", end="")
                        for aiindex, avaalue in enumerate(answer):
                            if aiindex%8==0:
                                print("\n\t", end="")
                            print(f"{avaalue} ", end="")
                        print(".\n\n", end="")
        if status != "found!":
            print(status)
    
    @staticmethod
    def displayCatagory():
        catagory = input("\n\t\t\tEnter your Catagory below for search\n\n\t\t\t")
        f = open("questions.txt", "r")
        allQuestions = f.read()
        myQuestions = allQuestions.split("?\n")
        f.close()
        f = open("catagory.txt", "r")
        allCatagory = f.read()
        myCatagory = allCatagory.split("?\n")
        f.close()
        f = open("answers.txt", "r")
        allAnswers = f.read()
        myAnswers = allAnswers.split(".\n")
        f.close()
        
        status = "Sorry, Catagory Doesn't exists!"
        sno = 1
        for index, value in enumerate(myCatagory):
            if value.lower() == catagory.lower():
                status = "found!"

                print(f"  {sno}. ", end="")
                question = myQuestions[index].split(" ")
                for iindex, vaalue in enumerate(question):
                    if iindex%8==0:
                        print("\n\t", end="")
                    print(f"{vaalue} ", end="")
                print("?\n  Ans-", end="")

                answer = myAnswers[index].split(" ")
                for aiindex, avaalue in enumerate(answer):
                    if aiindex%8==0:
                        print("\n\t", end="")
                    print(f"{avaalue} ", end="")
                print(".\n\n", end="")
            sno+=1

        if status != "found!":
            print(status)


    @staticmethod
    def main():
        # Creating a file to store all my quotes.
        try:
            open("questions.txt", "+x")
            open("answers.txt", "+x")
            open("catagory.txt", "+x")
        except:
            pass
        
        source = QuestionBank()
        while True:
            print("\n\n\t\t\tQUESTION BANK\n\n\t\t\t1. Add QnA\n\t\t\t2. Search\n\t\t\t3. Display All\n\t\t\t4. Display Catagory\n")
            option = input("\t\t\tChoose one from Above: ")
            if option == "1":
                source.addQuestions() # For adding new questions to the list
                source.addAnswers() # For adding new answers to the list
            elif option == "2":
                source.search() # To search for existing question & answer
            elif option == "3":
                source.display() # To display all question and answer together
            elif option == "4":
                source.displayCatagory() # To display all question and answer within the catagory
            elif option == "exit":
                print("\n\n\t\t--------Thank you for using our Application!--------\n\t\t\t\tSee You Again ;)\n\n")
                break
            else:
                print("\n\t\t--------Wrong Input, Please Input Again!--------")

QuestionBank.main()