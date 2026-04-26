# Problem 7: Search recipes by ingredient keyword
n = int(input())
recipes = input().split()
keyword = input().lower()
matches = [recipe for recipe in recipes if keyword in recipe.lower()]
if matches:
    print(' '.join(matches))
else:
    print("No recipes found")
print(len(matches))
if matches:
    smallest_recipe = min(matches)
    print(smallest_recipe)
else:
    print("-")