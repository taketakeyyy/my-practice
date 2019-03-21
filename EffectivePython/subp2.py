# -*- coding: utf-8 -*-
import random
import time

if __name__ == "__main__":
    pre_num = random.randrange(start=1, stop=7, step=1)
    while True:
        time.sleep(0.5)
        num = random.randrange(start=1, stop=7, step=1)
        if num == pre_num:
            break
        pre_num = num
