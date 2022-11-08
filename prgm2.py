file = open("C:\workspace\python\data.txt", "r")
data = file.read()
occurrences = data.count("python")

print('Number of occurrences of the word :', occurrences)