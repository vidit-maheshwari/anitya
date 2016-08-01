# -*- coding: utf-8 -*-

"""
 (c) 2014 - Copyright Red Hat Inc

 Authors:
   Pierre-Yves Chibon <pingou@pingoured.fr>

"""

from __future__ import absolute_import
from anitya.lib.backends import BaseBackend, get_versions_by_regex


REGEX = '<a href="/projects/[^/]*/releases/[0-9]*">([^<]*)</a>'


class FreshmeatBackend(BaseBackend):
    ''' The custom class for projects hosted on freshmeat.net.

    This backend allows to specify a version_url and a regex that will
    be used to retrieve the version information.
    '''

    name = 'Freshmeat'
    examples = [
        'http://freecode.com/projects/atmail',
        'http://freecode.com/projects/awstats',
    ]

    @classmethod
    def get_version(cls, project):
        ''' Method called to retrieve the latest version of the projects
        provided, project that relies on the backend of this plugin.

        :arg Project project: a :class:`model.Project` object whose backend
            corresponds to the current plugin.
        :return: the latest version found upstream
        :return type: str
        :raise AnityaPluginException: a
            :class:`anitya.lib.exceptions.AnityaPluginException` exception
            when the version cannot be retrieved correctly

        '''
        return cls.get_ordered_versions(project)[-1]

    @classmethod
    def get_versions(cls, project):
        ''' Method called to retrieve all the versions (that can be found)
        of the projects provided, project that relies on the backend of
        this plugin.

        :arg Project project: a :class:`model.Project` object whose backend
            corresponds to the current plugin.
        :return: a list of all the possible releases found
        :return type: list
        :raise AnityaPluginException: a
            :class:`anitya.lib.exceptions.AnityaPluginException` exception
            when the versions cannot be retrieved correctly

        '''
        url_template = 'http://freshmeat.net/projects/%(name)s'

        url = url_template % {'name': project.name}

        return get_versions_by_regex(url, REGEX, project)
