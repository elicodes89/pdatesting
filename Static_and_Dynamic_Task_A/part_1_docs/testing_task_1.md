### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
#there is no constructor defined. Python needs a function with the __init__ constructor for the classes to be initialized by this method.

  def check_for_ace(self, card):
    #the function is expecting to return a True or False value. I need to amend the if statement in order to compare the actual symbol of the card with values within certain range, that in this case is anything equal or higher than 1.
    if card.value = 1:
      return True
    else #: missing colon
      return False
   

  dif highest_card(self, card1 card2): #spelling mistake on "dif" this would stop the test from running. Also, the function would need to take card and card1 as arguments.
  if card1.value > card2.value:
    return card1 #card1 is missing
  else:
    return card2
  


def cards_total(self, cards):#cardstotal should come from cardgame. As the cardgame is the object that holds a list of the complete set of cards.
  total #there is no operator. there is no value assigment and the function does not know what total actually is
  for card in cards:#again, for each card of the cardgame, not cards
    total += card.value
    return "You have a total of" + total #again, total would need an operator to make this return work and also delete the string.
  
```
