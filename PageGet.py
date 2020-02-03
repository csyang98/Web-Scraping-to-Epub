# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:39:02 2020

@author: chris
"""

import urllib.request
from bs4 import BeautifulSoup
#%%

class Chapter:
    
    
    """
    Class that represents a chapter of a book
    
    Instance Variables
    - url: URL of the page
    - body_text: text directly obtained from website w/o html encoding
    - chapter_text: text that has been parsed and html encoded for epub
    - chapter_title: chapter title
    
    """
    
    
    def __init__(self,url):
        self.url=url

    def getChapter(self, title_type, title_class, content_type, content_class):
        #use URL to open webpage and get text
        try:
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent,} 
            request=urllib.request.Request(self.url,None,headers) #The assembled request
            html = urllib.request.urlopen(request)
        except:
           print("Invalid URL, cannot open")
            #return
        
        self.soup = BeautifulSoup(html, 'lxml')
        
        #chapter_title is what will show up as the header of every chapter

        
        #chapter title for dwff
#        title=self.soup.find("div",class_="caption clearfix").find('h4')
#        self.chapter_title=title.text.strip()
#        print(self.chapter_title)
        
        
        self.chapter_title=self.soup.find(title_type, class_=title_class).find('h3')
        print(self.chapter_title)
#        self.chapter_title=self.chapter_title.replace(self.soup.find("span",class_="wtr-time-wrap after-title").get_text(),"")
#        self.chapter_title=self.chapter_title.replace("GDC","")
#        self.chapter_title=self.chapter_title.strip()
#        print(self.chapter_title)
        
        
        
        #book_chapter is what the chapter headings will show up as in the table of contents
#        self.book_chapter=self.soup.find("header",class_="entry-header").find('h1').get_text()
#        pos=self.book_chapter.index(":")
#        self.book_chapter=self.book_chapter[pos+1:].strip()        
        
        #add all the chapter text 
        self.body_text=[]     
        #for paragraph in self.soup.find_all('p'):
        
        #add text into Chapter
        for paragraph in self.soup.find(content_type, class_=content_class).find_all('p'):
            self.body_text.append(paragraph.text)
            #print("{"+paragraph.text+"}")
            
    def getNextLink(self): #return str with link to the next page
        self.next_link=self.soup.find("div", class_="nav-next").find('a').get("href")
        return self.next_link
    
    def getTitle(self): #used when creating epub
        return str(self.book_chapter)
    
    def parseChapter(self, mode): #use this for replacing words in the text
        #mode determines if making replacements is necessary-> False results in no replacements
      
        replacements={"WangJi":"Wangji", "WuXian":"Wuxian","XiChen":"Xichen","ZiYuan":"Ziyuan",
                      "LuanZang Hill":"the Burial Mounds","HanGuang-Jun":"Hanguang-Jun",
                      "FengMian":"Fengmian","YanLi":"Yanli","ZeWu-Jun":"Zewu-Jun","SiZhui":"Sizhui","JingYi":"Jingyi",
                      "QiRen":"Qiren","GuangYao":"Guangyao","LianFang-Zun":"Lianfang-Zun","Jin ZiXuan":"Jin Zixuan",
                      "GuangShan":"Guangshan","XuanYu":"Xuanyu","RuoHan":"Ruohan","MingJue":"Mingjue","ChiFeng-Zun":"Chifeng-Zun",
                      "HuaiSang":"Huaisang","Xiao XingChen":"Xiao Xingchen", "YiLing":"Yiling"}

        text=""
        text+="<h1>"+self.chapter_title+"</h1>"
        for line in self.body_text:
            words=line
            #words=removeInTextNotes(words)
            #print(words)
            if mode==True:
                for word in replacements:
                    words=words.replace(word,replacements[word])
            text+="<p>"+words+"</p>"
           # print(text)
        self.chapter_text=text
        return
    
    def getFilename(self, website): # will create the .xhmtl filename for ebook creation
#        #print(self.book_chapter)
#        try:
#            parts=self.book_chapter.split()
#        except IndexError:
#            return self.book_chapter+".xhtml" 
#        
#        if(len(parts)<2):
#            return self.book_chapter+".xhtml" 
#        
#        filename=parts[0]+"0"+parts[1]
#        for i in range(2,len(parts)):
#            filename+=parts[i]
#        filename+=".xhtml"
#        return filename
        filename=self.url.replace(website,"")
        filename=filename.replace("/","")
        filename=filename.strip()
        return filename+".xhtml"
    
    
    
    #getters and setters
    def setChapterTitle(self, new_title): #used to fix parser errors
        self.chapter_title=new_title
        return
    def getChapterText(self):
        return self.chapter_text
    def getChapterTitle(self): #use when creating a chapter in epub
        return self.chapter_title

#%% Test Cases
#url="https://m.wuxiaworld.co/The-Good-for-Nothing-Seventh-Young-Lady/1074879.html"   
###%%
#try:
#    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#    headers={'User-Agent':user_agent,} 
#    request=urllib.request.Request(url,None,headers) #The assembled request
#    html = urllib.request.urlopen(request)
#except:
#    print("Error in opening")
#soup = BeautifulSoup(html, 'lxml')
#
##%%
#res=soup.find("div",class_="Readarea ReadAjax_content")
#print(res.text)
##%%
#for script in soup(["script"]):
#    script.extract()    # rip it out
#
## get text
#text = soup.get_text()
#print(text)
#
#lines = (line.strip() for line in text.splitlines())
## break multi-headlines into a line each
#chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
## drop blank lines
#text = '\n'.join(chunk for chunk in chunks if chunk)
#
#print(text)
##%%
#body_text=[]
#
#for paragraph in soup.find("div", class_="entry-content").find_all('p'):
#    body_text.append(paragraph.text)
#    print(paragraph.text)
