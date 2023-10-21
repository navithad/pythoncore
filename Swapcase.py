#This function convert the case of letters in a given alphanumeric input string.  
# Eg:
#input:kj2HiL76jkg
#output:KJ2hIl76JKG
def swap_case(str):
  list1=[]
  for i in str:
    if(i.isupper()==True):
      list1.append(i.lower())
    else:
      list1.append(i.upper())
  return "".join(list1)
s=input("Enter a string: ")    
result=swap_case(s)
print("Swaped string: ",result)
