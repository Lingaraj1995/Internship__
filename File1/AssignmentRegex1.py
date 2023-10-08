#!/usr/bin/env python
# coding: utf-8

# In[6]:


import regex as re


# In[7]:


#Answer1-------------
text='Python Exercises, PHP exercises.'
result=re.sub(r'[ ,.]',r':',text)
print(result)


# In[8]:


#Answer2-------------
text='We should eat an apple daily'
pattern='\\b[ae]\w+'
result=re.findall(pattern,text)
print(result)


# In[9]:


#Answer3------------------------------
def Question3(text):
    superregex=re.compile('\\b\w{4,}\\b')
    for i in superregex.finditer(text):
        print(i)
        print(i.group())


# In[10]:


string1="Mahendra Singh Dhoni is my favourite cricketer"


# In[11]:


Question3(string1)


# In[12]:


#Answer4-----------------
def Question4(text):
    sup_regex=re.compile('\\b\w{3,5}\\b')
    for i in sup_regex.finditer(text):
        print(i)
        
string2="cat and dogss are very innocent pets"
Question4(string2)


# In[13]:


#Answer5----------------
sample_text=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
def Question5(text):
    sr=re.compile(r'[ ()]')
    for i in text:
        print(i)
        x=sr.sub('',i)
        print(x)


# In[14]:


Question5(sample_text)


# In[15]:


#Answer6---------------
sample_text=["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
def Question6(text):
    Answertext=[]
    sr=re.compile(r'\([^(]+\)')
    for i in text:
        print(i)
        y=sr.sub('',i)
        Answertext.append(y)     
        
    return Answertext    
        
Question6(sample_text)


# In[16]:


#Answer7-----------------
s_text="ImportanceOfRegularExpressionsInPython"
Question7=re.findall(r'[A-Z][a-z]+',s_text)
print(Question7)


# In[17]:


#Answer8----------------------------

text1="RegularExpression1IsAn2ImportantTopic3InPython"

def Question8(text):
    Q8=re.sub('([A-Z][a-z]+)(\d)',r'\1 \2',text)
    print(Q8)
    


# In[18]:


Question8(text1)


# In[19]:


#Answer9------------------
text1="RegularExpression1IsAn2ImportantTopic3InPython"

def Question9(text):
    Q9=re.sub(r'([A-Z][a-z]+)(\d+)',r'\1 \2 ',text)
    print(Q9)
    
Question9(text1)


# In[20]:


#Answer10----------------
sampletext="Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com.Please contact us at hr@fliprobo.com for further information."

Q10=re.findall(r'\w+\.*\w+\@\w+\.*\w+\.*\w+',sampletext)
print(Q10)


# In[21]:


#Answer11--------------
Question11="My_Name_is_Lingaraj_dehury_123"
Q11=re.search(r'[A-Za-z0-9_]+',Question11)
print(Q11)
print(Q11.group())


# In[22]:


#Answer12---------------------
Question12="1My name is Lingaraj."
b=re.match(r'^1.*',Question12)
print(b)
print(b.group())


# In[23]:


#Answer13-------------
ip_address="10.024.009.542"
Q13=re.sub(r'\.[0]*',r'.',ip_address)
print(Q13)


# In[24]:


#Answe14-------------------------------
Question14='On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country'
Q14=re.search(r'[A-Za-z]+\s\d{2}\w+\s\d{4}',Question14)
print(Q14)
print(Q14.group())


# In[25]:


#Answer15----------------------------
Question15="The quick brown fox jumps over the lazy dog."
patterns=['fox','dog','horse']

def AoQ15(text):
     for i in patterns:
            if re.search(i,text):
                print(i,"matched")
            else:
                print (i,"not matched")        
            


# In[26]:


AoQ15(Question15)


# In[27]:


#Answer16------------
Question15="The quick brown fox jumps over the lazy dog."

Q16=re.search(r'fox',Question15)
print(Q16)
print(Q16.span())


# In[28]:


#Answer17-----------------
Question17= 'Python exercises, PHP exercises, C# exercises'
pattern="exercises"
Q17=re.findall(pattern,Question17)
print(Q17)


# In[29]:


#Answer18--------------
Question17= 'Python exercises, PHP exercises, C# exercises'
pattern="exercises"
Q18=re.finditer(pattern,Question17)
for i in Q18:
    print(i)
    print(i.span())
    print(i.start())
    print(i.end())
    print('-------------')


# In[30]:


#Answer19----------------
def dateformat(dt):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\3-\2-\1',dt)
dt="1972-06-26"


# In[31]:


dateformat(dt)


# In[32]:


#Answer20---------------
text1="01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
def Question20(text):
    sr=re.compile(r'([0-9]+\.\d{1,2})\s')
    x=sr.findall(text)
    print (x)

#For Question no 20 couldnot think a regex code to get 0.25 in o/p


# In[33]:


Question20(text1)


# In[34]:


#Answer21-------------
text1="Ram has 13 shirts and 5 pants"

for i in re.finditer(r'\d+',text1):
    print(i)
    print(i.group())
    print(i.span())
    print(i.start())
    print(i.end())
    print("\n")


# In[35]:


#Answer22---------------
text2="My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
y=re.findall(r'\d+',text2)
print(y)
print("maximum marks:-",max(y))


# In[36]:


#Answer23---------------
text="RegularExpressionIsAnImportantTopicInPython"
def function(text):
    y=re.sub(r'([A-Z])([a-z]+)',r'\1\2 ',text)
    print(y)
    


# In[37]:


function(text)


# In[38]:


#Answer24-----------------
text="Lingaraj"
pattern=r'[A-Z][a-z]+$'
y=re.search(pattern,text)
print(y)


# In[39]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world

sample_text="Hello hello world world"
x=re.sub(r'\b(\w+)(\W+\1)\b',r'\1',sample_text)
print(x)


# In[40]:


#Answer26---------------
text="I will go to NewYork in the month 123end"
pattern=r"[a-zA-Z0-9]+$"
y=re.search(pattern,text)
print(y)
print(y.group())


# In[41]:


#Answer27-------------
text1="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
pattern=r"\#\w+"
x=re.findall(pattern,text1)
print(x)


# In[42]:


#Answer28--------------
text2="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

z=re.sub(r'\<\w+\+\d+\w+\>',r'',text2)
print(z)


# In[43]:


#Answer29--------------
text3="Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
a=re.findall(r'\d{2}-\d{2}-\d{4}',text3)
print(a)


# In[44]:


#Answer30----------------
text4="The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

def function30(text):
    sr=re.compile(r'\W*\b\w{2,4}\b')
    y=sr.sub(r'',text4)
    print(y)


# In[45]:


function30(text4)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




