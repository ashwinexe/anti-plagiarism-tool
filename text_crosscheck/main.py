import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from colorama import Fore, Back, Style

student_files = [doc for doc in os.listdir() if doc.endswith('.txt')]
student_notes =[open(File).read() for File in  student_files]

vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()
similarity = lambda doc1, doc2: cosine_similarity([doc1, doc2])

vectors = vectorize(student_notes)
s_vectors = list(zip(student_files, vectors))
plagiarism_results = set()

def check_plagiarism():
    global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors =s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b , text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            score = (student_pair[0], student_pair[1],sim_score)
            plagiarism_results.add(score)
    return plagiarism_results

print('\n---------------------------------------\n')
high = []
mid = []
low =[]

# print('All test cases : ')
for data in check_plagiarism():
    temp = int(data[2]*100)
    if temp >= 85:
        high.append(data)
    elif  temp in range(50, 85):
        mid.append(data)
    else:
        low.append(data)

high.sort(key  = lambda x : x[2], reverse=True)
mid.sort(key  = lambda x : x[2], reverse=True)
low.sort(key  = lambda x : x[2], reverse=True)

def chances(ls):
    if not ls:
        print('None')
    else:
        print(len(ls))
    print(Style.RESET_ALL   + '')

def output(content):
    if not content:
        print('None')
    else:
        print(Back.BLACK, len(content))
    print(Style.RESET_ALL  + '')

    for data in content:
        first = data[0]
        first = first[:len(first) - 4]
        second = data[1]
        second = second[:len(second) - 4]
        print(first + ' and ' + second + ', Probability : ' + str(round(data[2]*100, 3)) + '%')    

print(Back.RED + 'High chance of Plagiarism:', end=" -> ")
output(high)

print('---------------------------------------\n')
print(Back.YELLOW + 'Medium chance of Plagiarism:', end=" -> ")

output(mid)

print('---------------------------------------\n')
print(Back.GREEN + 'Low chance of Plagiarism:', end=" -> ")

output(low)
print('')
os.system('Pause')