#!coding: utf-8 
import urllib2
import sys
import re




from bs4 import BeautifulSoup
#care_word keyword

def PrintAllLink( ):
  care_word = ["西甲","阿根提","葡萄牙","西班牙","梅西","C罗", "裁判"]
  quote_page = 'https://bbs.hupu.com/topic'
  page = urllib2.urlopen(quote_page)
  soup = BeautifulSoup(page, 'html.parser')
  post_count = 0
  care_post_count = 1
  avail_favor_team_count = 0
  hit = 0
  for a in soup.findAll('a'):    
    s = a.get('class')
    # some a has class but some don't, if you simply output the class some would be u['truetit'] some would be None
    # for tag a dont have class, can not check whether class name is truetit. So first make sure you exclude None class
    if s != None: 
      # only extract tag a which class is truetit. here use needle in stack to check
      if "truetit" in s:
          post_count += 1
          post_content = a.string
          temp = post_content.decode('utf8')
          care = 0
          for i in range(len(care_word)):
            target_word = u"" + care_word[i]
            pattern = re.compile(target_word) 
            if pattern.search(temp) != None:
              care += 1
          if care >= 1:
            #strange way to concat int & string in python, str convert value to a string form so they can be combinded with other strings
            print str(care_post_count) + "." + a.string
            care_post_count += 1
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
                  tpc_author_link = post_div.a.get('href')
                  tpc_author_home_page = urllib2.urlopen(tpc_author_link)
                  tpc_author_soup = BeautifulSoup(tpc_author_home_page,'html.parser')
                  for home_page_div in tpc_author_soup.findAll('div'):
                    # if "class" in home_page_div:
                    #   if (home_page_div['class']=="personalinfo"):
                    #     print home_page_div
                    if home_page_div.get('class') != None:
                      if "personalinfo" in home_page_div.get('class'):
                        # print home_page_div
                        has_favor_team = False
                        for span in home_page_div:
                          if span.string != None:
                            # print span.string
                            span_content = span.string
                            span_content_searcheable = span_content.decode('utf8')
                            favor = u"" + care_word[0]
                            favor_pattern = re.compile(favor)
                            # use target span's previous span to locate
                            if favor_pattern.search(span_content_searcheable) != None:
                              # print span_content
                              # use next_sibling to navigate target next span
                              avail_favor_team_count += 1
                              favor_team = span.next_sibling.string
                              print favor_team
                              comparable_team = "皇马"
                              ucompareable_team = comparable_team.decode('utf8')
                              ufavor_team = favor_team.decode('utf8')
                              if ucompareable_team == ufavor_team:
                                hit += 1
                                print "hit" + str(hit)
                              has_favor_team = True
                              #跳过后面的span
                        if has_favor_team == False:
                          print "currently cannot know its favor team"
                          # # no favor team in personal page
                          # tpc_author_tpc_link = tpc_author_link + "/topic"
                          # print tpc_author_tpc_link
                          # tpc_author_tpc_page = urllib2.urlopen(tpc_author_tpc_link)
                          # tpc_author_tpc_soup = BeautifulSoup(tpc_author_tpc_page, 'html.parser')
                          # #print tpc_author_tpc_soup
                          # print tpc_author_tpc_soup.select('div[id^=container]')
                          # # for tpc_page_div in tpc_author_tpc_soup.findAll('div'):
                          # #   if tpc_page_div.get('id') != None:
                          # #     print "success check div id"
                          # #     print tpc_page_div
                          # #     if "container" in tpc_page_div.get('id'):
                          # #       print "success locate contend div"
                          # #       print tpc_page_div
                          # # for tpc_page_a in tpc_author_tpc_soup.finaAll('td'):
                          # #   print tpc_page_a
                  # 按id找就可以，按class找就会报syntax error, the part find tpc could be modify by use one statement
                  # personalinfo_div_tag = tpc_author_soup.find("div", id="event")
                  # print personalinfo_div_tag
            # for post_a in post_soup.findAll('a'):
            #   if post_a.get('class') != None:
            #     if "u" in post_a.get('class'):
            #       print post_a.get('href')
            #break 
  print "-------------------------"
  print "statistic summary"
  print "care post percentage: " + str( float (care_post_count - 1) / post_count)
  print "available favor team percentage: " + str( float (avail_favor_team_count)/ (care_post_count - 1))
  print "hit percentage: " + str(float (hit) / avail_favor_team_count )

  
if __name__ == "__main__" :  
    # 测试正则表达式  
  	#PrintAllLink( )
    reload(sys)
    sys.setdefaultencoding("utf-8") 
    PrintAllLink( )
    #TestReChinese( ) 