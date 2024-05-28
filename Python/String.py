str = "samurai@gmail.com"
str1 = "@7"
str2 = "subbaram"
str3 = "         great  i      "
print(str[1])
print(str[0:7])  # It is sub string in python
print((str + str1))  # Concatenate
print(str2 in str)  # Sub string check
print(str.split("."))  # split the string wherever "."
var = str.split(".")
print(var[0])
print(var[1])
print(str3)
print(str3.strip(" "))  # Strip the spaces form the string
print(str3.lstrip(" "))  # Strip the spaces form the left side of the string
print(str3.rstrip(" "))  # # Strip the spaces form the right side of the string
