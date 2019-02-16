ch=input()
vowels={"a","e","i","o","u","A","E","I","O","U"}
if any(char in vowels for char in ch):
      print("yes")
else:
      print("no")
