import random

class Password:

  ''' Class constructor '''
  def __init__(self,size, chars, numbers, others):

    self.size = size
    self.chars = chars
    self.numbers = numbers
    self.others = others

  ''' Returns a random char '''
  def select_char(self):
    if(not self.chars):
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

  ''' Return an alternate character '''
  def select_others(self):
    if(not self.others):
      return

    return random.choice('@#!&.')

  ''' Chooses type of next character and returns it '''
  def select_next(self):
    opt = random.randint(0,3)

    if opt == 3:
      return self.select_others()
    elif opt == 2:
      return self.select_num()
    else:
      return self.select_char()

  ''' Create password given the parameters '''
  def get_pass(self):
    psw_ = [];

    for i in range(self.size):
      psw_.append(self.select_next())

    return ''.join(psw_)
