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


  def check_for_ace(self, card):
    if card.value = 1: # double ='s needed
      return True 
    else # colon is needed here
      return False
   
# def has been misspelt
  dif highest_card(self, card1 card2): #comma needed between parameters
  if card1.value > card2.value: # if statement needs indented
    return card # card is not defined in this function. Should be card1
  else:
    return card2
  


def cards_total(self, cards): # function needs indented
  total # total has not been assigned a starting value
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # to add the total to a string the total needs converted to a string
    # return statement currently in the for loop. Needs moved left
  
```
