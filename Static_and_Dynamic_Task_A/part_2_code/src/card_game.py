### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

  def __init__(self, card):
    self.card = card


  def check_for_ace(self, card):
    if card in self.symbol >= 1:
      return True
    else:
      return False

  def highest_card(self, card):
    return card.symbol == "ace"
  

  def cards_total(self, card):
    total = 0
    for card in self.card:
      total += (card.value)
    return "You have a total of" + total