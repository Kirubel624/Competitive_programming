#!/bin/python3

import math
import os
import random
import re
import sys

def check_weirdness(n):
    if n % 2 == 1 or (n % 2 == 0 and n in range(6, 21)):
        return "Weird"
    else:
        return "Not Weird"
        
if __name__ == '__main__':
    n = int(input().strip())
    result = check_weirdness(n)
    print(result)
