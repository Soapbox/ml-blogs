"""The blog endpoints unit test."""

import unittest
from test.super_test_case import SuperTestCase

class BlogsTests(SuperTestCase):
    def __init__(self, *args, **kwargs):
        super(BlogsTests, self).__init__(*args, **kwargs)

        self.blogs_endpoint = "/blogs"

    def tearDown(self):
        """Removes the temporary database."""
        self.session.close()

    def test_blog_with_categories_should_return_status_2000(self):

        request_data = {"first_category": "Work", "second_category": "Communication"}

        response, status_code = self.generate_payload(
            None,
            self.blogs_endpoint + "?first_category=Work&second_category=Communication",
            self.http_method_get
        )

        self.assertEqual(status_code, 200)
        self.assertIsNotNone(response[0]["author"])
        self.assertIsNotNone(response[0]["categories"])
        self.assertIsNotNone(response[0]["description"])
        self.assertIsNotNone(response[0]["image"])
        self.assertIsNotNone(response[0]["link"])
        self.assertIsNotNone(response[0]["published_date"])
        self.assertIsNotNone(response[0]["title"])


if __name__ == "__main__":
    unittest.main()
