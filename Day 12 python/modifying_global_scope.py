enemies = 1
# def increase_enemies():
#     global enemies
#     enemies +=1
#     print(f"enemies inside function: {enemies} ")
# increase_enemies()
# print(f"enemies outside the function : {enemies}")  
# 
# above code is valid but varibal declare global


def increase_enemies():
    print(f"enemies inside function: {enemies} ")
    return enemies +1
increase_enemies()
print(f"enemies outside the function : {enemies}") 

# modifying global scope