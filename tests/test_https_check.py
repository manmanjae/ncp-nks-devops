import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from tools.https_check import check_url


class TestCheckUrl(unittest.TestCase):

    @patch("tools.https_check.urlopen")
    def test_success_returns_zero(self, mock_urlopen):
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.status = 200

        result = check_url("https://example.com/healthz")

        self.assertEqual(result, 0)
        mock_urlopen.assert_called_once_with(
            "https://example.com/healthz",
            timeout=5,
        )

    @patch("tools.https_check.urlopen")
    def test_http_error_returns_one(self, mock_urlopen):
        mock_urlopen.side_effect = HTTPError(
            url="https://example.com/not-found",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )

        result = check_url("https://example.com/not-found")

        self.assertEqual(result, 1)

    @patch("tools.https_check.urlopen")
    def test_connection_error_returns_one(self, mock_urlopen):
        mock_urlopen.side_effect = URLError("DNS lookup failed")

        result = check_url("https://example.invalid/healthz")

        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
