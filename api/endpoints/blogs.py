"""The item classification blueprint implementation."""

import random
from flask import Blueprint, jsonify, request
import mysql.connector
from api.config import db_database_name, db_password, db_private_ip, db_username

blogs_api = Blueprint("blogs_api", __name__)

# Blogs routes
@blogs_api.route("/blogs", methods=["GET"])
def get_tasks():
    """Retrieves the list of blog posts from the database for given categories.

    Returns:
        A JSON data of the list of blog posts that match given categories.
    """
    db = mysql.connector.connect(user=db_username,
                                 host=db_private_ip,
                                 password=db_password,
                                 database=db_database_name)
    cur = db.cursor()

    default = ["", "", "", "", "", "", ""]
    first_category = (request.args.get('first_category'))
    second_category = (request.args.get('second_category'))

    if first_category is None or first_category == "":
        return jsonify("Please ensure that the 'first_category' parameter is populated")

    if second_category is None or second_category == "":
        second_category = first_category

    potential_blogs_first_category = get_blogs_for_category(cur, first_category)
    potential_blogs_second_category = get_blogs_for_category(cur, second_category)

    try:
        rand_choice_1 = random.choice(potential_blogs_first_category)
    except: #pylint: disable=bare-except
        rand_choice_1 = default

    safe_iterator = 0

    try:
        rand_choice_2 = random.choice(potential_blogs_second_category)

        while (rand_choice_2[0] == rand_choice_1[0] and safe_iterator < 10):
            rand_choice_2 = random.choice(potential_blogs_second_category)
            safe_iterator += 1

        if safe_iterator == 10:
            rand_choice_2 = default
    except: #pylint: disable=bare-except
        rand_choice_2 = default

    blogs = [
        {
            "title": rand_choice_1[0],
            "description": rand_choice_1[1],
            "link": rand_choice_1[2],
            "published_date": rand_choice_1[3],
            "image": rand_choice_1[4],
            "categories": (rand_choice_1[5]).replace("_", " ").title().split(","),
            "author": rand_choice_1[6]
        },
        {
            "title": rand_choice_2[0],
            "description": rand_choice_2[1],
            "link": rand_choice_2[2],
            "published_date": rand_choice_2[3],
            "image": rand_choice_2[4],
            "categories": (rand_choice_2[5]).replace("_", " ").title().split(","),
            "author": rand_choice_2[6]
        }]

    cur.close()
    db.close()

    return jsonify(blogs)

# Helper functions
def get_mapped_categories(category):
    """Creates a mapping between the model's item category mappings against blog post tags
    and returns the mapping of a given category.

    Args:
        category: The category to retrieve its mapping with the model.

    Returns:
        The corresponding model mapping of a given category.
    """
    mapping = {
        'Communication': ['Communication', 'Remote_teams', 'Difficult_conversations', 'Feedback', \
                'Productive_meetings', 'Management_skills', \
                'New_manager', 'Senior_manager', 'Change_management'],
        'Growth': ['Team_tools', 'New_manager', 'Senior_manager', 'Growth'],
        'Motivation': ['Employee_motivation', 'Employee_engagement'],
        'Work': ['Time_management', 'Accountability', 'Building_trust', 'Work']
    }

    return mapping[category]

def get_blogs_for_category(cur, category):
    """Retrieves the blog post information based on a given category.

    Args:
        cur: The database cursor
        category: The category to filter the blog posts with.

    Returns:
        The list of blogs that match a given category.
    """
    categories = get_mapped_categories(category)
    or_like_string = " OR ".join([f"blogs.categories like '%{category}%'" for category in categories]) #pylint: disable=line-too-long,syntax-error
    sql_string = f"select title, description, link, published_date, image, categories, author from blogs where {or_like_string}" #pylint: disable=line-too-long

    cur.execute(sql_string)
    blogs = cur.fetchall()

    return blogs
