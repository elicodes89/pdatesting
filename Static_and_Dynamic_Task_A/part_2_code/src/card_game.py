### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

  def __init__(self, total):
    # self.card = card
    self.total = total
    self.cards = []
  # def setUp(self):
  #   self.card = Card("hearts" , 14, "ace")


  def check_for_ace(self, card):
    if card in self.symbol >= 1:
      return True
    else:
      return False

  def highest_card(self, card):
    return card.symbol == "ace"
  

  def cards_total(cardgame):
    total = 0
    for card in cardgame.cards:
      total += (card.value)
    return total    