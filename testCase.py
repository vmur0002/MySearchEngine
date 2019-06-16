import nltk.stem.porter
from collections import *
import math
import re
import os


# noinspection RegExpRedundantEscape
class MySearchEngine:

    # matched_lists = []
    # document_ID = []

    def tokenizing(self, text, matched_lists):
        match = []

        match_hypend = re.findall("\w+\-\n+\w*", text)
        for word in match_hypend:
            hypen = word.replace("-\n", "")
            match.append(hypen)
        text = re.sub("\w+\-\n+\w*", "", text)

        # match_email = re.findall("\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", text)
        match_email = re.findall("\w[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\w", text)
        match.extend(match_email)
        text = re.sub("\w[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\w", "", text)

        match_quotation = re.findall("\s+\'(?:.*)'", text)
        for word in match_quotation:
            quotation = word.replace("\n", "")
            match.append(quotation)
        text = re.sub("\s+\'(?:.*)'", "", text)

        match_url = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", text)
        match.extend(match_url)
        text = re.sub("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", "", text)

        match_ip = re.findall("\d{1,3}\.+\d{1,3}\.+\d{1,3}\.+\d{1,9}", text)
        match.extend(match_ip)
        text = re.sub("\d{1,3}\.+\d{1,3}\.+\d{1,3}\.+\d{1,9}", "", text)

        match_acronym = re.findall("((?:[A-Z]\.[A-Z.]*){2,})", text)
        match.extend(match_acronym)
        text = re.sub("((?:[A-Z]\.[A-Z.]*){2,})", "", text)

        match_capital = re.findall("(?:[A-Z][a-z]+\s){2,}", text)
        for word in match_capital:
            capital = word.replace("\n", "")
            match.append(capital)
        text = re.sub("(?:[A-Z][a-z]+\s){2,}", "", text)
        split_list = []
        split_list = re.split("\s+|\n|[,:;(')?!{}.-]\s*", text)
        for element in split_list:
            if element == '':
                split_list.remove(element)
        for element in split_list:
            match.append(element)
        matched_lists.append(match)
        return matched_lists

    def stopwords_func(self, matched_lists, stopwords_list):
        outer_list = []
        for lists in matched_lists:
            inner_list = []
        for words in lists:
            inner = words.lower()
            inner_list.append(inner)
        outer_list.append(inner_list)

        Nostopwords = []
        for element in outer_list:
            remove_stopwords = [token for token in element if token not in stopwords_list]
            Nostopwords.append(remove_stopwords)
            # print(len(Nostopwords))
        return Nostopwords

    def stemming(self, Nostopwords):
        stemmer = nltk.stem.porter.PorterStemmer()
        Nostop_outer = []
        for lists in Nostopwords:
            Nostop_inner = []
            for words in lists:
                stem = stemmer.stem(words)
                if stem != '':
                    Nostop_inner.append(stem)
            Nostop_outer.append(Nostop_inner)

        return Nostop_outer


def main():
    path = "C:/Users/viki/Desktop/"
    file = "test.txt"
    document_ID = []
    searchEngine = MySearchEngine()
    matched_lists = []
    filename = os.path.join(path, file)
    file = open(filename, "r")
    text = file.read()
    matched_lists = searchEngine.tokenizing(text, matched_lists)

    stop = open(
        "C:/Users/viki/PycharmProjects/Assignment-DocumentsAndQueries-ForTesting/Assignment-DocumentsAndQueries-ForTesting/stopword.txt",
        "r")
    stopwords = stop.read()
    stopwords_list = []
    for word in stopwords.split():
        stopwords_list.append(word)

    Nostopwords = searchEngine.stopwords_func(matched_lists, stopwords_list)
    #print(Nostopwords)

    Nostop_outer = searchEngine.stemming(Nostopwords)
    for list in Nostop_outer:
        for items in list:
            print(items)
    #print(Nostop_outer)

main()
