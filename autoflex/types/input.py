import pydantic as pd
import pydantic.v1 as pd1

AutoflexInputClassTypes = \
    pd._internal._model_construction.ModelMetaclass |
    pd1._internal._model_construction.ModelMetaclass |
    pd.BaseModel |
    pd1.BaseModel


