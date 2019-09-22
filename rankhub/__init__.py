#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome
# See LICENSE for details.

__author__ = 'Alvaro Bartolome <alvarob96@usal.es>'
__version__ = '0.0.1'

import requests
import pandas as pd

import math
import datetime
import operator


OAUTH_TOKEN = 'YOUR_GITHUB_OAUTH_TOKEN'

if __name__ == '__main__':
    header = {
        'Authorization': 'token ' + OAUTH_TOKEN
    }

    url = 'https://api.github.com/search/users?q=location:salamanca'

    req = requests.get(url=url, headers=header)

    pages = math.ceil(req.json()['total_count'] / 30)

    total_users = list()

    for page in range(1, pages + 1):
        url = 'https://api.github.com/search/users?q=location:salamanca&page=' + str(page)

        req = requests.get(url=url, headers=header)

        users = req.json()['items']

        for user in users:
            username = user['login']
            username_url = user['html_url']
            avatar_url = user['avatar_url']

            public_contributions = 0
            languages = dict()

            url = user['repos_url']

            req = requests.get(url=url, headers=header)

            repos = req.json()

            for repo in repos:
                flag = False

                while flag is False:
                    full_name = repo['full_name']

                    url = 'https://api.github.com/repos/' + full_name + '/stats/contributors'

                    req = requests.get(url=url, headers=header)

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
                                    public_contributions += int(week['c'])

                            if repo['language'] is not None:
                                if repo['language'] in languages:
                                    languages[repo['language']] += 1
                                else:
                                    languages[repo['language']] = 1
                    flag = True

            if bool(languages) is False:
                top_language = ''

                used_languages = ''
            else:
                top_language = max(languages.items(), key=operator.itemgetter(1))[0]

                used_languages = ', '.join(languages.keys())

            obj = {
                'username': username,
                'username_url': username_url,
                'avatar_url': avatar_url,
                'public_contributions': public_contributions,
                'top_language': top_language,
                'used_languages': used_languages,
            }

            total_users.append(obj)

    df = pd.DataFrame(total_users)

    df.sort_values(by='public_contributions', ascending=False, inplace=True)

    ranks = [value for value in range(1, len(df) + 1)]

    df['ranks'] = ranks

    df.set_index('ranks', inplace=True)

    rows_desc = '| Rank | User | Avatar | Public Contributions | Most Used Language | Used Languages |\n' \
                '|------|------|--------|----------------------|--------------------|----------------|\n'

    lines = ''

    for index, row in df.iterrows():
        image_html = "<img src='" + str(row['avatar_url']) + "&s=64' width='64'>"

        line = '| ' + str(index) + \
               ' | [' + str(row['username']) + '](' + str(row['username_url']) + ')' + \
               ' | ' + str(image_html) + \
               ' | ' + str(row['public_contributions']) + \
               ' | ' + str(row['top_language']) + \
               ' | ' + str(row['used_languages']) + ' |\n'

        lines += line

    with open('salamanca/salamanca.md', 'w') as result:
        result.write(rows_desc)
        result.close()

    with open('salamanca/salamanca.md', 'a') as result:
        result.write(lines)
        result.close()

    with open('salamanca/salamanca.json', 'w') as result:
        df.to_json(result, orient='index')
        result.close()
