first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #f-strings=format strings
print(full_name)

print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}"
print(message)

#old way of using format below:
full_name = "{} {}".format(first_name, last_name)

#adding whitespace with tabs or newlines
#to add tab -> \t
print("Python")
print("\tPython")
#newline \n
print("Languages:\nPython\nC\nJavaScript")
#can also combine tab and newline
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#stripping whitespace at right end = rstrip()
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
#above is the same for left end except use lstrip()
#for both sides use strip()

