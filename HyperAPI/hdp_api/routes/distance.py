from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class Distance(Resource):
    name = "distance"
    available_since = "4.2.15"
    removed_since = None

    class _getDistances(Route):
        name = "getDistances"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/distances"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _setDistances(Route):
        name = "setDistances"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/distances"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }