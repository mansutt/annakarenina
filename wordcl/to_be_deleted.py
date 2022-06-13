with open('stopwords.txt', 'r') as file:
    stopwords = file.readlines()
    converted_list = []
    for e in stopwords:
        converted_list.append(e.strip())
