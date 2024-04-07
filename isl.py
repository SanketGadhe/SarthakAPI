import ast
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import os
def word(sentence):
    '''
    Sentence to words
    '''
    if sentence[-1]=='.':
        sentence=sentence[:-1]
    words=sentence.split(' ')
    return words
def stop_word_removal(sentence):
    '''
    Removing the words which have no sign (ISL stop Words)
    '''
    stop_words = set(stopwords.words('english'))
    removed_stopword=[w for w in sentence if w not in stop_words]
    return removed_stopword
def sentence_lemmatization(sentence):
    '''
    lemmatizing the word to v1 form
    '''
    lemmatizer=WordNetLemmatizer()
    lemmatized_sentence=[lemmatizer.lemmatize(w) for w in sentence]
    return lemmatized_sentence
def synonym_replacement(sentence):
    '''
    Replacing the word with ISL available similar word
    '''
    r=open("synonym.txt","r")
    synonym_dictionary=r.read()
    synonym_dictionary=ast.literal_eval(synonym_dictionary)
    replaced_synonyms=[]
    for word in sentence:
        if word not in synonym_dictionary.keys():
            replaced_synonyms.append(word)
            continue 
        replaced_synonyms.append(synonym_dictionary[word])
    return replaced_synonyms
def isl_famed(sentence):
    '''
    Framing list of words to ISL sentence
    '''
    framed_sentence=""
    for word in sentence:
        framed_sentence+=word.lower()+" "
    return framed_sentence
def word_available(word):
    '''
    checking if the word is available in ISL Dictionary
    '''
    r=open("ISL_Dictionary.txt","r")
    file=r.read()
    list_of_word=list(file.split(","))
    if word in list_of_word:
        return True
    else:
        return False
def list_of_available(sentence):
    '''
    returning the available words 
    if not in available in ISL dictionary like name words then appending their spelling
    '''
    available=[]
    words=sentence.lower()
    words=words.split(' ')
    for word in words:
        if word_available(word):
            available.append(word)
        else:
           for letter in word:
               available.append(letter)
    return available
def word_available_sarthak(word):
    '''
    checking if the word is available in Sarthak Dictionary
    #Will be Removed in Future 
    '''
    with open('Sarthak_Dictionary.txt', 'r') as f:
        lines = f.read()
    print(lines)
    if word in lines:
        return True
    else:
        return False
def list_of_available_sarthak(sentence):
    '''
    returning the available words 
    if not in available in ISL dictionary like name words then appending their spelling
    #Will be removed in Future
    '''
    available=[]
    words=sentence.lower()
    words=words.split(' ')
    for word in words:
        if word_available_sarthak(word):
            available.append(word)
        else:
           for letter in word:
               available.append(letter)
    return available[:-1]

def isl_framing(sentence):
    '''
    Operating Function to directly convert any sentence to ISL Format
    '''
    sentence=word(sentence)
    sentence=stop_word_removal(sentence)
    sentence=sentence_lemmatization(sentence)
    sentence=synonym_replacement(sentence)
    sentence=isl_famed(sentence)
    return sentence.capitalize()