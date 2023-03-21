#!/usr/bin/env python
# coding: utf-8

# # Task 1. Game menu function

# In[11]:


import random

deck = []
player_hand = []
robot_hand = []
def game_menu():
    print("Welcome to the Card Game!")
    print("1. start game")
    print("2. pick a card")
    print("3. shuffle deck")
    print("4. show my cards")
    print("5. check win or lose")
    print("6. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        play_game()
    elif choice == "6":
        print("Thank you for playing!")
        exit()
    elif choice == "2":
        pick_card()
   
    elif choice == "3":
        shuffle_deck()
        exit()
    elif choice == "4":
        show_cards()
        exit()
    elif choice == "5":
        check_result()
        exit()
    else:
        print("Invalid input. Please try again.")
        game_menu()


# # Task 2. Create Deck function

# In[12]:


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + ' of ' + suit)


# # Task 3. Shuffle Deck function

# In[13]:


def shuffle_deck():
    suits = ["♥", "♦", "♣", "♠"]
    deck = []
    for suit in suits:
        for rank in range(2, 11):
            deck.append(f"{rank} of {suit}")
        deck.append(f"A of {suit}")
        deck.append(f"J of {suit}")
        deck.append(f"Q of {suit}")
        deck.append(f"K of {suit}")

    random.shuffle(deck)

    # ensure the required cards are always in their respective positions
    first_card_suit = suits[0]
    second_card_suit = suits[1]
    last_card_suit = suits[-1]

    for i, card in enumerate(deck):
        rank, suit = card.split(" of ")
        if rank == "A" and suit == first_card_suit:
            deck.pop(i)
            deck.insert(0, card)
        elif rank == "Q" and suit == second_card_suit:
            deck.pop(i)
            deck.insert(len(deck)//2, card)
        elif rank == "K" and suit == last_card_suit:
            deck.pop(i)
            deck.append(card)

    print("Shuffled deck:")
    print(deck)


# # Task 4. Pick Card function

# In[14]:


def pick_card():
    if len(deck) > 0:
        return deck.pop()
  
    else:
        print("No more cards in the deck.")
        return None


# # Task 5. Show Cards function
# 

# In[15]:


def show_cards():
    print("Your cards:")
    print(', '.join(player_hand))
    print("Robot's cards:")
    print(', '.join(robot_hand))


# # Task 6. Check Result function
# 

# In[16]:


def check_result():
    player_sum = 0
    for card in player_hand:
        rank = card.split()[0]
        if rank == 'Ace':
            player_sum += 11
        elif rank in ['Jack', 'Queen', 'King']:
            player_sum += 10
        else:
            player_sum += int(rank)
    robot_sum = 0
    for card in robot_hand:
        rank = card.split()[0]
        if rank == 'Ace':
            robot_sum += 11
        elif rank in ['Jack', 'Queen', 'King']:
            robot_sum += 10
        else:
            robot_sum += int(rank)
    if player_sum > 21:
        print("You busted. Robot wins.")
    elif robot_sum > 21:
        print("Robot busted. You win!")
    elif player_sum > robot_sum:
        print("You win!")
    elif robot_sum > player_sum:
        print("Robot wins.")
    else:
        print("It's a tie.")


# # Task 7. Play Game function

# In[17]:


def play_game():
    create_deck()
    shuffle_deck()
    player_hand.clear()
    robot_hand.clear()
    for i in range(2):
        player_hand.append(pick_card())
        robot_hand.append(pick_card())
    show_cards()
    while True:
        choice = input("Do you want to pick another card? (y/n): ")
        if choice.lower() == 'y':
            player_hand.append(pick_card())
            robot_hand.append(pick_card())
            show_cards()
            check_result()
            if len(deck) == 0:
                game_menu()
        elif choice.lower() == 'n':
            check_result()
            game_menu()
        else:
            print("Invalid input. Please try again.")


# In[ ]:


game_menu()


# In[ ]:





# In[ ]:




