import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock,paper,scissor];

input = int(input('Enter a Number?0 for rock.1 for paper,2 for scissor!'));

if input == 0:
    print(rock);
elif input == 1:
    print(paper);
else:
    print(scissor)

print('Computer choose');

num = random.randint(0,len(list)-1);

# num = random.choice(list)

print(list[num]);

if input == num:
    print('Draw');
elif input < num:
    print('You Wins!');
else:
    print('Computer Wins')          

