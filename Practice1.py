#!/usr/bin/env python
# coding: utf-8

# In[69]:


from bs4 import BeautifulSoup


# In[70]:


from openpyxl import Workbook


# In[71]:


from selenium import webdriver


# In[72]:


driver = webdriver.Chrome("./chromedriver")


# In[73]:


result_list = []
for i in range(1,3):
    url = "https://pann.nate.com/talk/ranking/y?stdt=2020&page="+str(i)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source,"html.parser")
    
    for i in soup.select("#container > div.content.sub > div.mainarea > div.tsCnt > div.cntList > ul > li"):
        result = i.find("dl").find("dt").find("a").text
        result_list.append(result)
        print(result)


# In[74]:


driver.close()


# In[75]:


write_workbook = Workbook()


# In[76]:


write_cell = write_workbook.active


# In[79]:


for i in range(1, len(result_list)+1):
    write_cell.cell(i,1,result_list[i-1])


# In[80]:


write_workbook.save("natepann.xlsx")


# In[ ]:




