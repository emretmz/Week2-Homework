import string
sentence=list(input("Write a sentences:").lower().replace(" ", ""))
sentence.sort()
def count_letter(sentence):
   frequency=[sentence.count(x) for x in sentence if x not in string.punctuation]
   result_dictionary=dict(zip(sentence,frequency))
   return print(result_dictionary)
count_letter(sentence)
