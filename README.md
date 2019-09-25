# rankhub - is a Python package to generate GitHub users rankings

[![Python Version](https://img.shields.io/pypi/pyversions/rankhub.svg)](https://pypi.org/project/rankhub/)
[![PyPi Version](https://img.shields.io/pypi/v/rankhub.svg)](https://pypi.org/project/rankhub/)
[![Package Status](https://img.shields.io/pypi/status/rankhub.svg)](https://pypi.org/project/rankhub/)
[![Build Status](https://img.shields.io/travis/alvarob96/rankhub/master.svg?label=Travis%20CI&logo=travis&logoColor=white)](https://travis-ci.org/alvarob96/rankhub)
[![codecov](https://codecov.io/gh/alvarob96/rankhub/branch/master/graph/badge.svg)](https://codecov.io/gh/alvarob96/rankhub)

## Introduction

This project is intended to be a Python package in order to retrieve data from GitHub using 
its public API with an application token. Currently, as this project is under-development,
a simple use-case is proposed in order to retrieve data from Salamanca (Spain) GitHub users 
as to generate a ranking with the most active users in public repositories created by them 
throughout 2019. This feature will be updated in order to retrieve also the stats form the
repositories were the user has contributed to, since some users have a lot of contributions on
public repositories created by an organization or by another user.

## Top GitHub Users from Salamanca (Spain) sorted by Public Contributions throughout 2019

As already mentioned, this ranking contains all the GitHub users from Salamanca sorted by the
amount of public contributions just between 01/01/2019 until the current date 21/09/2019.

| Rank | User | Avatar | Public Contributions | Most Used Language | Used Languages |
|------|------|--------|----------------------|--------------------|----------------|
| 1 | [Emirodgar](https://github.com/Emirodgar) | <img src='https://avatars0.githubusercontent.com/u/4302127?v=4&s=64' width='64'> | 2188 | HTML | HTML, JavaScript, CSS |
| 2 | [tomhendra](https://github.com/tomhendra) | <img src='https://avatars1.githubusercontent.com/u/32566274?v=4&s=64' width='64'> | 853 | JavaScript | JavaScript, CSS, HTML |
| 3 | [alvarob96](https://github.com/alvarob96) | <img src='https://avatars3.githubusercontent.com/u/36760800?v=4&s=64' width='64'> | 302 | Python | Jupyter Notebook, Python |
| 4 | [JParzival](https://github.com/JParzival) | <img src='https://avatars3.githubusercontent.com/u/33935947?v=4&s=64' width='64'> | 230 | Jupyter Notebook | PHP, JavaScript, Python, Jupyter Notebook, Java, TypeScript, R, HTML |
| 5 | [francaguilar](https://github.com/francaguilar) | <img src='https://avatars1.githubusercontent.com/u/11558278?v=4&s=64' width='64'> | 203 | Python | Swift, Eagle, JavaScript, C++, Assembly, Rust, C#, HTML, Common Lisp, Objective-C, PHP, OpenSCAD, Java, Python, Makefile, CSS, C, Ruby, Shell, TeX, Prolog, Jupyter Notebook |

This is just the leading Top 5 GitHub users from the generated ranking, so the complete ranking 
can be found in [spain/salamanca](https://github.com/alvarob96/rankhub/blob/master/spain/salamanca) in both
JSON and Markdown format.

Note that both the ranking and the package will be updated in order to create a 2019 ranking resume
at the end of the year! So make sure to watch and star the repo in order to get tuned for updates!

## Rankings

Currently as explained above, as the use case is the ranking from Salamanca (Spain) users measured in
public contributions on self-created repositories, the Salamanca 2019 ranking will always be available, but
now more rankings can be found in this repository such as:

* **Salamanca, Spain 2019 Ranking** - https://github.com/alvarob96/rankhub/blob/master/spain/salamanca
* **Zamora, Spain 2019 Ranking** - https://github.com/alvarob96/rankhub/blob/master/spain/zamora
* **Valladolid, Spain 2019 Ranking** - https://github.com/alvarob96/rankhub/blob/master/spain/valladolid

**If you have any ranking request please open an issue as described below.**

## Contribute

As this is an open source project it is open to contributions, bug reports, bug fixes, documentation improvements, 
enhancements and ideas.

Also there is an open tab of [issues](https://github.com/alvarob96/rankhub/issues) where anyone can contribute opening 
new issues if needed or navigate through them in order to solve them or contribute to its solving.

## Disclaimer

This project is made with research purposes only, so to create a Python package to make it 
usable with Python in order to retrieve GitHub stats that can further be used for data analysis.

As the use case is just an approach, note that it can have some errors related to data retrieval
from GitHub. Also the generated ranking has no intention of generating any kind of competition
between the involved people in the generated ranking/s.