
for x in range(1, 6):
    for y in range(1, 6):
        print ('%d * %d = %d' % (x, y, x*y))
    print ("")


What you're looking at is simply one of pythons formatting techniques.
So the % sign is used to seperate the formatting string and also to denote what to use the next token for.
('%d * %d = %d'     %      (x, y, x*y))
"%d" means that its expecting a float or integer parameter. First off, that will be the first x.
The next * is just printing out a star. Same for the = sign.
So that will evaluate to:
print(x + " * " + y + " = " + (x * y))