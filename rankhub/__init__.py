#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome
# See LICENSE for details.

__author__ = 'Alvaro Bartolome <alvarob96@usal.es>'
__version__ = '0.0.1'

import requests
import math
import datetime


OAUTH_TOKEN = '8b0a47622eaa278f0aefc7b32629cab034f58604'

if __name__ == '__main__':
    header = {
        'Authorization': 'token ' + OAUTH_TOKEN
    }

    url = 'https://api.github.com/search/users?q=location:salamanca'

    req = requests.get(url=url,
                       headers=header)

    pages = math.ceil(req.json()['total_count'] / 30)

    total_users = list()

    for page in range(1, pages + 1):
        url = 'https://api.github.com/search/users?q=location:salamanca&page=' + str(page)

        req = requests.get(url=url,
                           headers=header)

        users = req.json()['items']

        for user in users:
            obj = {
                'username': user['login'],
                'contributions': None,
                'languages': None
            }

            contributions = 0
            languages = set()

            url = user['repos_url']

            req = requests.get(url=url,
                               headers=header)

            repos = req.json()

            for repo in repos:
                flag = False

                while flag is False:
                    full_name = repo['full_name']

                    url = 'https://api.github.com/repos/' + full_name + '/stats/contributors'

                    req = requests.get(url=url,
                                       headers=header)

                    if req.status_code == 204:
                        flag = True
                    elif req.status_code != 200:
                        continue
                    else:
                        if req.json():
                            weeks = req.json()[0]['weeks']

                            for week in weeks:
                                date_value = datetime.datetime.fromtimestamp(week['w'])

                                if date_value.year == 2019:
                                    contributions += int(week['c'])

                            languages.add(repo['language'])
                    flag = True

            obj['contributions'] = contributions
            obj['languages'] = list(languages)

            print(obj)

            total_users.append(obj)
