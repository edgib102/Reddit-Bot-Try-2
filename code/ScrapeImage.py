from PIL import Image
from requests.api import options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, requests, os


def search_google(search_query,maxImages):
    print('scraping images from google')
    options = Options()
    options.headless = True    

    browser = webdriver.Firefox(options=options,firefox_profile='C:/Users/edgib102/Documents/geckodriver-v0.29.1-win64')
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)
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
        reponse = requests.get(images_url[count])
        if reponse.status_code == 200:
            imageList.append(f"Thumbnail\\search{count}.png")
            with open(f"Thumbnail\\search{count}.png","wb") as file:
                file.write(reponse.content)

        count += 1

        # Stop get and save after 5
        if count == maxImages:
            break
    print('finished scraping images from google')
    return imageList



if __name__ == '__main__':
    items = search_google('dog png', 10)

