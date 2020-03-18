# Modules
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration
kingdomlikes_email = ""
kingdomlikes_password = ""

google_email = ""
google_password = ""

instagram_username = ""
instagram_password = ""

actions_per_module = "20"

chrome_options = Options()
chrome_options.add_extension('ublock_origin.crx')
chrome_options.add_extension('autoplaystopper.crx')

total_points = "0"

# Chrome Driver
browser = webdriver.Chrome(options=chrome_options)
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to KingdomLikes Bot")
print("[+] Starting...")
print("[+] Importing Modules...")

# Google Account
print("[+] Logging in Google...")
browser.get("https://www.youtube.com/account")
browser.find_element_by_xpath("//*[@id='identifierId']").send_keys(google_email)
browser.find_element_by_xpath("//*[@id='identifierNext']").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(google_password)
browser.find_element_by_xpath("//*[@id='passwordNext']").click()
time.sleep(5)

# Instagram
print("[+] Loggin in Instagram...")
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(5)
browser.find_element_by_name("username").send_keys(instagram_username)
browser.find_element_by_name("password").send_keys(instagram_password)
browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(5)

# KingdomLikes
print("[+] Loggin in KingdomLikes...")
browser.get("http://kingdomlikes.com")
browser.find_element_by_xpath("//*[@id='formlogin']/div[1]/input[1]").send_keys(kingdomlikes_email)
browser.find_element_by_xpath("//*[@id='formlogin']/div[1]/input[2]").send_keys(kingdomlikes_password)
browser.find_element_by_xpath("//*[@id='formlogin']/div[1]/input[3]").click()

# YouTube Views
print("[+] Starting YouTube Views...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/youtube-views")
    time.sleep(5)
    views_timer = browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/h5").text
    views_timer = views_timer.replace("Must play for 0:00/", "")
    views_timer = views_timer.replace(" minutes", "")
    views_seconds = int((sum(int(x) * 60 ** i for i,x in enumerate(reversed(views_timer.split(":"))))))
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    time.sleep(views_seconds + 30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

# YouTube likes
print("[+] Starting YouTube Likes...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/youtube-likes")
    window_before = browser.window_handles[0]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a").click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(window_before)
    time.sleep(30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

# YouTube Dislikes
print("[+] Starting YouTube Dislikes...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/youtube-dis-likes")
    window_before = browser.window_handles[0]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[2]").click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(window_before)
    time.sleep(30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

# YouTube Subscribers
print("[+] Starting YouTube Subscribers...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/youtube-subscribe")
    window_before = browser.window_handles[0]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='subscribe-button']").click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(window_before)
    time.sleep(30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Instagram Followers
print("[+] Starting Instagram Followers...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/instagram-followers")
    window_before = browser.window_handles[0]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(window_before)
    time.sleep(30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Instagram Followers
print("[+] Starting Instagram Followers...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/instagram-followers")
    window_before = browser.window_handles[0]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(window_before)
    time.sleep(30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Instagram likes
print("[+] Starting Instagram Likes...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/instagram-likes")
    window_before = browser.window_handles[0]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/article/div[2]/section[1]/span[1]/button").click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(window_before)
    time.sleep(30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Web Traffic
print("[+] Starting Web Traffic...")
for x in range(0, int(actions_per_module)):
    browser.get("https://kingdomlikes.com/free_points/web-traffic")
    time.sleep(5)
    views_timer = browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/h5").text
    views_timer = views_timer.replace("Must play for 0:00/", "")
    views_timer = views_timer.replace(" minutes", "")
    views_seconds = int((sum(int(x) * 60 ** i for i,x in enumerate(reversed(views_timer.split(":"))))))
    browser.find_element_by_xpath("//*[@id='idpage5']/div/div[5]/button").click()
    time.sleep(views_seconds + 30)
    points = browser.find_element_by_class_name("redfont").text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

print("Total Points Earned: " + total_points)
