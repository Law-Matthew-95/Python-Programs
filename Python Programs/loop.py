def delete_starting_evens(lst):
 
  for number in lst:
   
      if len(lst) > 0 and number % 2 == 0:
        lst = lst[1:]
        continue 
      return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
