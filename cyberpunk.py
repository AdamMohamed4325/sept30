print("Testing")
#Code should have 3 questions ascending in difficulty from order of 1-3
# Each right and wrong answer should have corresponding replies related to whether they were true or false
#questions should be easy to interpret whithout any tricks to give players a fair chance
# Dialog through the code should be fun and engaging
#MUHAHAHA traped in a CYBERLAB and he have to solve 3 problems to escape form it.
#So, the Lavel-1 Going to be a massage appears on the door and he have to input a decrypted massage to unlock the lavel 1 and the answer is wired fishes
#If he fail on this lavel he dei. On the other hand if he would able to pass the game going to hin in the next lavel.
#Now the Lavel-2, he need to write the digit that is even and prime at the same time, the answe going to be 2. I he can answer hw will go to the next lavel otherwise dei.
#Lets talk about lavel-3, its  riddle "I have keys but no locks. I have space but no room. You can enter, but you cannot go outside. What am I?"
#The amswer is keyboard. I he can answer it he will win the game and escape from the Cyberlab otherwise will stack there and wil done forever.


print (" CYBER PUNK ESCAPE ROOM ")
print ("MUHAHAHA YOU ARE TRAPPED IN MY CYBERLAB")
print ("you have to solve 3 problems!")
print ("LEVEL 1: encrypted message")
print("A message appears on the door!")
print ("ZHLUG ILVKHV")
print ("hint: the message uses ceasar cipher with the key:3")
message = input("Enter decrypted message: ")
if message =="weird fishes":
   print("CORRECT PASSWORD! YOU ARE VERY LUCKY YOUNG ONE!!!")
   print("LEVEL 2: math problem! ")
   print("What is the digit that is even and prime at the same time? ")
   digit = int(input("type the digit!: "))
   if digit == 2:
       print("HOW DID YOU KNOW THAT! YOU WONT GET THE NEXT ONE CORRECT")
       print("LEVEL 3:a silly riddle!!")
       print("I have keys but no locks. I have space but no room. You can enter, but you cannot go outside. What am I? ")
       answer = input("Enter your answer: ")
       if answer == "keyboard":
           print("WHAT NOO YOU WERE NEVER SUPPOSED TO GET THAT RIGHT!! YOU ESCAPED THE ROOM")
       else: 
           print("ACCESS DENIED")
       
   else: 
       print("YOU HAVE DIED")
       
else:
    print("HAHAHA GAME OVER")
