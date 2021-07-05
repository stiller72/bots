class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class BackendError(Error):
    """Вызывается, когда входное значение мало"""
    pass


class ValueTooLargeError(Error):
    """Вызывается, когда входное значение велико"""
    pass
