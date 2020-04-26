class DetectionFactory():

    def get_model_zoo():
        return 0


DATASETS_COCO = "coco"

class Detector:

    def __init__(self):
        pass

    def exclude_category(self):
        pass

    def set_active_categories_by_name(self):
        pass

    def list_categories(self):
        return ''

    def detect(self, img):
        return [0, 0, 100, 100]


class ModelZoo(metaclass=abc.ABCMeta):
    
    def __init__(self, name: str):
        self.supports_queries = False
        
    @abc.abstractmethod
    def register_model(self, DetectorMetaData, ModelFetcher):
        raise NotImplementedError()


    def update_model_metadata(self, detector_meta_data):
        pass

    def get_list_of_models():
        return ''

    def get_fastest_model(self):
        return Detector()

    def get_best_model(self):
        return Detector()

    def list_models(self):
        return ''

    def get_model_by_id(self, id):
        return Detector()

    def get_model_by_category(self, id):
        pass

    def remove_model(self, model_id):
        return 0


ModelZooRegistry = {
    "zoos": [
        # ModelZoo1, ModelZoo2
    ]
}


class ModelZooTFOD(ModelZoo):

    def __init__(self, name: str):
        # initialize a db here?
        self.supports_queries = True

    def register_model(self, meta: DetectorMetaData, fetcher: ModelFetcher):
        raise NotImplementedError()

    def remove_model(self, model_id):
        return 0

    
