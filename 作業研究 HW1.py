#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("My student ID number:",112426015)
print("My English name is Aaren and my Chinese name is 張博崴",)
print("I come from Taipei. I'm 22 years old now and I like to play basketball and guitar")


# In[14]:


#宣告變數將圖形拆分為兩半執行
upside = 5
downside = 2

# Print 上半部
for i in range(1, upside + 1):
    spaces = " " * (upside - i )
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Print 下半部
for i in range(1, downside + 1):
    spaces = " " * (downside )
    stars = "*" * 5
    print(spaces+stars)


# In[22]:


age=input("How oldare you? ")#讓使用者輸入自己的年齡
age=int(age)
if age > 22:
    print("elder")#若大於22歲print elder
elif age == 22:
    print("I am not elder")#若等於22歲print I am not elder
else: 
    print("younger")#若小於22歲 print younger


# In[37]:


family_member=input("請輸入你的家庭人數?")
family_member=int(family_member)#將輸入的結果轉文整數型態，方便後續運算
print("我家共有",family_member,"人")

my_age=22
dad_age=52
mom_age=47

print("我的年紀:",my_age,"媽媽的年紀:",mom_age,"爸爸的年紀:",dad_age)
result= float((my_age+mom_age+dad_age)/family_member)#以符點數表示更加精確
print("我們家的年齡平均:",result,"歲")

