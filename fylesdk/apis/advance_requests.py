from .api_base import ApiBase


class AdvanceRequests(ApiBase):
    """Class for Advance Requests APIs"""

    GET_ADVANCE_REQUESTS = '/api/tpa/v1/advance_requests'
    GET_ADVANCE_REQUESTS_COUNT = '/api/tpa/v1/advance_requests/count'

    def get(self, offset=None, limit=None, updated_at=None, exported=None, state=None, approved_at=None):
        """Get a list of existing Advance Reports .

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list.
            (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Advances that are exported alone will be returned. (optional)
            state(str) : A parameter to filter expenses by the state that they're in. (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)

        Returns:
            List with dicts in Advance requests schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported,
            'state': state,
            'approved_at': approved_at
        }, AdvanceRequests.GET_ADVANCE_REQUESTS)

    def count(self, offset=None, limit=None, updated_at=None, exported=None, state=None, approved_at=None):
        """Get a count of the existing Advances that match the parameters.

        Parameters:
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list.
            (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            exported (bool): If set to true, all Advances that are exported alone will be returned. (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            state(str) : A parameter to filter expenses by the state that they're in. (optional)

        Returns:
            Count of Advance requests.
        """
        return self._get_request({
            'offset': offset,
            'limit': limit,
            'approved_at': approved_at,
            'updated_at': updated_at,
            'exported': exported,
            'state': state,
        }, AdvanceRequests.GET_ADVANCE_REQUESTS_COUNT)

    def get_all(self, offset=None, limit=None, updated_at=None, exported=None, state=None, approved_at=None):
        """
        Get all the Advance requests based on paginated call
        """

        count = self.count(offset=offset, limit=limit, updated_at=updated_at,
                           exported=exported, state=state, approved_at=approved_at)['count']
        advance_requests = []
        page_size = 300
        for i in range(0, count, page_size):
            segment = self.get(offset=i, limit=page_size, updated_at=updated_at, exported=exported,
                               approved_at=approved_at)
            advance_requests = advance_requests + segment['data']
        return advance_requests
