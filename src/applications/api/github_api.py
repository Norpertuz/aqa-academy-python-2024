import requests


class GitHubAPIClient:

    def __init__(self) -> None:
        pass

    def search_repos(self, repo_name):
        r = requests.get(
            url=f"https://api.github.com/search/repositories?q={repo_name}",
        )

        data = r.json()
        return data["total_count"], r

    def get_repo_info(self, owner, repo_name):
        r = requests.get(
            url=f"https://api.github.com/repos/{owner}/{repo_name}",
        )

        data = r.json()
        return data["watchers_count"], r
