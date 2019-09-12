#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  batch = 0
  count = 0
  
  for name,meas in recipe.items():
    if(name in ingredients.keys()):
      if(recipe[name] <= ingredients[name]):
        temp = ingredients[name]//recipe[name]
        if(count == 0):
          batch = temp
          count = count+1
        else:
          if(temp < batch):
            batch = temp
    else:
      batch=0
      break
    
  print(batch)
  return batch       

recipe = { 'milk': 2 }
ingredients = { 'milk': 200}
print(recipe_batches(recipe,ingredients))


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))