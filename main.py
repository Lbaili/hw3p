# Author: Chang Li cxl5844@psu.edu
# Collaborator: Daniel Mikita djm6907@psu.edu 
# Collaborator: John O’Toole jbo5232@psu.edu 
# Section: 1
# Breakout: 8

def digit_sum(n):
  if  n <= 10 :
    return n
  else :
    return int(digit_sum(n/10)+n%10)
    

if __name__ =="__main__":
  a = int(input("Enter an int: "))
  print(f"sum of digits of {a} is {digit_sum(a)}.")