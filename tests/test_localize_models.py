import os
import pytest

from odeasy.model_fetcher_tar import ModelFetcherRemoteTarFile
from odeasy.base import ModelMetaData
from odeasy import ODEASY_MODELS_FOLDER


def test_fetch_remote_tar():
    tarfile = 'https://dev-files.blender.org/file/download/bwdp5reejwpkuh5i2oak/PHID-FILE-nui3bpuan4wdvd7yzjrs/sample.tar.gz'
    model_fetcher = ModelFetcherRemoteTarFile()
    assert os.path.exists(model_fetcher.fetch(tarfile))
    
def test_must_fail_fetching_non_tar():
    tarfile = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
    model_fetcher = ModelFetcherRemoteTarFile()

    with pytest.raises(Exception):
        model_fetcher.fetch(tarfile)
