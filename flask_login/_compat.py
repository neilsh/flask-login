# -*- coding: utf-8 -*-
'''
    flask.ext.login.compat
    ----------------------
    A module providing tools for cross-version compatibility.
'''


import sys


PY2 = sys.version_info[0] == 2


if not PY2:  # pragma: no cover
    unicode = str


if PY2:  # pragma: nocover

    from urlparse import urlparse, urlunparse

    def iteritems(d):
        return d.iteritems()

    def itervalues(d):
        return d.itervalues()

    text_type = unicode

else:  # pragma: nocover

    from urllib.parse import urlparse, urlunparse

    assert (urlparse, urlunparse)

    def iteritems(d):
        return iter(d.items())

    def itervalues(d):
        return iter(d.values())

    text_type = str
