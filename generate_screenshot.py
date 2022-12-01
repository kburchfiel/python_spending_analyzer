# Python file for generating screenshots using Selenium
# By Kenneth Burchfiel
# Released under the MIT license

from selenium import webdriver
import time
import os

def generate_screenshot(path_to_html, html_name, path_to_image = None, image_name = None, image_extension = '.png', window_width = 3000):
    '''Creates a screenshot of an HTML graphic.
    
    path_to_html: the full path to the folder where the HTML file is located. Should
    not include the HTML file itself. (e.g. use 'folder' rather than 'folder/file.html'

    html_name: the HTML file name. You can include the .html
    component, or the function will do so for you.

    path_to_image: the full path to the folder where you wish to place the screenshot.
    As with path_to_html, it should not include the image name itself.

    image_name: The name of the image. It should not include any image extension
    (e.g. .png).

    image_extension: the extension that you wish to use, including the period
    before the extension (e.g. .png).

    window_width: the width of the browser window that you wish to have render
    the graphic. Larger widths result in larger image files.


    html_name_and_extension should include '''
    ff_driver = webdriver.Firefox() 
    # See https://www.selenium.dev/documentation/webdriver/getting_started/open_browser/
    # For more information on using Selenium to get screenshots of .html 
    # files, see my get_screenshots.ipynb file within my route_maps_builder
    # program, available here:
    # https://github.com/kburchfiel/route_maps_builder/blob/master/get_screenshots.ipynb
    ff_driver.set_window_size(window_width,window_width*(9/16)) # Creates
    # a window with an HD/4K/8K aspect ratio
    if '.html' not in html_name: 
        html_name = html_name + '.html' 
    full_path_to_html = os.path.join(path_to_html, html_name)
    ff_driver.get(full_path_to_html)
    # See https://www.selenium.dev/documentation/webdriver/browser/navigation/
    time.sleep(2) # This gives the page sufficient
    # time to load the map tiles before the screenshot is taken. 
    # You can also experiment with longer sleep times.
    # Setting image path details:
    if path_to_image == None:
        path_to_image = path_to_html # Will save images in the same folder
        # as the original HTML file if no other image path is specified
    if image_name == None:
        image_name = html_name.replace('.html', '') # Will use the same
        # file name as that for the HTML file 
    full_path_to_image = os.path.join(path_to_image, image_name)+image_extension
    print("Saving to:",full_path_to_image)
    screenshot_image = ff_driver.get_screenshot_as_file(full_path_to_image) 
    # Based on:
    # https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/TakesScreenshot.html

    ff_driver.quit()
    # Based on: https://www.selenium.dev/documentation/webdriver/browser/windows/