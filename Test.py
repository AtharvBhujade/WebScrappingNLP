import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string


filename = "Final\\1.txt"
file = open(filename, mode='r')
text = file.read()
lowerCase = text.lower()
toBeRemoved = '!#$%&^*+__--:;/\<>@[]|`,.{}~'
toBeReplaced = ["'", "(", ")", "\""]
replacing = [" ", " ", " ", " "]
toBeReplaced = ' '.join([str(elem) for elem in toBeReplaced])
replacing = ' '.join([str(elem) for elem in replacing])

cleanedText = lowerCase.translate(str.maketrans(toBeReplaced, replacing, toBeRemoved))

tokenizedText = cleanedText.split()
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
finalText = []
for word in tokenizedText:
    if word not in stopwords:
        finalText.append(word)
# print(string.punctuation)
print(finalText)

print("Hello")
