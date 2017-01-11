import requests
from datetime import datetime,timedelta


def get_trending_repositories(days_amount, top_amount):
    week_ago = datetime.date(datetime.today() - timedelta(days_amount))
    payload = {'q': 'created:>%s' % week_ago, 'sort': 'stars', 'per_page': top_amount}
    response = requests.get("https://api.github.com/search/repositories", params=payload)
    return response.json()["items"]


def print_response(response):
    for count, repository in enumerate(response, start=1):
        print('%s) Name of repository: "%s",' % (count, repository['name']),
              'number of stars: %s, ' % (repository['stargazers_count']),
              'number of open issues: %s, ' % (repository['open_issues']),
              'link to repository: %s' % (repository['html_url']))

if __name__ == '__main__':
    days_amount = 7
    top_amount = 20
    response = get_trending_repositories(days_amount, top_amount)
    print_response(response)