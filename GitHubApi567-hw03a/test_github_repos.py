import unittest
from unittest import mock

from github_repos import get_repositories


class TestGitHubRepos(unittest.TestCase):
    @mock.patch("requests.get")
    def test_two_repositories(self, mocked_get):
        mocked_get.side_effect = [
            mock.Mock(text='[{"name": "Triangle567"}, {"name": "Square567"}]'),
            mock.Mock(text='[{"sha": "a"}, {"sha": "b"}]'),
            mock.Mock(text='[{"sha": "c"}]'),
        ]

        self.assertEqual(
            get_repositories("John567"),
            [
                "Repo: Triangle567 Number of commits: 2",
                "Repo: Square567 Number of commits: 1",
            ],
        )

    @mock.patch("requests.get")
    def test_no_repositories(self, mocked_get):
        mocked_get.return_value = mock.Mock(text="[]")

        self.assertEqual(get_repositories("John567"), [])


if __name__ == "__main__":
    unittest.main()
