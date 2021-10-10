import random
import os


length = 32
dir_name = 'random_outputs'

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

random_seeds = random.sample(range(2 ** 32), 100)
for i in range(len(random_seeds)):
    state = random_seeds[i]

    with open(dir_name + '/' + str(i) + '.bnr', "wb") as f:
        for j in range(1024 ** 2):
            byte = 0b0
            for x in range(8):
                newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 22) ^ (state >> 32)) & 1
                byte = (byte << 1) | newbit
                state = (state >> 1) | (newbit << 31)
            f.write(byte.to_bytes(1, byteorder='big'))

