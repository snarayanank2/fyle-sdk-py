from .api_base import ApiBase


class Settlements(ApiBase):
    """Class for Settlements APIs."""

    GET_SETTLEMENTS = '/api/tpa/v1/settlements'
    GET_SETTLEMENT_BY_ID = '/api/tpa/v1/settlements/{0}'
    GET_SETTLEMENTS_COUNT = '/api/tpa/v1/settlements/count'

    def get(self, updated_at=None, offset=None, limit=None, exported=None):
        """Get Settlements that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Settlements that are exported alone will be returned. (optional)

        Returns:
            List with dicts in Settlements schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'exported': exported
        }, Settlements.GET_SETTLEMENTS)

    def get_by_id(self, settlement_id):
        """Get an Settlement by Id.

        Parameters:
            settlement_id (str): Unique ID to find an Settlement. Settlement Id is our internal Id, it starts with prefix re always. (required)

        Returns:
            Dict in Settlement schema.
        """
        return self._get_request({}, Settlements.GET_SETTLEMENT_BY_ID.format(settlement_id))

    def count(self, updated_at=None, exported=None):
        """Get the number of Settlements that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Settlements that are exported alone will be returned. (optional)

        Returns:
            Count of Settlements.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported
        }, Settlements.GET_SETTLEMENTS_COUNT)

    def get_all(self, updated_at=None, exported=None):
        """
        Get all the settlements based on paginated call
        """

        count = self.count(updated_at, exported)['count']
        settlements = []
        page_size = 300
        for i in range(0, count, page_size):
            segment = self.get(offset=i, limit=page_size, updated_at=updated_at, exported=exported)
            settlements = settlements + segment['data']
        return settlements
