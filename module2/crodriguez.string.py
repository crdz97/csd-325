
fullname =input("Enter your first, middle, and last name")

nameparts = fullname.split()

firsti = nameparts[0][0].upper()
middlei = nameparts[1][0].upper()
lasti = nameparts[2][0].upper()
print(f"{firsti}.{middlei}.{lasti}.")

