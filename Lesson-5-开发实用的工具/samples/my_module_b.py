# coding=utf8
# Copyright (c) 2017 CineUse

import my_module_a as a

print a.x
print a.y

a.foo()

print __name__

if a.__name__ == "__main__":
    print "yes, __name__ is '__main__'"
else:
    print "no, __name__ is not '__main__', now it's: %s " % a.__name__
