from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Segmentation(Resource):
    name = "segmentation"
    available_since = "4.2.13"
    removed_since = None

    class _segmentation(Route):
        name = "segmentation"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/segmentation"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _rateModel(Route):
        name = "rateModel"
        available_since = "4.2.14"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/datasets/rateModel"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }