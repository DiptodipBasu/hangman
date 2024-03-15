import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word=[
    "elephant",
    "giraffe",
    "lion",
    "tiger",
    "zebra",
    "cheetah",
    "leopard",
    "gorilla",
    "chimpanzee",
    "hippopotamus",
    "rhinoceros",
    "kangaroo",
    "koala",
    "panda",
    "sloth",
    "penguin",
    "eagle",
    "dolphin",
    "shark",
    "whale"
]
lives=6
x=random.randint(0,2)
lst=[]
chosen=word[x]
print("Guess the animal")
for i in range(len(chosen)):
    lst+="_"
print(f"{' '.join(lst)}")   
end=False
while not end:
    s=input("Enter your letter : ")
    for i in range(len(chosen)):
        letter=chosen[i]
        if letter==s:
            lst[i]=letter
    print(f"{' '.join(lst)}")   
    if s not in lst:
        lives-=1
        print("You guessed the wrong letter...You have ",lives," left")
        if lives==0:
            end=True
            print("You lose")
            print("You kiled the hangman")
    if "_" not in lst:
        end=True
        print("You Win")     
    print(stages[lives])    
