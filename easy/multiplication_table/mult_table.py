
for i in xrange(1, 13):
    row = [x * i for x in xrange(1, 13)]
    for num in row:
        print '{' ': >3}'.format(num),
    print '\r'
