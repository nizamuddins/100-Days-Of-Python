import random
words_list = ["rain","dancing","slaaping"]

randomWord = [];
word = random.choice(words_list)
for i in range(len(word)):
    randomWord += "_";

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
    
val = 0;

def func2():
    guess = input("Guess a letter?").lower();
    for index1 ,arr in enumerate(word):
        if word.count(guess) != 0:
            if guess == arr:
                randomWord[index1] = arr;
        else:
            global val;
            val += 1;
            break;
    if val == 1:
        print(stages[6]);
        print("You enter wrong word ,You loose one life!");            
    elif val == 2:
        print(stages[5]);
        print("You enter wrong word ,You loose one life!");            
    elif val == 3:
        print(stages[4]);
        print("You enter wrong word ,You loose one life!");            
    elif val == 4:
        print(stages[3]);
        print("You enter wrong word ,You loose one life!");            
    elif val == 5:
        print(stages[2]);
        print("You enter wrong word ,You loose one life!");            
    elif val == 6:
        print(stages[1]);
        print("You enter wrong word ,You loose one life!");            
    elif val == 7:
        print(stages[0]);
        print("You Loss the Game!")
        return;                     
    

    if randomWord.count("_") != 0:
        joining = "".join(randomWord);
        print(joining);
        func2()        

func2();

random = "".join(randomWord);
print(random)
 
if randomWord.count("_") == 0:
    print("Won");
