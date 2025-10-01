#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient.public_repos.
"""

import unittest
from parameterized import parameterized_class
from unittest.mock import patch
from client import GithubOrgClient
import fixtures


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (
            fixtures.org_payload,
            fixtures.repos_payload,
            fixtures.expected_repos,
            fixtures.apache2_repos,
        )
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get to return predefined fixture payloads."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            class MockResponse:
                def __init__(self, payload):
                    self.payload = payload

                def json(self):
                    return self.payload

            if url.endswith("/orgs/google"):
                return MockResponse(cls.org_payload)
            elif url == cls.org_payload.get("repos_url"):
                return MockResponse(cls.repos_payload)
            return MockResponse(None)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected repo list."""
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by license."""
        client = GithubOrgClient(self.org_payload["login"])
        repos = client.public_repos()
        filtered = [
            repo for repo in self.repos_payload
            if repo.get("license", {}).get("key") == "apache-2.0"
        ]
        self.assertEqual(filtered, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
