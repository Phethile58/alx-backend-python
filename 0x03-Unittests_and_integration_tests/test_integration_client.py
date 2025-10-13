#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
import requests

from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class by mocking requests.get"""
        cls.get_patcher = patch('requests.get')

        # Start the patcher and get the mock object
        mock_get = cls.get_patcher.start()

        # Define behavior for requests.get(...).json()
        def side_effect(url):
            if url.endswith("orgs/google"):
                return MockResponse(cls.org_payload)
            elif url.endswith("orgs/google/repos"):
                return MockResponse(cls.repos_payload)
            return MockResponse(None)

        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns expected list of repos"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license filtering"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


# A simple mock response to simulate requests.get().json()
class MockResponse:
    """Mock requests.Response object"""
    def __init__(self, json_data):
        self._json_data = json_data

    def json(self):
        return self._json_data


if __name__ == "__main__":
    unittest.main()
