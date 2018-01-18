# coding=utf8

# 即时更新foo
import sys
if "my_pack.foo" in sys.modules.keys():
    sys.modules.pop("my_pack.foo")

from foo import foo


def hey():
    print "Hello~"
