#!/usr/bin/env python3
"""
Client module for GithubOrgClient.
"""

import requests


def get_json(url):
    """Helper function to fetch JSON data from a URL."""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """A client to interact with the GitHub API for organizations."""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Fetch and return the organization data from GitHub API."""
        url = self.ORG_URL.format(org=self.org_name)
        return get_json(url)
