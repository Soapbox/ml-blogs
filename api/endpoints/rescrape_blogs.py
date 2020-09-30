"""The rescraping endpoints for blog posts."""

import os
from flask import Blueprint, jsonify, request

rescrape_blogs_api = Blueprint("rescrape_blogs_api", __name__)

# Rescrape blogs routes
@rescrape_blogs_api.route("/rescrape_blogs", methods=["GET"])
def get_tasks():
    """Retrieves the list of blog posts that exist in the website.

    Returns:
        A JSON object indicating the status of the rescraping process.
    """
    req_actionable = request.args.get('only_actionable')
    if req_actionable:
        req_actionable = req_actionable.lower()
    if req_actionable == "true":
        os.system("python3 api/get_blogs.py actionable")
    else:
        os.system("python3 api/get_blogs.py")

    return jsonify({"Message": "Successfully re-scraped the blog"})
