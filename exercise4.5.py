my_foods = ['pizza', 'falafel' , 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\n")
for myFood in my_foods:
    print(myFood)

print("\n")
for friendFood in friend_foods:
    print(friendFood)
