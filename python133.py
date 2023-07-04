import string
str="this is a simple string"
print("Orignal string =>",str)
print("capitalize first character=>",str.capitalize())
print("string padded with * =>",str.center(40,'*'))
print("count is in string =>",str.count('is'))
print("Position of substring  =>",str.find('simple'))
print("Is string a title case =>",str.istitle())
print("Is string a uppercase case =>",str.isupper())
print("Is string a lowercase case =>",str.islower())
print("Replace 'sample' with 'good' =>",str.replace('simple','good'))
str2="another string example"
print("Orignal string 2=>",str2)
print("swapcase ",str2.swapcase())
print("lower case ",str2.lower())
seq=('hello','welcome','home')
seq='-'
print("Example of join",seq.join(seq))







