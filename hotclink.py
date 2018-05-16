#!coding: utf-8 
import urllib2
import sys
import re




from bs4 import BeautifulSoup
#care keyword
def PrintAllLink( ):
  care = ["苏亚雷斯","拉莫斯","国家德比","梅西","C罗","乌姆","贝尔", "裁判"]
  quote_page = 'https://bbs.hupu.com/topic'
  page = urllib2.urlopen(quote_page)
  soup = BeautifulSoup(page, 'html.parser')
	
  for a in soup.findAll('a'):
    s = a.get('class')
    # some a has class but some don't, if you simply output the class some would be u['truetit'] some would be None
    # for tag a dont have class, can not check whether class name is truetit. So first exclude None
    if s != None: 
      # only extract tag a which class is truetit. here use needle in stack to check
      if "truetit" in s:
          post_content = a.string
          temp = post_content.decode('utf8')
          #for i in range(len(care)):
          target_word = u"" + care[4]
          pattern = re.compile(target_word) 
          if pattern.search(temp) != None:
            print a.string
            post_link = 'https://bbs.hupu.com' + a.get('href')
            post_page = urllib2.urlopen(post_link)
            post_soup = BeautifulSoup(post_page, 'html.parser')
            for post_div in post_soup.findAll('div'):
              #only extract div which has id
              if post_div.get('id') != None:
                # find post topic part via navigating the parse tree by name of the tag, use this trick again and again to zoom in on a certain part
                if "tpc" in post_div.get('id'):
                  #use post_div.a refer 
                  print post_div.a.get('href')
                  # tpc_author_home_page = urllib2.urlopen(post_div.a.get('href'))
                  # tpc_author_soup = BeautifulSoup(tpc_author_home_page,'html.parser')
                  # for home_page_div in tpc_author_soup.findAll('div'):
                  #   if post_div.get('id') != None:
                  #     if "personalinfo" in post_div.get('class'):
            # for post_a in post_soup.findAll('a'):
            #   if post_a.get('class') != None:
            #     if "u" in post_a.get('class'):
            #       print post_a.get('href')
            #break     
  
if __name__ == "__main__" :  
    # 测试正则表达式  
  	#PrintAllLink( )
    reload(sys)
    sys.setdefaultencoding("utf-8") 
    PrintAllLink( )
    #TestReChinese( ) 