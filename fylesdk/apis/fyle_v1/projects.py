from ..api_base import ApiBase

class Projects(ApiBase):
    """Class for Projects APIs."""

    GET_PROJECTS = '/api/tpa/v1/projects'
    GET_PROJECTS_COUNT = '/api/tpa/v1/projects/count'
    POST_PROJECTS = '/api/tpa/v1/projects'

    def post(self, data):
        """Create or Update Projects in bulk.

        Parameters:
            data (list): List of dicts in Projects schema.
        
        Returns:
            List with IDs from the new and updated Projects.
        """
        return self._post_request(data, Projects.POST_PROJECTS)

    def get(self, active_only=None, **kwargs):
        """Get the list of existing Projects.

        Parameters:
            active_only (bool): When set as false, the result will include all the Projects for the organization. (optional)

        Returns:
            List with dicts in Projects schema.
        """
        return self._get_request({
            'active_only': active_only,
            **kwargs
        }, Projects.GET_PROJECTS)

    def count(self):
        """Get the number of Projects.

        Returns:
            Count of Projects.
        """
        return self._get_request({}, Projects.GET_PROJECTS_COUNT)

    def get_all(self):
        """
        Get all the projects based on paginated call
        """
        count = self.count()['count']
        projects = []
        page_size = 200
        for i in range(0, count, page_size):
            segment = self.get(offset=i, limit=page_size)
            projects = projects + segment['data']
        return projects
