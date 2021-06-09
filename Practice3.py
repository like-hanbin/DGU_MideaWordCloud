#!/usr/bin/env python
# coding: utf-8

# In[17]:


from konlpy.tag import Kkma
import collections


# In[11]:


kkma = Kkma()


# In[13]:


print(kkma.sentences("네 안녕하세요. 반갑습니다. 저는 마한빈입니다."))


# In[15]:


print(kkma.nouns("진실로 진실로 내가 그대를 사랑하는 까닭은 내 나의 사랑을 한없이 잇닿은 그 기다림으로 바꾸어 버린 데 있었다. 밤이 들면서 골짜기엔 눈이 퍼붓기 시작했다. 내 사랑도 어디쯤에선 반드시 그칠 것을 믿는다. 다만 그때 내 기다림의 자세를 생각하는 것뿐이다. 그 동안에 눈이 그치고 꽃이 피어나고 낙엽이 떨어지고 또 눈이 퍼붓고 할 것을 믿는다."))


# In[21]:


collections.Counter(["가","나","다","라","가","나"]).most_common(2)


# In[ ]:




