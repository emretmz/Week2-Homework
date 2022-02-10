word_1=input("Enter first word: ").lower() 
word_2=input("Enter second word: ").lower()

if __name__ == '__main__':
    word_1=set(x for x in word_1)
    word_2=set(x for x in word_2)
    
print(word_1.symmetric_difference(word_2))
print(word_1.intersection(word_2))
 