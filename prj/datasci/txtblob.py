from textblob import TextBlob

'''
$ pip install -U textblob
$ python -m textblob.download_corpora

This will install TextBlob and download the necessary NLTK corpora. If you need to change the default download directory set the NLTK_DATA environment variable.
https://www.geektime.co.il/nlp-technology-modules-intel/
http://textprocessing.org/a-beginners-guide-to-textblob
'''


test_text = "Text mining, also referred to as text data mining, roughly equivalent to text analytics, is the process of deriving high-quality information from text. High-quality information is typically derived through the devising of patterns and trends through means such as statistical pattern learning. Text mining usually involves the process of structuring the input text (usually parsing, along with the addition of some derived linguistic features and the removal of others, and subsequent insertion into a database), deriving patterns within the structured data, and finally evaluation and interpretation of the output. 'High quality' in text mining usually refers to some combination of relevance, novelty, and interestingness. Typical text mining tasks include text categorization, text clustering, concept/entity extraction, production of granular taxonomies, sentiment analysis, document summarization, and entity relation modeling (i.e., learning relations between named entities)."

# Word Tokenization 
print('Word Tokenization')
text_blob = TextBlob(test_text)
print (text_blob.words)

# Sentence Tokenization
print('Sentence Tokenization')
 
# Cycle through the sentences list  
for i in text_blob.sentences:
    print("{} : {}".format(text_blob.sentences.index(i), i))

#print (text_blob.sentences)


# Sentiment Analysis
for sentence in text_blob.sentences:
    print(sentence.sentiment)

# POS Tagging
print(text_blob.tags)	

print('text_blob.words[-1] = ',text_blob.words[-1])
print ('text_blob.words[-1].singularize() = ',text_blob.words[-1].singularize())

print('text_blob.words[0]  = ',text_blob.words[0]) 
print ('text_blob.words[0].pluralize() = ',text_blob.words[0].pluralize())
 
 
from textblob import Word
 
w = Word("are")
 
print('w.lemmatize()= ', w.lemmatize())
 
print('w.lemmatize(v) = ',  w.lemmatize('v'))
 
 
# WordNet
from textblob.wordnet import VERB
word = Word("are")
print (word.synsets) 
print('Definitions')
print( word.definitions)


'''

Penn Part of Speech Tags
Note:  these are the 'modified' tags used for Penn tree banking; these are the tags used in the Jet system. NP, NPS, PP, and PP$ from the original Penn part-of-speech tagging were changed to NNP, NNPS, PRP, and PRP$ to avoid clashes with standard syntactic categories.

	1.	CC	Coordinating conjunction
	2.	CD	Cardinal number
	3.	DT	Determiner
	4.	EX	Existential there
	5.	FW	Foreign word
	6.	IN	Preposition or subordinating conjunction
	7.	JJ	Adjective
	8.	JJR	Adjective, comparative
	9.	JJS	Adjective, superlative
	10.	LS	List item marker
	11.	MD	Modal
	12.	NN	Noun, singular or mass
	13.	NNS	Noun, plural
	14.	NNP	Proper noun, singular
	15.	NNPS	Proper noun, plural
	16.	PDT	Predeterminer
	17.	POS	Possessive ending
	18.	PRP	Personal pronoun
	19.	PRP$	Possessive pronoun
	20.	RB	Adverb
	21.	RBR	Adverb, comparative
	22.	RBS	Adverb, superlative
	23.	RP	Particle
	24.	SYM	Symbol
	25.	TO	to
	26.	UH	Interjection
	27.	VB	Verb, base form
	28.	VBD	Verb, past tense
	29.	VBG	Verb, gerund or present participle
	30.	VBN	Verb, past participle
	31.	VBP	Verb, non-3rd person singular present
	32.	VBZ	Verb, 3rd person singular present
	33.	WDT	Wh-determiner
	34.	WP	Wh-pronoun
	35.	WP$	Possessive wh-pronoun
	36.	WRB	Wh-adverb


'''