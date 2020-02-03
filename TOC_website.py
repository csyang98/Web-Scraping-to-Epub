# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:09:29 2020

@author: chris
"""
from PageGet import Chapter
import urllib.request
from bs4 import BeautifulSoup
#%%
#get URL and its corresponding html

#user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#headers={'User-Agent':user_agent,} 
#
#url = "https://www.volarenovels.com/novel/demon-wangs-favorite-fei/dwff-chapter-1"
#
#request=urllib.request.Request(url,None,headers) #The assembled request
#html = urllib.request.urlopen(request)

#%%
#soup = BeautifulSoup(html, 'lxml')
#type(soup)
#%%
#Get title and text of the code of web page
#title = soup.title
#print(title)
#%%
#Get all hyperlinks with the html tags removed
#all_links = soup.find("div", class_="entry-content").find_all('a')
#all_links=soup.find("div",class_="caption clearfix").find('h4')
#trim=all_links[0].text.strip()
#%%
#link_list=[]
#for link in all_links:
#    link_list.append(link.text)
   #item=link.get("href")
#   print(item)
#   link_list.append(item)
#%%
#portion=link_list[0:10]
#chapter_text=[]
#for link in portion:
#    ch=Chapter(link)
#    ch.getChapter()
#    ch.parseChapter()
    #chapter_text.append(ch.html_encode())
#    link=ch.getNextLink()
#    print(link)
#%%
class TOC_parser:
    
    """
    Class that creates a parser to obtain chapter links from a webpage with table of contents
    
    """
    def __init__(self, url):
        self.url=url
    def load_parser(self):
        '''
        Will return a list of all links on a web page, after running function, may have to trim out unrelated links
        before calling load_chapters
        '''
        
        try:
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            headers={'User-Agent':user_agent,} 
            request=urllib.request.Request(self.url,None,headers) #The assembled request
            html = urllib.request.urlopen(request)
        except:
            print("Invalid URL, cannot open")
            return
        
        self.soup = BeautifulSoup(html, 'lxml')
        #all_links = self.soup.find("div", class_="entry-content").find_all('a')
        all_links=self.soup.find_all('a')
        link_list=[]
        for link in all_links:
           item=link.get("href")
           link_list.append(item)
        return link_list
    #pass in a list of links to parse as book chapters
    def load_chapters(self,link_list,title_type, title_class, content_type, content_class):
        
        chapter_list=[]
        for link in link_list:
            ch=Chapter(link)
            ch.getChapter(title_type, title_class, content_type, content_class)
            ch.setChapterTitle()
            ch.parseChapter(True)
            chapter_list.append(ch)
            print(ch.getChapterTitle())
        return chapter_list
        #    link=ch.getNextLink()
        #    print(link)