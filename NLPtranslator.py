#!/usr/bin/env python
# coding: utf-8

# Task-1
# 	You need to translate each word or sentence from English to Spanish, French and German 
# 

# For this we are using the google translation and deep learning package deep-translator. first installing neccessary packages.

# In[27]:


get_ipython().system('pip install deep-translator')


# In[29]:


from deep_translator import GoogleTranslator
import pandas as pd
import string


# The dataset for this task can be found here... https://drive.google.com/file/d/1YMHJjblc8dDzUN1ry8BOCnAR4_TyKmXM/view?usp=sharing

# In[30]:


df=pd.read_csv('English.csv')


# In[31]:


df.columns


# In[32]:


df.shape # we can see that the dataset contains nearly 1.75lakhs of row entries.


# In[36]:


df=df.drop_duplicates() #we observed that our data has some multiple same entries, so to clean it we are removing duplicates.


# In[37]:


df


# The dataset contains punctuations at the end of the words. So we need to create a function to remove punctuation from end.
# using string.punctuation

# In[33]:


string.punctuation


# Function to remove punctuation in our row entries. 

# In[34]:


def remove_punct(txt):
    txt_nonpunct= ''.join([i for i in txt if i not in string.punctuation])
    return txt_nonpunct


# In[38]:


df['english no_punct']=df['English words/sentences'].apply(lambda x : remove_punct(x))


# In[53]:


translator= GoogleTranslator(source='english', target='es') #instance of translator from eng --> spanish
spanish_word=[translator.translate(i) for i in df['english no_punct'][0:100]] #first 100 words from the dataframe


# In[52]:


print(spanish_word[0:10])


# To translate into spanish sentences

# In[58]:


spanish_sentence=[translator.translate(i) for i in df['english no_punct'][-100:-1]] #first 100 sentences from df


# In[59]:


print(spanish_sentence[1:10])


# Now English --> French 

# In[60]:


translator= GoogleTranslator(source='english', target='french')
french_word=[translator.translate(i) for i in df['english no_punct'][0:100]] #first 100 words in dataframe


# In[61]:


print(french_word[0:10])


# In[62]:


french_sentence=[translator.translate(i) for i in df['english no_punct'][-100:-1]]


# In[63]:


print(french_sentence[0:10])


# Now english to German 

# In[64]:


translator= GoogleTranslator(source='english', target='german')
german_word=[translator.translate(i) for i in df['english no_punct'][0:100]]


# In[65]:


print(german_word[0:10])


# In[66]:


german_sentence=[translator.translate(i) for i in df['english no_punct'][-100:-1]]


# In[67]:


print(german_sentence[0:10])

