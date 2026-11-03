# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import unittest
import warnings

from fastapi.testclient import TestClient

from app import app


class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.addCleanup(self.client.close)

    def test_index_renders_form_and_static_link(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        self.assertIn('action="http://testserver/hello"', response.text)
        self.assertIn(
            'href="http://testserver/static/bootstrap/css/bootstrap.min.css"',
            response.text,
        )

    def test_index_supports_head(self):
        response = self.client.head("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")

    def test_hello_renders_name_and_home_link(self):
        response = self.client.post("/hello", data={"name": "Seattle"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello Seattle", response.text)
        self.assertIn('href="http://testserver/"', response.text)

    def test_hello_escapes_user_input(self):
        response = self.client.post(
            "/hello", data={"name": "<script>alert(1)</script>"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", response.text)
        self.assertNotIn("<script>", response.text)

    def test_missing_or_empty_name_redirects_home(self):
        for data in ({}, {"name": ""}):
            with self.subTest(data=data):
                response = self.client.post(
                    "/hello", data=data, follow_redirects=False
                )
                self.assertEqual(response.status_code, 302)
                self.assertEqual(response.headers["location"], "/")
                home = self.client.get(response.headers["location"])
                self.assertEqual(home.status_code, 200)

    def test_multipart_form(self):
        response = self.client.post("/hello", files={"name": (None, "Seattle")})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello Seattle", response.text)

    def test_whitespace_name_is_preserved(self):
        response = self.client.post("/hello", data={"name": " "})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello  </h1>", response.text)

    def test_api_documentation(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error", UserWarning)
            response = self.client.get("/openapi.json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("get", response.json()["paths"]["/"])
        self.assertIn("post", response.json()["paths"]["/hello"])
        self.assertEqual(self.client.get("/docs").status_code, 200)

    def test_static_css_is_served(self):
        response = self.client.get("/static/bootstrap/css/bootstrap.min.css")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/css", response.headers["content-type"])
        self.assertIn("Bootstrap", response.text)

    def test_hello_only_accepts_post(self):
        self.assertEqual(self.client.get("/hello").status_code, 405)

    def test_unknown_route_returns_not_found(self):
        self.assertEqual(self.client.get("/missing").status_code, 404)


if __name__ == "__main__":
    unittest.main()
