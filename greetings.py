#!/usr/bin/env python3
import random

def greeting():
  name = input("Hello!, What's your name?")
  number = random.randint(1,101)
  return "Hello {}, your random number is {}".format(name, str(number))

greeting()
