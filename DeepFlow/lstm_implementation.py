import numpy as np

text = "Hello my name is Guillem Romero Naranjo and I live in spain therefore I am spanish"
words = text.lower().split()
unique_words = sorted(set(words))

look_up_dictionary = {word: idx for idx, word in enumerate(unique_words)}
decode_dictionary = {idx: word for word, idx in look_up_dictionary.items()}

def encode(words):
    return [look_up_dictionary[word] for word in words]

def decode(indices):
    return [decode_dictionary[idx] for idx in indices]

encoded_text = encode(words)
context_list = []
target_list = []

for idx in range(len(encoded_text) - 2):
    input_1 = encoded_text[idx]
    input_2 = encoded_text[idx + 1]
    target = encoded_text[idx + 2]
    context = (input_1, input_2)

    context_list.append(context)
    target_list.append(target)

print(context_list)
print(target_list)



class LSTM:
    def __init__(self):
        #Cell 1
        weights_1_1 = np.random.randn(2, 10)
        bias_1_1 = np.random.randn(1, 10)

    
        weights_2_1 = np.random.randn(7, 15)
        bias_2_1 = np.random.randn(1, 15)

        #Cell 2
        weights_1_2 = np.random.randn(2, 7)
        bias_1_2 = np.random.randn(1, 7)

    
        weights_2_2 = np.random.randn(7, 12)
        bias_2_2 = np.random.randn(1, 12)


        #Cell 2
        weights_1_2 = np.random.randn(2, 7)
        bias_1_2 = np.random.randn(1, 7)

    
        weights_2_2 = np.random.randn(7, 12)
        bias_2_2 = np.random.randn(1, 12)






        
