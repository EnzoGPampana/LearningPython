# Directions Reduction
# In a wild western journey, a man got directions like "NORTH," "SOUTH," "WEST," and "EAST." 
# Going opposite right away is wasteful due to harsh conditions. 
# Help him simplify by removing consecutive opposite directions like "NORTH"-"SOUTH" or "WEST"-"EAST." 
# Write a function called dirReduc that takes a direction array and returns a simplified one, removing needless steps.

arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

def dirReduc(arr):
    opposite_pairs = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    new_dir = []

    for i in arr:
        if new_dir and new_dir[-1] in opposite_pairs[i]:
            new_dir.pop()
        else:    
            new_dir.append(i)
    return new_dir

print(dirReduc(arr))