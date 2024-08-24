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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n "))

rps_list = [[rock, paper, scissors],[rock, paper, scissors]]

num_random = random.randint(0, 2)
bot_display = rps_list[0][num_random]

player_display = rps_list[1][choose]

print(f"You: \n{player_display}")
print(f"Bot: \n{bot_display}")

if rps_list[0][num_random] == rps_list[1][choose]:
    print("It's a draw")
elif rps_list[0][num_random] != rps_list[1][choose]:
    if rps_list[0][num_random] == rps_list[1][choose - 1]:
        print("You win")
    if rps_list[0][num_random - 1] == rps_list[1][choose]:
        print("You lose")
