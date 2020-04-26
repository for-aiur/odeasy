import os
import wget
import tarfile

from odeasy import ODEASY_MODELS_FOLDER
from odeasy.base import ModelFetcher, ModelMetaData
from odeasy.helpers import url_is_valid
from odeasy.exceptions import InvalidUrlException


class ModelFetcherRemoteTarFile(ModelFetcher):

    def __init__(self):
        super(ModelFetcherRemoteTarFile, self).__init__()

        self.root = ODEASY_MODELS_FOLDER
        self.subfolder = ''

    def set_subfolder(self, subfolder):
        self.subfolder = subfolder

    def fetch(self, uri):
        if not url_is_valid(uri):
            raise InvalidUrlException

        self.target_location = os.path.join(self.root, self.subfolder, os.path.basename(uri))

        if not tarfile.is_tarfile(self.target_location):
            raise Exception

        if os.path.exists(self.target_location):
            return self.target_location

        wget.download(uri, self.target_location)

        if os.path.exists(self.target_location):
            tf = tarfile.open(self.target_location)
            tf.extractall(path=os.path.dirname(self.target_location))

        return self.target_location
