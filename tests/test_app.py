import unittest
from PIL import Image
from io import BytesIO
from app import app
import re


class TestResizer(unittest.TestCase):
    def setUp(self):  # mock client
        app.config['TESTING'] = True
        self.app = app
        self.client = self.app.test_client()

    def test_index_redirection(self):  # verify if redirection in index works
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.request.path, '/resizer')

    def test_resizer_status(self):  # verify request status
        response = self.client.post('/resizer',
                           data=dict(length='256',
                                     width='256'))
        self.assertEqual(response.status_code, 200)

    def test_resize_width_and_height(self):  # mock post request
        response = self.client.post('/resizer',
                           data=dict(length='256',
                                     width='256'))

        pat = re.compile(rb'<img [^>]*src="([^"]+)')
        img_url = pat.findall(response.data)
        img = Image.open(BytesIO(img_url[0]))
        self.assertEqual(img.width, 256)
        self.assertEqual(img.height, 256)


if __name__ == '__main__':
    unittest.main()