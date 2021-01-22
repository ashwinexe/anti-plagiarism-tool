import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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

# for data in check_plagiarism():
#     first = data[0]
#     first = first[:len(first) - 4]
#     second = data[1]
#     second = second[:len(second) - 4]
#     if data[2] > 0.5:
#         print('\nHigh Probabilities')
#         print(first + ' and ' + second + ', Probability : ' + str(data[2]))

print('\n---------------------------------------\n')
high = []
mid = []
low =[]

# print('All test cases : ')
for data in check_plagiarism():
    if data[2]*100 >= 85:
        high.append(data)
    elif  data*100 in range(50, 85):
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
    print('')

print('High chance of Plagiarism:', end=" -> ")
# if not high == 0:
#     print('None')
chances(high)

def output(content):
    for data in content:
        first = data[0]
        first = first[:len(first) - 4]
        second = data[1]
        second = second[:len(second) - 4]
        print(first + ' and ' + second + ', Probability : ' + str(data[2]))    

# for data in high:
#     first = data[0]
#     first = first[:len(first) - 4]
#     second = data[1]
#     second = second[:len(second) - 4]
#     print(first + ' and ' + second + ', Probability : ' + str(data[2]))
    
output(high)

print('---------------------------------------\n')
print('Medium chance of Plagiarism:', end=" -> ")
chances(mid)

# for data in mid:
#     first = data[0]
#     first = first[:len(first) - 4]
#     second = data[1]
#     second = second[:len(second) - 4]
#     print(first + ' and ' + second + ', Probability : ' + str(data[2]))
output(mid)
print('---------------------------------------\n')
print('Low chance of Plagiarism:', end=" -> ")
chances(low)
# for data in low:
#     first = data[0]
#     first = first[:len(first) - 4]
#     second = data[1]
#     second = second[:len(second) - 4]
#     print(first + ' and ' + second + ', Probability : ' + str(data[2]))
output(low)
print('')