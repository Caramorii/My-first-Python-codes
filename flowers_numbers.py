def flowers_numbers():
    dict_flower = {}
    with open("flowers.txt") as flower:
        for linha in flower:
            partes = linha.split(":")
            part1 = partes[0].strip()
            part2 = partes[1].strip()
            dict_flower[part1] = part2
    return dict_flower

def user_flower():
    flower_d = flowers_numbers()
    flower_s = input("Enter your First [space] Last name only: ")
    first_le = flower_s[0].upper()
    if first_le in flower_d:
        c_flower = flower_d[first_le]
        print("Unique flower name with the first letter: ", c_flower)
    else:
        print("Don`t exist this letter in name flowers")
        
user_flower()    
    