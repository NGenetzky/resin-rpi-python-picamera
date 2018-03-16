#!/usr/bin/env python

import time

time.sleep(2)

with open('/data/image.txt', 'w+') as f:
    t = 'TextCaptured'
    print(t)
    f.write(t)

time.sleep(10)
