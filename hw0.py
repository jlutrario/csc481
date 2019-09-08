"""
hw0.py
"""
# Function declarations
def my_rotate(the_list):
 """Takes a list, pops off the first element and adds it to the end of the list,
 returning the resulting list."""
 temp = the_list[0]
 new_list = the_list[1:len(the_list)+1]
 new_list.append(temp)
 return new_list
def my_rotate_n(n, the_list):
 """Takes a number n and a list and performs the my_rotate function n times."""
 count = 0
 temp = the_list[0]
 new_list = the_list
 while count < n:
     new_list = new_list[1:len(new_list)+1]
     new_list.append(temp)
     count = count + 1
     temp = new_list[0]
 return new_list
def first_sat(first_list, second_list, foo):
 """Takes two lists and a function foo as arguments.
 Function foo should take two arguments and return a boolean.
 The result of a call to first_sat should be a list containing the first pair of
arguments
 that satisfies (returns True) from foo."""
 x = 0
 while x < len(first_list):
     if foo(first_list[x],second_list[x]):
         pair = [first_list[x],second_list[x]]
         return pair
     x = x + 1
 return 'No match'
fin_list = []
def my_remove(the_char, the_list):
 """Takes a character and a list as input and returns a list with all instances
 of the character removed (including recursive instances)."""
 tmp_list = []
 for i in the_list:
   if (isinstance(i,list)):
     my_remove(the_char,i)
   elif (i != the_char):
     tmp_list.append(i)
 fin_list.append(tmp_list)
 return fin_list
def palindromep(the_list):
 """Takes a list as input and returns True if the list is a palindrome and False
otherwise."""
 length = len(the_list)
 x = length - 1
 new_list = []
 while (x >= 0):
   new_list.append(the_list[x])
   x = x - 1
 if the_list == new_list:
   return True
 else:
   return False
def main():
 """Calling the functions."""
 print(my_rotate(['a', 'b', 'c', 'd']))
 print(my_rotate_n(3, ['a', 'b', 'c', 'd']))
 print(first_sat([1, 4, 1, 4], [2, 5, 3, 5], (lambda x, y: x > y)))
 print(my_remove('b', [['a', 'b'], 'b', ['c','b','d','e','a'], ['b'], ['a'], 'c']))
 print(palindromep(['a',['b']]))
if __name__ == '__main__':
 main()
