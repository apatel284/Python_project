questions=["Who was women prime minister of India" ,
   " what is the capital of India",
   " What is the capital of Canada",
    "Who went to moon first"]




option=[["A. smriti irani","B. Pratibha Gandhi","C. Pratibha Patil","D. Pratibha Gandhi"],["A. Delhi","B. Mumbai","C. Kolkata","D. Chennai"],["A. Toronto","B. Vancouver","C. Montreal","D. Ottawa"],
["A. Rohini","B. Mark Aldrin","C. Buz Aldrin","D. Nil Armstrong"]]



def functionOfask():
 i=0
 money=0
 for question in questions:
    print(question)
    print(option[i])
    
    
    userInput=input("Enter you anwer in A,B,C,D: ")
    if userInput=="C" and question==questions[i]:
      money=money+1000
      print("You won ", money)
        
    elif userInput=="A" and question==questions[i]:
      money=money+1000
      print("You won ", money)

    elif userInput=="D" and question==questions[i]:
      money=money+1000
      print("You won ", money)

    elif userInput=="D" and question==questions[i]:
      money=money+1000
      print("You won ", money)

    else:
      print("You loss")
      
    i=i+1


  
  
   
functionOfask()
   



 
