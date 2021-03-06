from pandas_datareader.base import _DailyBaseReader


class StooqDailyReader(_DailyBaseReader):

    """
    Returns DataFrame/Panel of historical stock prices from symbols, over date
    range, start to end.

    Parameters
    ----------
    symbols : string, array-like object (list, tuple, Series), or DataFrame
        Single stock symbol (ticker), array-like object of symbols or
        DataFrame with index containing stock symbols.
    retry_count : int, default 3
        Number of times to retry query request.
    pause : int, default 0
        Time, in seconds, to pause between consecutive queries of chunks. If
        single value given for symbol, represents the pause between retries.
    chunksize : int, default 25
        Number of symbols to download consecutively before intiating pause.
    session : Session, default None
        requests.sessions.Session instance to be used


    Notes
    -----
    See `Stooq <https://stooq.com>`__
    """

    @property
    def url(self):
        """API URL"""
        return 'https://stooq.com/q/d/l/'

    def _get_params(self, symbol, country="US"):
        symbol_parts = symbol.split(".")
        if len(symbol_parts) == 1:
            symbol = ".".join([symbol, country])
        else:
            if symbol_parts[1].lower() not in ['de', 'hk', 'hu', 'jp',
                                               'pl', 'uk', 'us']:
                symbol = ".".join([symbol, "US"])

        params = {
            's': symbol,
            'i': "d"
        }
        return params
