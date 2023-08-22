#!/usr/bin/env python3
class MyString:
  def __init__(self, value):
       self.value = value

  @property
  def value(self):
    return self._value

  @_value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      print(f"Setting value to '{new_value}'.")
      self._value = new_value
    else:
      print("Value must be a string.")    

  
  def is_sentence(self):
    return self._value.endswitch('.')
