<<<<<<< HEAD
import random
import itertools

elements = [1, 2, 3, 4, 5]

random.shuffle(elements)

cycle_iterator = itertools.cycle(elements)

for _ in range(15):
=======
import random
import itertools

elements = [1, 2, 3, 4, 5]

random.shuffle(elements)

cycle_iterator = itertools.cycle(elements)

for _ in range(15):
>>>>>>> 4c9823e48e9de3acee01fde2d9c90d22d4d47041
    print(next(cycle_iterator))