import datetime
import os
import unittest

from webapp import template_utils


class TemplateUtilsTest(unittest.TestCase):
    def test_truncate_chars(self):
        value = "123456789"
        length = 5
        expected_result = "1234&hellip;"

        result = template_utils.truncate_chars(value, length)
        self.assertEqual(expected_result, result)

        value = "1234 56789"
        length = 5
        expected_result = "1234&hellip;"

        result = template_utils.truncate_chars(value, length)
        self.assertEqual(expected_result, result)

    def test_format_date(self):
        date = "2020-12-12"
        expected_result = "12 December 2020"

        result = template_utils.format_date(date)
        self.assertEqual(expected_result, result)

    def test_replace_admin(self):
        url = "https://admin.insights.ubuntu.com/test-url/123"
        expected_result = "https://blog.ubuntu.com/test-url/123"

        result = template_utils.replace_admin(url)
        self.assertEqual(expected_result, result)

    def test_versioned_static(self):
        url_for_non_exising_file = "123"
        expected_result = "/static/123"
        result = template_utils.versioned_static(url_for_non_exising_file)
        self.assertEqual(expected_result, result)

        exising_file_name = "test123"
        directory = "static"

        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(f"{directory}/{exising_file_name}", "w") as file:
            file.write("hi")

        md5_sum_of_test_file = "49f68a5c8493ec2c0bf489821c21fc3b"
        shortened_md5_sum = md5_sum_of_test_file[:7]

        expected_result = (
            f"/{directory}/{exising_file_name}?v={shortened_md5_sum}"
        )

        result = template_utils.versioned_static(exising_file_name)

        self.assertEqual(result, expected_result)

        os.remove(f"{directory}/{exising_file_name}")

    def test_get_year(self):
        expected_result = datetime.datetime.now().year
        result = template_utils.get_year()

        self.assertEqual(expected_result, result)
