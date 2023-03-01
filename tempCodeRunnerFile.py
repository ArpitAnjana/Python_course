():
    fruit=['🍒','🍓','🍇']
    for i in enumerate(fruit):
        print(f'fruit: {i}')

    for fruit in range(5):
        print(fruit)
        fruit.append('apple')

fruits()