import requests


class GitHubTrendingRepos:
    """
    Class to get trending repositories on GitHub using the GitHub API.
    """

    def __init__(self):
        """
        Initializes the class.
        """
        self.base_url = "https://api.github.com/search/repositories"

    def get_trending_repos(self, language):
        """
        Gets the trending repositories for the specified language.
        """
        params = {
            'q': f'language:{language}',
            'sort': 'stars',
            'order': 'desc'
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data['items'][:10]
        else:
            return f"Error getting trending repositories: {data['message']}"

    def generate_report(self, language):
        """
        Generates a Markdown report with the trending repositories.
        """
        repos = self.get_trending_repos(language)

        report = f"# Trending Repositories in {language}\n"
        for i, repo in enumerate(repos, start=1):
            report += f"\n## {i}. {repo['name']}\n"
            report += f"- Description: {repo['description']}\n"
            report += f"- URL: {repo['html_url']}\n"
            report += f"- Stars: {repo['stargazers_count']}\n"

        return report


def main():
    """
    Main function to run the script.
    """
    gt = GitHubTrendingRepos()
    report = gt.generate_report('Python')
    print(report)


if __name__ == "__main__":
    main()
