#!/usr/bin/env python3
"""
Client module for GithubOrgClient.
"""

import requests


def get_json(url: str) -> dict:
    """
    Helper function to fetch JSON data from a URL.

    Args:
        url: The URL to fetch JSON data from.

    Returns:
        A dictionary of the JSON response.
    """
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """
    A client to interact with the GitHub API for organizations.
    """

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """
        Initialize GithubOrgClient.

        Args:
            org_name: Name of the GitHub organization.
        """
        self.org_name = org_name

    @property
    def org(self) -> dict:
        """
        Fetch and return the organization data from GitHub API.

        Returns:
            Dictionary containing organization data.
        """
        url = self.ORG_URL.format(org=self.org_name)
        return get_json(url)

    @property
    def _public_repos_url(self) -> str:
        """
        Return the URL for the organization's public repositories.

        Returns:
            URL string for public repositories.
        """
        return self.org.get("repos_url", "")

    def public_repos(self, license: str = None) -> list[str]:
        """
        Return the list of public repository names for the organization.

        Args:
            license: Optional license key to filter repositories.

        Returns:
            A list of repository names.
        """
        repos_url = self._public_repos_url
        repos_data = get_json(repos_url)

        if license is None:
            return [repo["name"] for repo in repos_data]

        return [
            repo["name"]
            for repo in repos_data
            if self.has_license(repo, license)
        ]

    def has_license(self, repo: dict, license_key: str) -> bool:
        """
        Check if a repository has a specific license.

        Args:
            repo: A dictionary of repository data.
            license_key: The license key to check for.

        Returns:
            True if license matches, False otherwise.
        """
        return repo.get("license") and repo["license"].get("key") == license_key
