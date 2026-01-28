#this program prompts the user for their name and then greets them
Name = input("what's your name? ")
clean = " ".join(Name.split())
print(f"hello, {clean}")