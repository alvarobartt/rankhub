#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome
# See LICENSE for details.

import requests
import pandas as pd

import math
import time
import datetime
import operator

from investpy.user_agent import get_random


class Rankhub:
    def __init__(self, oauth_token):
        self.oauth_token = oauth_token

    def _city_ranking(self, city):
        header = {
            'Authorization': 'token ' + self.oauth_token,
            'User-Agent': get_random(),
        }

        url = 'https://api.github.com/search/users?q=location:' + city

        req = requests.get(url=url, headers=header)

        pages = math.ceil(req.json()['total_count'] / 30)

        total_users = list()

        for page in range(1, pages + 1):
            url = 'https://api.github.com/search/users?q=location:' + city + '&page=' + str(page)

            header = {
                'Authorization': 'token ' + self.oauth_token,
                'User-Agent': get_random(),
            }

            req = requests.get(url=url, headers=header)

            users = req.json()['items']

            for user in users:
                username = user['login']
                username_url = user['html_url']
                avatar_url = user['avatar_url']

                public_contributions = 0
                languages = dict()

                repo_page = 1
                repo_flag = False

                while repo_flag is False:
                    url = user['repos_url'] + '?page=' + str(repo_page)

                    header = {
                        'Authorization': 'token ' + self.oauth_token,
                        'User-Agent': get_random(),
                    }

                    req = requests.get(url=url, headers=header)
                    status_code = req.status_code

                    while status_code != 200:
                        time.sleep(1)
                        req = requests.get(url=url, headers=header)
                        status_code = req.status_code

                    repos = req.json()

                    if len(repos) != 30:
                        repo_flag = True
                    else:
                        repo_page += 1

                    for repo in repos:
                        flag = False

                        while flag is False:
                            full_name = repo['full_name']

                            url = 'https://api.github.com/repos/' + full_name + '/stats/contributors'

                            header = {
                                'Authorization': 'token ' + self.oauth_token,
                                'User-Agent': get_random(),
                            }

                            req = requests.get(url=url, headers=header)

                            if req.status_code in [204, 403]:
                                break
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

        return df
