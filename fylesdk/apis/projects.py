from .api_base import ApiBase

class Projects(ApiBase):
    """Class for Projects APIs."""

    GET_PROJECTS = '/api/tpa/v1/projects'
    POST_PROJECTS = '/api/tpa/v1/projects'

    def post(self, data):
        """Create or Update Projects in bulk.

        Parameters:
            data (list): List of dicts in Projects schema.
        
        Returns:
            List with IDs from the new and updated Projects.
        """
        return self._post_request(data, Projects.POST_PROJECTS)

    def get(self, active_only=None):
        """Get the list of existing Projects.

        Parameters:
            active_only (bool): When set as false, the result will include all the Projects for the organization. (optional)

        Returns:
            List with dicts in Projects schema.
        """
        return self._get_request({
            'active_only': active_only
        }, Projects.GET_PROJECTS)