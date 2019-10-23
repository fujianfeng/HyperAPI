from HyperAPI.hdp_api.base.resource import Resource
from HyperAPI.hdp_api.base.route import Route


class ExportService(Resource):
    name = "ExportService"
    available_since = "4.2.12"
    removed_since = None

    class _exportCreate(Route):
        name = "exportCreate"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/exports"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID
        }

    class _exportStream(Route):
        name = "exportStream"
        httpMethod = Route.GET
        path = "/projects/{project_ID}/exports/{export_ID}/stream"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
            'export_ID': Route.VALIDATOR_OBJECTID
        }
