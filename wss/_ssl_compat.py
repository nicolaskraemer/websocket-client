"""
wss - WebSocket client library for Python

Copyright (C) 2010 Hiroki Ohtani(liris)

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""
__all__ = ["HAVE_SSL", "ssl", "SSLError", "SSLWantReadError", "SSLWantWriteError"]

try:
    import ssl
    from ssl import SSLError
    from ssl import SSLWantReadError
    from ssl import SSLWantWriteError
    HAVE_CONTEXT_CHECK_HOSTNAME = False
    if hasattr(ssl, 'SSLContext') and hasattr(ssl.SSLContext, 'check_hostname'):
        HAVE_CONTEXT_CHECK_HOSTNAME = True

    __all__.append("HAVE_CONTEXT_CHECK_HOSTNAME")
    HAVE_SSL = True
except ImportError:
    # dummy class of SSLError for environment without ssl support
    class SSLError(Exception):
        pass

    class SSLWantReadError(Exception):
        pass

    class SSLWantWriteError(Exception):
        pass

    ssl = None
    HAVE_SSL = False
