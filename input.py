import subprocess
import os

array = ["./input"] + ["A"] * 99

array[ord('A')] = "\x00"
array[ord('B')] = "\x20\x0a\x0d"
array[ord('C')] = "1"

my_env = "\xde\xad\xbe\xef"
env = os.environ.copy()
env["\xde\xad\xbe\xef"] = "\xca\xfe\xba\xbe"

f = open("\x0a", "wb")
f.write("\x00\x00\x00\x00")
f.close()
proc = subprocess.Popen(array, stdin=PIPE, stdout=PIPE, env=my_env)

proc.stdin.write("\x00\x0a\x00\xff")
proc.stderr.write("\x00\x0a\x02\xff")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))
s.send("\xde\xad\xbe\xef")
s.close()