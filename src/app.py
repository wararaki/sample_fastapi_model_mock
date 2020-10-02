from fastapi import FastAPI

from .prediction import predict as predict_function


api = FastAPI()


@api.get('/ping')
def ping():
    return 'hello'


invocation = (api.post('/invocations'))(predict_function)
