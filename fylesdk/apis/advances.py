from .api_base import ApiBase


class Advances(ApiBase):
    """Class for Advances APIs."""

    GET_ADVANCES = '/api/tpa/v1/advances'
    GET_ADVANCES_COUNT = '/api/tpa/v1/advances/count'
  
    def get(self, updated_at=None, settled_at=None, offset=None, limit=None, exported=None, settlement_id=None):
        """Get a list of existing Advances.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list.
            (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Advances that are exported alone will be returned. (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            settlement_id(str): List of settlement ids.

        Returns:
            List with dicts in Advance schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'settled_at': settled_at,
            'exported': exported,
            'settlement_id': settlement_id
        }, Advances.GET_ADVANCES)

    def count(self, updated_at=None, exported=None, settled_at=None, settlement_id=None):
        """Get a count of the existing Advances that match the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            exported (bool): If set to true, all Advances that are exported alone will be returned. (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern.
            (optional)
            settlement_id(str): List of settlement ids. (optional)

        Returns:
            Count of Advances.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported,
            'settled_at': settled_at,
            'settlement_id': settlement_id
        }, Advances.GET_ADVANCES_COUNT)

    def get_all(self, updated_at=None, exported=None, settled_at=None, settlement_id=None):
        """
        Get all the advances based on paginated call
        """

        advances = []

        if len(settlement_id) > 40:
            pages = range(0, len(settlement_id), 40)
            chunks = []
            for i in range(0, len(pages)-1):
                chunks.append(settlement_id[pages[i]:pages[i+1]])
            chunks.append(settlement_id[pages[len(pages)-1]:])

            for chunk in chunks:
                count = self.count(updated_at, exported, settled_at, chunk)['count']

                page_size = 300
                for i in range(0, count, page_size):
                    segment = self.get(
                        offset=i,
                        limit=page_size,
                        updated_at=updated_at,
                        exported=exported,
                        settled_at=settled_at,
                        settlement_id=chunk
                    )
                    advances = advances + segment['data']
            return advances

        count = self.count(updated_at, exported, settled_at, settlement_id)['count']

        page_size = 300
        
        for i in range(0, count, page_size):
            segment = self.get(
                offset=i,
                limit=page_size,
                updated_at=updated_at,
                exported=exported,
                settled_at=settled_at,
                settlement_id=settlement_id
            )
            advances = advances + segment['data']
        return advances
