import random

class Password:

  ''' Class constructor '''
  def __init__(self,size, letters, numbers, others):

    self.size = size
    self.letters = letters
    self.numbers = numbers
    self.others = others

  ''' Returns a random char '''
  def select_char(self):
    if(not self.letters):
      return

    is_caps = random.randint(0,1)

    if(is_caps):
      return chr(random.randint(65,90))
    else:
      return chr(random.randint(97,122))

  ''' Return a random number converted to char '''
  def select_num(self):
    if(not self.numbers):
      return

    return chr(random.randint(48,57))

  ''' Return an alternate caracter '''
  def select_others(self):
    if(not self.others):
      return

    return random.choice('@#!&.')
