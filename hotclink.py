#!coding: utf-8 
import urllib2
import sys
import re




from bs4 import BeautifulSoup
#care keyword
def PrintAllLink( ):
  care = ["西甲","苏亚雷斯","拉莫斯","国家德比","梅西","世界杯","乌姆","C罗", "裁判"]
  quote_page = 'https://bbs.hupu.com/topic'
  page = urllib2.urlopen(quote_page)
  soup = BeautifulSoup(page, 'html.parser')
  count = 1
  for a in soup.findAll('a'):    
    s = a.get('class')
    # some a has class but some don't, if you simply output the class some would be u['truetit'] some would be None
    # for tag a dont have class, can not check whether class name is truetit. So first make sure you exclude None class
    if s != None: 
      # only extract tag a which class is truetit. here use needle in stack to check
      if "truetit" in s:
          post_content = a.string
          temp = post_content.decode('utf8')
          #for i in range(len(care)):
          target_word = u"" + care[5]
          pattern = re.compile(target_word) 
          if pattern.search(temp) != None:
            #strange way to concat int & string in python
            print str(count) + "." + a.string
            count += 1
            post_link = 'https://bbs.hupu.com' + a.get('href')
            post_page = urllib2.urlopen(post_link)
            post_soup = BeautifulSoup(post_page, 'html.parser')
            for post_div in post_soup.findAll('div'):
              #only extract div which has id
              if post_div.get('id') != None:
                # find post topic part via navigating the parse tree by name of the tag, use this trick again and again to zoom in on a certain part
                if "tpc" in post_div.get('id'):
                  # #use post_div.a refer 
                  # print post_div.a.get('href')
                  tpc_author_home_page = urllib2.urlopen(post_div.a.get('href'))
                  tpc_author_soup = BeautifulSoup(tpc_author_home_page,'html.parser')
                  for home_page_div in tpc_author_soup.findAll('div'):
                    # if "class" in home_page_div:
                    #   if (home_page_div['class']=="personalinfo"):
                    #     print home_page_div
                    if home_page_div.get('class') != None:
                      if "personalinfo" in home_page_div.get('class'):
                        # print home_page_div
                        for span in home_page_div:
                          if span.string != None:
                            # print span.string
                            span_content = span.string
                            span_content_searcheable = span_content.decode('utf8')
                            favor = u"" + care[0]
                            favor_pattern = re.compile(favor)
                            # use target span's previous span to locate
                            if favor_pattern.search(span_content_searcheable) != None:
                              # print span_content
                              # use next_sibling to navigate target next span
                              favor_team = span.next_sibling.string
                              print favor_team
                              comparable_team = "皇马"
                              ucompareable_team = comparable_team.decode('utf8')
                              ufavor_team = favor_team.decode('utf8')
                              print ucompareable_team == ufavor_team
                  # 按id找就可以，按class找就会报syntax error, the part find tpc could be modify by use one statement
                  # personalinfo_div_tag = tpc_author_soup.find("div", id="event")
                  # print personalinfo_div_tag
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