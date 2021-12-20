import csv
# https://alexwlchan.net/2018/12/reading-a-utf8-encoded-csv/

def translate(w):
    with open("data.csv", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        for row in csvreader:
            if w in str(row):
                print(": ".join(row))





word=input("Enter word: ")
output=translate(word)
