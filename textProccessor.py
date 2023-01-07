from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def readText(filename):
    file = open(filename, mode='r')
    text = file.read()
    text = text.lower()
    return text


def getCleanText(text):
    cleanedText = text.translate(str.maketrans('', '', string.punctuation))
    return cleanedText


def getTokenizedText(cleanedText):
    tokenizedText = word_tokenize(cleanedText, 'english')
    return tokenizedText


def removeStopword(tokenizedText):
    finalText = []
    for word in tokenizedText:
        if word not in stopwords.words('english'):
            finalText.append(word)
    return finalText


def getPositiveScore(finalText):
    score = SentimentIntensityAnalyzer().polarity_scores(finalText)
    positiveScore = score['pos']
    return positiveScore


def getNegativeScore(finalText):
    score = SentimentIntensityAnalyzer().polarity_scores(finalText)
    negativeScore = score['neg']
    return negativeScore


def getPolarityScore(positiveScore, negativeScore):
    polarityScore = (positiveScore - negativeScore) / ((positiveScore + negativeScore) + 0.000001)
    return polarityScore


def getSubjectivityScore(positiveScore, negativeScore, tokenizedText):
    subjectivityScore = (positiveScore + negativeScore) / ((len(tokenizedText)) + 0.000001)
    return subjectivityScore


def getAverageSentencelength(text):
    sentences = text.split('.')
    averageSentencelength = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
    return averageSentencelength


def getPersentageofComplexWords():
    pass


def getAverageNumberofWordPerSentence(text, tokenizedText):
    noOfSentences = len(text.split('.'))
    noOfWords = len(tokenizedText)
    avergeNumberofWordPerSentence = noOfWords / noOfSentences
    return avergeNumberofWordPerSentence


def getWordCount(tokenizedText):
    wordCount = len(''.join(tokenizedText))
    return wordCount


def getAverageWordLength(tokenizedText):
    noOfWords = len(tokenizedText)
    noOfLetters = len(''.join(tokenizedText))
    averageWordLength = noOfLetters / noOfWords
    return averageWordLength
