numbers = [2,15,0,-3]

def insertion_sort(arr):

  for iterater in range(len(arr)):

    #the variable cursor is assigned the value of the iterater for each int in numbers
    cursor = (arr[iterater])

    #the variable position is assigned the index of each num in numbers list 
    position = iterater

    while position > 0 and arr[position-1] > cursor:
      #swapping the number down the list 
      arr[position] = arr[position-1]
      position = position -1

      #when the loops breaks, we assign the iterator of arr to the cursor     
    arr[position] = cursor

  return arr

print(insertion_sort([-2, 100, 10, 5, 8]))