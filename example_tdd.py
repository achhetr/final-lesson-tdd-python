class ScaryMath:
  def __init__(self, x):
    self.x = x

  def double(self):
    return (self.x * 2)

m = ScaryMath(10)
m.double()

print(m.x)

def scary_math_double():
  m = ScaryMath(10)
  m.double()
  assert m.double() == 20

# load_file
# function does but does not something load_file
# - it changes the attribute -> change of attribute
# - it calls api -> load_file -> assert load_file
# unit test

def quick_print(window, x, y, text):
    ''' Clears screen and types supplied text'''
    window.erase()
    window.addstr(
        y, x, text)
    window.refresh()

# cli based function
# does not throw an error -> good enough check
# or you can ignore it
# assert window.display_current_string == NoneType
