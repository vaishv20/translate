from textblob import TextBlob
blob = TextBlob("Comment vas-tu?")
print(blob.translate(to='es'))
print(blob.translate(to='en'))
print(blob.translate(to='zh'))

l=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

for i in l:
    blob = TextBlob(i)
    print(blob.translate(to='de'))