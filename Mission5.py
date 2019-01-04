
# coding: utf-8

# In[ ]:


""""
使用python的request模組去訪問https://jsonplaceholder.typicode.com/users  取得第2,3,4,5 筆資料,

偵測當時日期，轉作檔名，將2345筆資料內容寫入檔案中。
""""


# In[1]:


# 使用python的request模組去訪問 https://jsonplaceholder.typicode.com/users 並轉成Json

# 載入request
import requests 
# 用request去取得訪問網頁
a = requests.get('https://jsonplaceholder.typicode.com/users')
# 轉成json
data = a.json()
# 印出檔案
print(a.text)


# In[2]:


# 取得第 2,3,4,5 筆資料
newData = data[1:5]
# 印出這幾筆資料
print(newData)


# In[3]:


# 偵測當時日期

# 載入套件
import datetime
# 設為utc時間
nowUtcUnixTime = datetime.datetime.utcnow().timestamp()


# In[4]:


# 轉作文字格式檔名
fileName = str(nowUtcUnixTime) + '.txt'


# In[6]:


# 將2345筆資料內容寫入新檔案中,然後關閉檔案

# 載入json
import json
# 以新檔名開一個新檔案
newFile = open(fileName,'w')
# 將新json寫入檔案
newFile.write(json.dumps(newData))
# 將檔案關閉
newFile.close()

