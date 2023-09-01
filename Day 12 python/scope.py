#scope
# enemies = 1
# def increase_enemies():
#     enemies =2
#     print(enemies)
# increase_enemies()
# print(enemies)

# local scope

# def fun():
#     y=2
#     print(y)
# fun()
# print(y)


#global scope

player_health=10
def drink_potion():
    potion_strength=2
    print(player_health)
drink_potion()