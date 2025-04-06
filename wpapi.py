#WordPress API procedure 1) get application password from WP dashboard. Users|profile|application passwords  also Need APP name.
import requests
import base64
import json

wordpress_user = "rogeridaho"
wordpress_password = "24 char password from wp dashboard"
wordpress_credentials = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {'Authorization': 'Basic' + wordpress_token.decode('utf-8')}

# sample API url: https:mychauffe.com/wp-json/wp/v2/posts
api_url = 'https://www.mychauffe.com/wp-json/wp/v2/posts'
response = requests.get(api_url)
response_json = response.json()

# https://www.mychauffe.com/wp-json/wp/v2/posts?page=2&per_page=100 - sample URL parameters

# see parseRequestDotGetHeader.py for header examples

# **************************************************************************************
#                                       Django tasks:
#   - setup development environment, create placeholder site with necessary features:  user accounts, ecommerce in place, custom
#      pages by user/user status.
#
#   - create pages for - general public, apply to be an accredited investor seminar attendees, store page with specific items,
#
#   Create class for User Account holders as:
#   - Public/no account - publicly accessible for browsing
#   - Public with account - general pages for interested parties.  Links to Indiegogo for 100/10000 partial investors,
#      apply button and info pages for potential accredited investors.
#   - application pages for accredited investors, SEND button
#
#   - User account page and store/product page for accepted Accredited Investors including Seminar Product/shooping cart in store
#   - User account page and seminar details page for accepted and registered Accredited Investors
#   - User account page for pre-LP Accredited Investors, with store/product including INVEST/LP product in store
#   - LP - accepted as accredited investor, User Account page, populated Wallet, info for LPs page.
#
#   - Partial100, Partial10000 - require access to User Account and Wallet pages. Invest via Indiegogo, MyCHAUFFE.com
#      account and CHAUFFEcoins are created by corporate and MyCHAUFFE.com login details are emailed. Need a script to
#      automate these procedures possibly via Admin level web page...?
#   - need ability to convert User account privileges (i.e. access to specific pages) based upon status/account type.