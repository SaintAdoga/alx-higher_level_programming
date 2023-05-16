#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Stephen", "Lydia")
say_my_name("Faith", "Saint")
say_my_name("Yes Daddy")
try:
    say_my_name(12, "Saint")
except Exception as e:
    print(e)
