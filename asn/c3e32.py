#Walter Sellars
#02-05-2019
#c3e32.py


silly = 'newly formed bland ideas are inexpressible in an infuriating way'
# a
bland = silly.split()
print (str(bland))

# b
b = ''.join([w[1] for w in bland])
print (b)

#c
c = ' '.join(bland)
print (c)
#d

print (str([w for w in sorted(bland)]))
