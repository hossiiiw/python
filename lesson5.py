import random

def game ():
  game_count = 0
  player_win = 0
  computer_win = 0


  def play_game():

    user_input = input("\nPlease selecet your operator 1.Rock 2.Papper 3.Scissor : ").strip()

    if user_input.lower() == "quit" : 
      return

    if user_input not in ["1" , "2" , "3"] :
      print("You must enter 1 , 2 , 3")
      return play_game()


    user_choice = int(user_input)
    computer_value = random.choice("123")
    computer_choice = int(computer_value)


    def decide_winner (user , computer):
      nonlocal player_win
      nonlocal computer_win
      print(f"Your choice is {user} \nComputer choice is {computer} ")

      if user == 1 and computer == 3:
        player_win +=1
        return "Player win"
      elif user == 2 and computer == 1:
        player_win += 1
        return "Player win"
      elif user == 3 and computer == 2:
        player_win +=1
        return("Player win")
      elif user == computer :
        return "Game tie"
      else :
        computer_win += 1
        return "Computer win"

    game_result = decide_winner(user_choice , computer_choice)      
    print(game_result)

    nonlocal game_count
    game_count += 1

    print(f"Game count is : {game_count}")
    print(f"Player win {player_win} times")
    print(f"Computer win {computer_win} times")
    return play_game()

  return play_game


play = game()

play()

