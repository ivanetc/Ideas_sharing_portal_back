import json
import math
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

AVGDL = 0
IDF = {}


def lose_non_russian_alphabet(text):
    return re.sub('[^а-яА-ЯёЁ]', '', text)


def compute_frequency_dictionary(request, document):
    count = {}
    for word in document:
        if word in request:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

    for word in request:
        if word not in count:
            count[word] = 0

    return {word: c / len(document) for word, c in count.items()}


def compute_avgdl(texts):
    corpus_length = 0
    for text in texts:
        corpus_length += len(text)
    return corpus_length / len(texts)


def compute_idf(request, texts):
    count = {}
    for text in texts:
        for word in request:
            if word in text:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

    for word in request:
        if word not in count:
            count[word] = 0
        else:
            count[word] = math.log2(len(texts) / count[word])

    return count


def compute_relevance(check_object):
    freq_dict = compute_frequency_dictionary(check_object['user_text'], check_object['idea_text'])
    relevance = 0
    for word in check_object['user_text']:
        relevance += IDF[word] * (freq_dict[word] * 3) / (
                freq_dict[word] + 2 * (0.25 + 0.75 * len(check_object['idea_text']) / AVGDL))
    return check_object['group_id'], check_object['idea_id'], relevance, check_object['idea_text']


def get_token_list(text, stop_words):
    document = []
    for token in word_tokenize(text):
        token = lose_non_russian_alphabet(token).lower()
        if token and token not in stop_words:
            document.append(token)
    return document


def get_relevance_list(user_text, groups):
    global AVGDL
    global IDF

    stop_words = set(stopwords.words('russian'))
    request = get_token_list(user_text, stop_words)

    server_texts = []
    for group in groups:
        for idea in group['ideas']:
            document = get_token_list(idea['text'], stop_words)

            server_texts.append(
                {'group_id': group['id'], 'idea_id': idea['id'], 'idea_text': document, 'user_text': request})

    AVGDL = compute_avgdl([text['idea_text'] for text in server_texts])
    IDF = compute_idf(request, [text['idea_text'] for text in server_texts])

    result = []
    for srt in server_texts:
        result.append(compute_relevance(srt))
    result.sort(key=lambda x: x[2], reverse=True)

    return result[0:5]


# get_relevance_list("Музыка должна быть лучше!", "../../data/data.json")
