import os

fp = os.popen('dir')

res = fp.read()

print(res)