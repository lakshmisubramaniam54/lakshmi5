input=raw_input().lower()
words=input.split(' ')
capitalized= []
for woed in words:
  final_words=word(0).upper() + word[1:]
  capitalized.append(final_words)
output = ' '.join(capitalized) 
print output
