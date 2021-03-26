from django.test import TestCase
from django.http import request
from urlshortener.models import ShortUrl

# Create your tests here.
class ShortUrlTestCase(TestCase):
    test_short_url = 'saranen'
    test_url = 'https://saranen.fi'

    # Create new row in your test database
    def setUp(self):
        test_url = ShortUrl.objects.create(url=self.test_url, slug=self.test_short_url)
        test_url.save()

    def test_redirect(self):
        response = self.client.get('/saranen')
        self.assertRedirects(response, self.test_url, status_code=302, fetch_redirect_response=False)