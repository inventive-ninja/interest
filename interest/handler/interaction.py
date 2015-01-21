from aiohttp.helpers import atoms


class Interaction(dict):
    """Interaction representation.

    Interaction object represents interaction between :class:`.Handler`
    and client as dict ready to use with text templates. Dict is safe.
    If key is missing client gets '-' symbol. All values are strings.
    By default there are available basic keys. When you set
    interaction.extended to True there are available also extended keys.
    See key lists below.

    Parameters
    ----------
    .. warning:: Parameters are not a part of the public API.

    Basic keys
    ----------
    agent: str
        Client's agent representation.
    duration: str
        Handling duration in mileseconds.
    host: str
        Client remote adress.
    lenght: str
        Response length in bytes.
    process: str
        Process identifier.
    referer: str
        Client's referer representation.
    request: str
        Client's request representation.
    status: str
        Response status.
    time: str
        Handling time (GMT).

    Extended keys
    -------------
    {key}i: str
        Request header by key.
    {key}o: str
        Response header by key.

    Example
    -------
    Usually we have Intercation instance in :meth:`.Logger.access` call.
    Imagine our interactive console works in context of this method::

        >>> interaction['host']
        '127.0.0.1',
        >>> interaction['length']
        '193'
        >>> interaction['{content-type}o']
        '-'
        >>> interaction.extended = True
        >>> interaction['{content-type}o']
        'application/json; charset=utf-8'

    Notes
    -----
    Safe dict idea with random access to request/respones headers
    is borrowed from Gunicorn/aiohttp libraries.

    .. seealso:: API: :attr:`dict`
    """

    # Public

    def __init__(self, *, request, response, transport, duration):
        self.__inheaders = getattr(request, 'headers', None)
        self.__outheaders = getattr(response, 'headers', None)
        self.__request = request
        self.__response = response
        self.__transport = transport
        self.__duration = duration
        self.__extended = False
        self.__populate()

    def __missing__(self, key):
        if self.extended:
            headers = None
            if key.startswith('{'):
                if key.endswith('}i'):
                    headers = self.__inheaders
                elif key.endswith('}o'):
                    headers = self.__outheaders
            if headers is not None:
                return str(headers.get(key[1:-2], '-'))
        return '-'

    @property
    def extended(self):
        """Extended flag (read/write).
        """
        return self.__extended

    @extended.setter
    def extended(self, value):
        self.__extended = value

    # Private

    def __populate(self):
        data = atoms(
            self.__request, None, self.__response,
            self.__transport, self.__duration)
        self['agent'] = data.get('a', '-')
        self['duration'] = data.get('D', '-')
        self['host'] = data.get('h', '-')
        self['lenght'] = data.get('b', '-')
        self['process'] = data.get('p', '-')
        self['referer'] = data.get('f', '-')
        self['request'] = data.get('r', '-')
        self['status'] = data.get('s', '-')
        self['time'] = data.get('t', '-')