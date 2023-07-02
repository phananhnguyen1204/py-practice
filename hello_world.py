# def divide(a,b):
#   return a/b

# try:
#   ans=divide(40,0)
# except ZeroDivisionError as e:
#   print(e, "we cannot divide by zero")
# except Exception as e: 
#   print("Something went wrong!",e)
#   print(e.__class__)
  
# The variable called file will get access to the contents of test.txt
# with open('text.txt',mode='r') as file:
  
#   data=file.readline()
#   print(data)

# file.close()

# with open("newfile.txt",'w') as file:
#   file.write("This is a new file created")


# with open('newfile.txt', 'r') as file:
#   print(file.read().split('\n'))

trial="abcd"
print(trial)
print(trial[::-1])

def string_reverse(str):
  if len(str)==0:
    return str
  return  string_reverse(str[1:]) +str[0]
print(string_reverse(trial))

a=[[96],[69]]
print("".join(list(map(str,a))))