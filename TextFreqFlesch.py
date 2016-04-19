#!/usr/bin/env python

# In[26]:

from __future__ import division

import sys


# In[3]:

import getopt

pos_default='nl'

pos_variable=['n=']

default_sentences=2


options, args=getopt.gnu_getopt(sys.argv, pos_default, pos_variable)


# ### Process text



filename=args[-1]


# In[7]:

with open(filename) as f:
    textstring=f.read()


# In[8]:

import nltk.data


# In[9]:

sent_detector=nltk.data.load('tokenizers/punkt/english.pickle')


# In[10]:

#print('\n-----\n'.join(sent_detector.tokenize(textstring.strip())))


# In[11]:

sent_list=sent_detector.tokenize(textstring.strip(),realign_boundaries=False)


# In[12]:

import string


# In[13]:

def remove_stuff(st,remove):
    import string
    return st.translate(string.maketrans('',''),remove)


# In[14]:

def remove_all(st):
    return remove_stuff(st,string.digits+string.punctuation)


# In[15]:

def process_string(st):
    return remove_all(st.replace('-',' ')).lower().split()


# In[16]:

words_sent_list=map(process_string,sent_list)


# ### Get functional and frequency data

# In[17]:

import numpy as np


# In[18]:

#from equiv_sylb import equiv_sylb
#equiv_sylb=e.equiv_sylb


# In[19]:

#equiv_sylb(50)

def equiv_sylb(ratio):
    import numpy as np
    return 0.012/np.sqrt(ratio)


# In[20]:

import pickle


# In[21]:

#frequency_corpus='frequency_dict.pkl'
frequency_corpus='frequency_ratio_dict.pkl'

with open(frequency_corpus,'rb') as f:
    freq_ser=pickle.load(f)


# ### Compute 

# In[22]:



def get_frequency_min(word,ser,minimum):
    if ser.has_key(word):
        return ser[word]
    else:
        return minimum

mymin=min(freq_ser.values())

def get_frequency(word,ser):
	return get_frequency_min(word, ser, mymin)

# In[23]:

just_words=[item for sublist in words_sent_list for item in sublist]


# In[24]:

frequency=np.array(map(lambda x: get_frequency(x,freq_ser),just_words))


# In[25]:

total_words=len(just_words)
total_sent=len(words_sent_list)
total_sylb=equiv_sylb(frequency).sum()





# In[27]:

def flesch_kincaid_gl(words,sent,sylb):
    return 0.39*(words/sent)+11.8*(sylb/words)-15.59


# In[28]:

improved_flesch_gl=flesch_kincaid_gl(total_words,total_sent,total_sylb)
improved_flesch_gl


# ### Compute problem sentences

def process_options(optionl,n_def,pos_variable, pos_default):
	if len(optionl) > 0:
		for i in optionl:
			if i[0] in pos_variable:
				if i[1].isdigit():
					return int(i[1])
				else:
					return n_def
			elif i[0] in pos_default:
				return n_def
			else:
				return 0
	else:
		return 0
					
		
			
	
pos_defaultl=['-' + i for i in list(pos_default)]
pos_variablel=['--' + i[:-1] for i in pos_variable]

n_sent= process_options(options, default_sentences, pos_variablel, pos_defaultl)

if n_sent > 0:

	# In[31]:

	def get_sent_freq(sent,freq_ser):
		return map(lambda x: get_frequency(x,freq_ser),sent)


	# In[40]:

	sent_freq=map(lambda x: np.array(get_sent_freq(x,freq_ser)),words_sent_list)


	# In[44]:

	words_per_sent=map(lambda x: x.shape[0], sent_freq)


	# In[49]:

	def get_sent_sylb(freq_list):
		return (map(lambda x: equiv_sylb(x),freq_list))




	sylb_per_word=map(lambda x: get_sent_sylb(x),sent_freq)
	sylb_per_sent=map(sum, sylb_per_word)



	imp_flesch_sent=map(lambda x,y: flesch_kincaid_gl(x,1,y),words_per_sent,sylb_per_sent)

	n_sent=min([n_sent, len(imp_flesch_sent)])




	top_arg=np.argpartition(np.array(imp_flesch_sent),-n_sent)[-n_sent:]




	top_sent=map(lambda x: sent_list[x], top_arg)




	top_flesch=map(lambda x: imp_flesch_sent[x], top_arg)
	
	def wordl_gl(wl):
		return map( lambda x: round(flesch_kincaid_gl(1,1,x)), wl)
	
	#Not actually frequency, gl of word
	top_freq = map(lambda x: wordl_gl(sylb_per_word[x]), top_arg)


	#print map(list, top_freq)
	
	def sent_string(x):
		return '%1.0f\t\t: %s\n  \t\t: %s' % x

	sent_print=map(sent_string, zip(top_flesch,top_sent,map(str, top_freq)))


	# In[109]:

	full_document_string='document grade level: %1.0f' % improved_flesch_gl


	# In[107]:

	sentence_string=('grade level \t: sentence\n'+('-'*40)+'\n'+(('\n'+('-'*40)+'\n').join(sent_print)))


	# In[112]:

	print(full_document_string+'\n'+'-'*80+'\n\n'+sentence_string)


	# In[ ]:
else:
	print('document grade level: %1.0f' % improved_flesch_gl)



