import random

insults = ["You're Uglier than a Naked Mole Rat", "Your Mom Left You At Birth"]

def insultGen():
  print(random.choice(insults))
  return False
insultGen()
