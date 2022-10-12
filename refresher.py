from random import randint
import time
import os

def refresher(seconds):
##    count = 0
    while True:
        mainDir = os.path.dirname(r'C:\Users\Lenovo\PycharmProjects\streamlit')
        filePath = os.path.join(mainDir, 'dummy.py')
        with open(filePath, 'w') as f:
            f.write(f'# {randint(0, 10000)}')
        time.sleep(seconds)
##        count+=1
##        print(count)
##        if count > 50:
##            return False
        
refresher(5)
