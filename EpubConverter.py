# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 13:58:04 2020

@author: chris
"""
#%%
from PageGet import Chapter
from TOC_website import TOC_parser
from ebooklib import epub
#%%
#load the chapters into the parser
test=TOC_parser("https://exiledrebelsscanlations.com/novels/grandmaster-of-demonic-cultivation/")
chapters=test.load_parser()
#%%
#cut out excess links not relavent to the novel
#only keep links that reference book chapters
chapters=chapters[62:191]
#%%
#get the content for each book chapter
chapter_list=test.load_chapters(chapters,"h1","entry-title","div","entry-content")
#%%
#for chapter in chapters:
#    print(chapter.getTitle())
#    print(chapter.getFilename())
#    chapters_text.append(chapter.getChapterText())

#%%
chapter_names=[] #chapter check
for chapter in chapter_list:
    chapter_names.append(chapter.getChapterTitle())
#%% FIX Corrections here
chapter_list[27].setNewChapterTitle("Chapter 28: That Person")
chapter_list[31].setNewChapterTitle("Chapter 32")
chapter_list[93].setNewChapterTitle("Chapter 94")
chapter_list[94].setNewChapterTitle("Chapter 95")
chapter_list[95].setNewChapterTitle("Chapter 96")
chapter_list[96].setNewChapterTitle("Chapter 97") 
         
#%%
for chapter in chapter_list:
    print(chapter.getFilename())
#%%    
flag = 0
  
# using naive method  
# make sure all .xhtml files have unique names 
for i in range(len(chapter_names)): 
        for i1 in range(len(chapter_names)): 
            if i != i1: 
                if chapter_names[i] == chapter_names[i1]: 
                    flag = 1
                    print(i)
                    print(chapter_names[i])
  
  
# printing result 
if(not flag) : 
    print ("List contains all unique elements") 
else :  
    print ("List contains does not contains all unique elements")  
 
#%% 
#Create epub    
book = epub.EpubBook()
#have to manually input ebook information
book.set_identifier('gdc')
book.set_title("Grandmaster of Demonic Cultivation")
book.set_language('en')
book.add_author('Mo Xiang Tong Xiu')
book.add_author('Translation by ExiledRebelsScanlations')
#book.set_cover(file_name="cover_page.xhtml",content="book_cover.jpg")
book.spine = ['nav']
#%%
#convert into ebook chapter
for chapter in chapter_list:
    #create chapter and set content, add to spine and table of contents
    ch = epub.EpubHtml(title=chapter.getChapterTitle(),
                   file_name=chapter.getFilename(),
                   lang='en')
    ch.set_content(chapter.getChapterText())
    book.add_item(ch)
    book.toc.append(ch)
    book.spine.append(ch)

#add style, arbitrary, can be changed with ebook reader
style = 'body { font-family: Times, Times New Roman, serif; }'

nav_css = epub.EpubItem(uid="style_nav",
                        file_name="style/nav.css",
                        media_type="text/css",
                        content=style)
book.add_item(nav_css)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
#generate output ebook
epub.write_epub('gdc.epub', book)