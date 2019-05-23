from selenium import webdriver
from selenium.webdriver.chrome.options import Options as options
#REFERENCE: https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver
#ATTENTION!: use interactive python run single step and open another terminal using ps command check whether process behave as u expect
#           use sleep command if u can't catch what is going on
#TAKE OUT:
#1. u can't use exist chrome binary under /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome run as chromdriver
#   like this: browser = webdriver.Chrome(executable_path="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome")
#   the binary under /Contents/MacOS is different from chromedriver binary, 
#   so you have to have a chromedriver
#2. u also need a real Chrome as well, you don't need to specify its as binary_location, but you do need one. you can move google chrome from /Applicatin to somewherelse 
#   to test it and then move it back
#3. to make it script find executable chromedriver, you either specify it using executable_path arguement or include parent folder of chromedriver(binary) to PATH env
#   or similarly just move chromedriver to some path already in PATH, for me I move it to /user/local/bin
#4. though it is weird to have to MB large file under /usr/local/bin, instead you could install chromedriver via brew, then you only have symlink under /user/local/bin
 
def checkAvail( ):
    # below 4 lines work, though not sure why you have to reassign the value
    # chrome_options = options()
    # chrome_options.binary_location="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
    # chrome_options = options()
    # browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()
    browser.get('https://www.apple.com/us-hed/shop/buy-mac/macbook-pro/15-inch')
    # print ("browser opened")
    avail = browser.find_element_by_xpath('//*[@id="model-selection"]/bundle-selection/div[4]/div[2]/div[2]/div/div[2]/div/bundle-selector/div[3]/div[1]/div/ul[2]/li[2]/div/div/div/div/div/span[2]').get_attribute('innerText')
    print (avail)
    # make sure you add close, otherwise chromdriver process would exit unexpectly because script ends
    browser.close() 
if __name__ == "__main__":
    checkAvail( )
