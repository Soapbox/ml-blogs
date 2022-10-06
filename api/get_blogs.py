"""The scraper used for fetching Soapbox blog posts based on categories."""

import urllib
import sys
from xml.etree.ElementTree import fromstring, ElementTree
import mysql.connector
import requests
from bs4 import BeautifulSoup
from config import db_username, db_private_ip, db_password, db_database_name #pylint: disable=no-name-in-module

db = mysql.connector.connect(user=db_username,
                             host=db_private_ip,
                             password=db_password,
                             database=db_database_name)

BASE_URL = "https://soapboxhq.com/blog/feed?paged="
req_actionable = False

cur = db.cursor()
if len(sys.argv) > 1:
    if sys.argv[1] == "actionable":
        req_actionable = True

def getvalueofnode(node):
    """Gets the value of the node for a given node.

    Args:
        node: The node to retrieve its value from.

    Returns:
        The string from the node if it exists, or None.
    """
    return node.text if node is not None else ""

def blog_data():
    """Retrieves the blog data by scraping the blog posts and inserting them into the database."""
    sql_string_1 = "CREATE TABLE IF NOT EXISTS blogs (id int not null auto_increment, title text, description text, link text, published_date text, image text, categories text, author text, primary key(id))" #pylint: disable=line-too-long
    sql_string_2 = "DELETE FROM blogs"

    cur.execute(sql_string_1)
    cur.execute(sql_string_2)

    db.commit()
    print("Collecting blogs, please wait...")

    i = 1
    while True:
        url = BASE_URL+str(i)
        try:
            req = urllib.request.Request(url, headers={'User-Agent': "Hypercontext Blog Bot"})
            current_file = urllib.request.urlopen(req)
        except Exception as e:
            print(e)
            break

        data = current_file.read()
        current_file.close()
        parsedXML = ElementTree(fromstring(data))
        root = parsedXML.getroot()
        for node in root.iter("item"):
            link = getvalueofnode(node.find("link"))
            categories_list = []
            for cat in node.iter("category"):
                categories_list.append(getvalueofnode(cat).replace(" ", "_").capitalize())
            categories = ",".join(categories_list)
            title, description, published_date, image, author, actionable = bsoup_data(link)

            title = title.replace('"', "'")
            description = description.replace('"', "'")

            if not req_actionable:
                actionable = True
            if actionable:
                sql_string_3 = 'INSERT INTO blogs(title, description, link, published_date, image, categories, author) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (title, description, link, published_date, image, categories, author) #pylint: disable=line-too-long
                cur.execute(sql_string_3)
                db.commit()
        i += 1

    print("Completed fetching the blogs")

def bsoup_data(blog_link):
    """Parses the given link and retrieve the necessary information to store in the database.

    Args:
        blog_link: The URL for the blog post.

    Returns:
        The tuple of necessary information about the blog post.
    """
    print('Fetching', blog_link)
    page = requests.get(blog_link)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("meta", property="og:title")
    title = remove_emoji(title["content"]) if title else ""
    description = soup.find("meta", property="og:description")
    description = remove_emoji(description["content"]) if description else ""
    published_date = soup.find("meta", property="article:published_time")["content"]
    image = soup.find("meta", property="og:image")
    image = image["content"] if image else ""
    author = soup.find("meta", property="author")
    author = author["content"] if author else ""
    actionable = soup.find("meta", property="actionable") is not None

    return title, description, published_date, image, author, actionable

def remove_emoji(input_string):
    """Removes any emoji characters in a string.

    Args:
        input_string: The string to filter emoji characters with.

    Returns:
        The filtered string with no emoji characters.
    """
    return input_string.encode('ascii', 'ignore').decode('ascii')


if __name__ == '__main__':
    blog_data()
