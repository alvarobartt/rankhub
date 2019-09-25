#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome
# See LICENSE for details.


def ranking_to_json(ranking):
    json_ranking = ranking.to_json(orient='index')

    return json_ranking


def ranking_to_md(ranking):
    rows_desc = '| Rank | User | Avatar | Location | Public Contributions | Most Used Language | Used Languages |\n' \
                '|------|------|--------|----------|----------------------|--------------------|----------------|\n'

    rows_ranks = ''

    for index, row in ranking.iterrows():
        image_html = "<img src='" + str(row['avatar_url']) + "&s=64' width='64'>"

        row_rank = '| ' + str(index) + \
                   ' | [' + str(row['username']) + '](' + str(row['username_url']) + ')' + \
                   ' | ' + str(image_html) + \
                   ' | ' + str(row['location']) + \
                   ' | ' + str(row['public_contributions']) + \
                   ' | ' + str(row['top_language']) + \
                   ' | ' + str(row['used_languages']) + ' |\n'

        rows_ranks += row_rank

    md_ranking = rows_desc + rows_ranks

    return md_ranking
