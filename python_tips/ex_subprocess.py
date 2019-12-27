import os
import subprocess

output = os.fsdecode(subprocess.check_output('ls'))
print (output)

output1 = subprocess.check_output('dir', shell=True, encoding='cp437')
print (output1)

from subprocess import Popen, PIPE
text = Popen(['ls', '-lat'], stdout=PIPE, encoding='utf-8').communicate()[0]
type(text)
#str
print(text)
