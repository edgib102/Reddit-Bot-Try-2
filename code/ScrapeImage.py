from PIL import Image
from nltk.util import pr
from requests.api import options
from requests.sessions import InvalidSchema
from selenium import webdriver
import selenium
from selenium.webdriver.firefox.options import Options
import time, requests, os
import base64
from lxml import html
from binascii import a2b_base64

def search_google(search_query,maxImages):
    print('scraping images from google')
    options = Options()
    options.headless = False   

    browser = webdriver.Firefox(options=options,firefox_profile='C:/Users/edgib102/Documents/geckodriver-v0.29.1-win64')
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)

    try:
        browser.find_element_by_class_name('hIOe2').click()
        browser.f
    except:
        print('no tranparency button')   

    elements = browser.find_elements_by_class_name('rg_i')

    global imageList    
    imageList = []

    count = 0
    for e in elements:
        # get images source url
        e.click()
        time.sleep(1)
        element = browser.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
           big_img = element[1].find_element_by_class_name('n3VNCb')

        images_url.append(big_img.get_attribute("src"))

        # write image to file
        # try:

        try:
            response = requests.get(images_url[count])
        except InvalidSchema:
            print(f'fucky data')
            ext = images_url[count].partition("data:image/")[2].split(';')[1]
            ext = ext.partition('base64,')[2]

            binary_data = a2b_base64(ext)
            fd = open(f"Thumbnail\\search{count}.png", 'wb')
            fd.write(binary_data)
            fd.close()

            print(count)
            count+=1
            if count >= maxImages:
                break
            continue



        if response.status_code == 200:
            imageList.append(f"Thumbnail\\search{count}.png")

            with open(f"Thumbnail\\search{count}.png","wb") as file:
                file.write(response.content)
        print(count)
        count += 1

        # Stop get and save after 5
        if count >= maxImages:
            break
    print('finished scraping images from google')
    # browser.close()
    return imageList



if __name__ == '__main__':
    items = search_google('dog png', 10)

