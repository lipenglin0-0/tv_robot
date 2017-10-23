class CookiePoolError(Exception):
    def __str__(self):
        return repr('Cookie Pool Error')


class SetCookieError(CookiePoolError):
    def __str__(self):
        return repr('Set Cookie Error')


class GetCookieError(CookiePoolError):
    def __str__(self):
        return repr('Get Cookie Error')


class DeleteCookieError(CookiePoolError):
    def __str__(self):
        return repr('Delete Cookie Error')


class GetRandomCookieError(CookiePoolError):
    def __str__(self):
        return repr('Get Random Cookie Error')


class GetAllCookieError(CookiePoolError):
    def __str__(self):
        return repr('Get All Cookie Error')
