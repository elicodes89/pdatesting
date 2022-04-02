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
    if card.value = 1:
      return True
    else #:
      return False
   

  dif highest_card(self, card1 card2): #spelling mistake on "dif" this would stop the test from running
  if card1.value > card2.value:
    return card
  else:
    return card2
  


def cards_total(self, cards):
  total #there is no operator. there is no value assigment and the function does not know what total actually is
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
