#!/usr/bin/env python

# Copyright 2019 Alvaro Bartolome
# See LICENSE for details.

import random
import pkg_resources
import os


def get_random():
    """
    This function selects a random User-Agent from the `user-agent-list` txt file, in order to avoid 
    the limitations of the requests that are going to be sent to GitHub. The User-Agent is specified 
    on the headers of the requests and is different for every request.

    Returns:
        :obj:`str` - user_agent:
            The returned :obj:`str` is the name of a random User-Agent, which will be passed on the 
            headers of a request so to avoid restrictions due to the use of multiple requests from the 
            same User-Agent.
    
    Raises:
        IOError: raised when `user_agent_list.txt` file was unable to retrieve or errored.
        FileNotFoundError: raised if `user_agent_list.txt` file has not been found.

    """

    resource_package = __name__
    resource_path = '/'.join(('resources', 'user_agent_list.txt'))
    file_ = pkg_resources.resource_filename(resource_package, resource_path)

    if os.path.exists(file_):
        with open(file_, 'r') as f:
            content = f.read(1)

            if content:
                lines = f.readlines()

                return str(random.choice(lines)).replace("\n", "")
            else:
                raise IOError("unable to retrieve a random user agent!")
    else:
        raise FileNotFoundError("user agents file not found!")
