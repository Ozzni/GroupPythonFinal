#Into. to Programming: Python - Final Project code
#Avery, Leila, Josiah
#Quiz Program

#Initialize variables
Score = 0
totalQuestions = 5
Answer = ""
Q = 0
QuestionList = ["Q1", "Q2", "Q3", "Q4", "Q5"]
QuestionAnswer = ["A", "B", "C", "D", "A"]
Name = input("What is your name? ")

#Assignment of actual contents to each question
QuestionList["Q1"] = "Question One"
QuestionList["Q2"] = "Question Two"
QuestionList["Q3"] = "Question Three"
QuestionList["Q4"] = "Question Four"
QuestionList["Q5"] = "Question Five"

#Introduces the quiz
print("[Topic] Quiz - 5 questions")
print()

#question loop
while Q < totalQuestions:
   
    #prints the current question from list, gets answer
    print(QuestionList[Q])
    Answer = input("A, B, C, or D? ")
    
    #validating input
    while Answer != "A" and "B" and "C" and "D":    #TODO: this currently does not work properly. Make this pass by if ANY of A B C or D are the given answer.
        Answer = input("Invalid answer. Please type A, B, C, or D ")
    
    #check if answer is correct and assign points accordingly
    if Answer == QuestionAnswer[Q]:
        print("Correct answer! ")
        Score = Score + 1
    else:
        print("Incorrect answer. ")
    
    #Iterate on the loop
    Q = Q + 1


#print final results
print("Hello, ", Name, "your score is: ", Score, "/", totalQuestions, "!")