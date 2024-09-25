#!/usr/bin/env python3

# Author: Grishma Gairhe
# Author ID: ggairhe
# Date Created: 2024/09/24

import sys

timer = 3

if len(sys.argv) > 1:
    timer = int(sys.argv[1])  

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

