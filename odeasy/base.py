import abc


class ModelMetaData(metaclass=abc.ABCMeta):

    def __init__(self, uri: str):
        self.uri = uri


class ModelFetcher(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def fetch(self, uri: str):
        raise NotImplementedError()