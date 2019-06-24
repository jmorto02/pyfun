import json
from collections import namedtuple


def map_json_to_object(model, data):
        x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        for key, value in x._asdict().items():
            setattr(model, key, value)
        return model
