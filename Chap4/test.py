seq = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]

def merge(seq, start, mid, stop):
  lst = []
  i = start
  j = mid

  while i < mid and j < stop:
    if seq[i] < seq[j]:
      lst.append(seq[i])
      i+=1
    else:
      lst.append(seq[j])
      j+=1
  while i < mid:
    lst.append(seq[i])
    i+=1

  for i in range(len(lst)):
    seq[start+i] = lst[i]


def mergeSortRecursively(seq, start, stop):
  if start >= stop-1:
    return

  mid = (start + stop) // 2

  mergeSortRecursively(seq, start, mid)
  mergeSortRecursively(seq, mid, stop)
  merge(seq, start, mid, stop)

def mergeSort(seq):
  mergeSortRecursively(seq, 0, len(seq))

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

print(len(seq))
quickSort(seq,0,len(seq)-1)
print(seq)
