import random


def get_choices():
  player_choice = input("Entrez un choix (pierre, feuille, ciseaux) : ")
  options = ["pierre", "feuille", "ciseaux"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"Vous avez choisi {player}, l'ordinateur a choisi {computer}")
  if player == computer:
    return "Match nul!"
  elif player == "pierre":
    if computer == "ciseaux":
      return "La pierre écrase les ciseaux! Vous avez gagné !"
    else :
      return "La feuille recouvre la pierre! Vous avez perdu !"
  elif player == "feuille":
    if computer == "pierre":
      return "La feuille recouvre la pierre! Vous avez gagné !"
    else :
      return "Les ciseaux coupent la feuille! Vous avez perdu !"
  elif player == "ciseaux":
    if computer == "feuille":
      return "Les ciseaux coupent la feuille! Vous avez gagné !"
    else :
      return "La pierre écrase les ciseaux! Vous avez perdu !"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)