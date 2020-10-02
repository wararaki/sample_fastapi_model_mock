import pickle
from typing import Dict

from pydantic import BaseModel


_MODEL_PATH = 'model/model.pkl'


class RequestForm(BaseModel):
    item_id: int
    user_id: int


class ModelService:
    model = None

    @classmethod
    def get_model(cls):
        if cls.model is None:
            with open(_MODEL_PATH, 'rb') as f:
                cls.model = pickle.load(f)
        return cls.model

    @classmethod
    def predict(cls, input_: RequestForm) -> float:
        model = cls.get_model()
        X = [[input_.item_id, input_.user_id]]

        return model.predict(X)


def predict(input_: RequestForm) -> Dict[str, float]:
    result = ModelService.predict(input_)
    return {'result': 0.0 }
