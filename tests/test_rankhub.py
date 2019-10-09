#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome
# See LICENSE for details.

import pytest

import os

from rankhub.github import Rankhub
from rankhub.ranking import ranking_to_md, ranking_to_json


def test_rankhub():
    ranks = Rankhub(oauth_token=os.environ['oauth_token'])

    df = ranks._city_ranking(city='uuu')

    ranking_to_md(ranking=df)
    ranking_to_json(ranking=df)


if __name__ == '__main__':
    test_rankhub()
