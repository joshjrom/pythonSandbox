#t = t.sort()


count = [2, 4, "still", "how"]

def add_all(t):
    total = 0
    for x in t:
        total += 1
    return total


holderdic = {
        "something": {
            "name": "Joshua Ayegba",
            "complexion": "Dark Skinned",
            "height": 6,
        
        },
        "something_else": ["Jesse", 1, 2, 3],
    }


context = [
            "house",
            "food",
            {
                "name": "Jesse",
                "car": ["benz", "mercedes"]
            }
    ]

for x in context:
    print(x)
