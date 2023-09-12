sentence = "What is the Airspeed velocity of a unladen Swallon?"
x= sentence.split()
print(x)
dict1 = {words:len(words) for words in sentence.split() }
print(dict1)