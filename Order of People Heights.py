def findOrder(height, infront):
    # Pair up height and infront
    people = list(zip(height, infront))
    # Sort people by descending height and then by ascending infront
    people.sort(key=lambda x: (-x[0], x[1]))
    
    result = []
    for h, inf in people:
        result.insert(inf, h)
    
    return result
