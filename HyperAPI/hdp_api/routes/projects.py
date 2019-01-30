from HyperAPI.hdp_api.routes import Resource, Route
from HyperAPI.hdp_api.routes.base.version_management import deprecated_since


class Projects(Resource):
    name = "Projects"
    available_since = "3.0"
    removed_since = None

    class _Projects(Route):
        name = "Projects"
        httpMethod = Route.GET
        path = "/projects"

    class _Getaproject(Route):
        name = "Get a project"
        httpMethod = Route.GET
        path = "/projects/{project_ID}"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _AddProject(Route):
        name = "Add Project"
        httpMethod = Route.POST
        path = "/projects"

    @deprecated_since('3.6')
    class _Defaultproject(Route):
        name = "Default project"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/updateSelected"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Updateproject(Route):
        name = "Update project"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/update"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    @deprecated_since('3.6')
    class _renameProject(Route):
        name = "renameProject"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/rename"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _updateShareUsers(Route):
        name = "updateShareUsers"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/updateShareUsers"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }

    class _Deleteproject(Route):
        name = "Delete project"
        httpMethod = Route.POST
        path = "/projects/{project_ID}/delete"
        _path_keys = {
            'project_ID': Route.VALIDATOR_OBJECTID,
        }
