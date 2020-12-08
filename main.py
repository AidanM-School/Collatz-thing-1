def collatz_gen(n):
  collatz_collection={}
  collatz_collection[1]=[1]
  for i in range(2,n):
    next_list=[i]
    next_thing=collatz(i)
    while True:
      next_thing = collatz(next_thing)
      if next_thing == 1:
        next_list.append(1)
        collatz_collection[i]=next_list
        break
      elif next_thing in collatz_collection.keys():
        next_list.extend(collatz_collection[next_thing])
        collatz_collection[i]=next_list
        break
      else:
        next_list.append(next_thing)
    for j in collatz_collection[i]:
      if not j in collatz_collection:
        f=collatz_collection[i].index(j)
        collatz_collection[j]=collatz_collection[i][:f]
  return collatz_collection

def collatz(n):
  if n%2==0:
    return n//2
  else:
    return 3*n+1

def is_pow_2(n):
  if n == 2:
    return True
  elif n%2 ==1:
    return False
  else:
    return is_pow_2(n//2)

def main():
  g=10000
  l = collatz_gen(g)
  longest_path=[0,0]
  for i in range(2,g):
    if len(l[i]) > longest_path[1]:
      longest_path=[i,len(l[i])]
  print("the number with the most steps is {} and it takes {} steps.".format(longest_path[0],longest_path[1]))
  non_2_powers=[i for i in range(3,g)if not is_pow_2(i)]
  short=768
  shortid=5
  for i in non_2_powers:
    if len(l[i])<short:
      short=len(l[i])
      shortid=i
  print("The shortest collatz path that doesn't start with a power of 2 starts with {} and takes {} steps.".format(shortid,short))
  avg=len(l[2])
  for i in range(3,g):
    avg+=len(l[i])
  avg/=g-2
  print("The average length of all of the strings from 2 to 10000 is {}.".format(avg))
main()