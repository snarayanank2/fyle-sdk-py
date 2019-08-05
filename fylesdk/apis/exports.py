from .api_base import ApiBase

class Exports(ApiBase):
    """Class for Exports APIs."""

    POST_EXPORT_BATCH = '/api/tpa/v1/export_batches'
    POST_EXPORT_BATCH_LINEITEMS = '/api/tpa/v1/export_batches/{0}/lineitems'
    GET_EXPORT_BATCHES = '/api/tpa/v1/export_batches'
    GET_EXPORT_BATCHES_COUNT = '/api/tpa/v1/export_batches/count'
    GET_EXPORT_BATCH_BY_ID = '/api/tpa/v1/export_batches/{0}'
    GET_EXPORT_BATCH_LINEITEMS = '/api/tpa/v1/export_batches/{0}/lineitems'

    def post_batch(self, batch):
        """Mark Third Party Export of Fyle objects as Successful or Failed.

        Parameters:
            batch (dict): Dict in Export Batch Schema  
        """

        return self._post_request(batch, Exports.POST_EXPORT_BATCH)
    
    def post_batch_lineitems(self, tpa_export_batch_id, lineitems):
        """Mark Third Party Export of Fyle objects as Successful or Failed.

        Parameters:
            batch (list): List of dicts in Export Batch Lineitems Schema  
        """

        return self._post_request(lineitems, Exports.POST_EXPORT_BATCH_LINEITEMS.format(tpa_export_batch_id))
        
    def get_batches(self, updated_at=None, offset=None, limit=None):
        """Returns the details of Third Party Exports.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)

        Returns:
            List with dicts in Export Batch schema.
        """

        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit
        }, Exports.GET_EXPORT_BATCHES)

    def count(self, updated_at=None):
        """Returns the count of Third Party Exports, that satisfy the parameters.

        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)

        Returns:
            Count of Export Batches.
        """
        return self._get_request({
            'updated_at': updated_at
        }, Exports.GET_EXPORT_BATCHES_COUNT)

    def get_batch_by_id(self, tpa_export_batch_id):
        """Get the details of a Third Party Export.

        Parameters:
            tpa_export_batch_id (str): Unique ID to find an Export Batch. (required)

        Returns:
            Dict in Export schema.
        """
        return self._get_request({}, Exports.GET_EXPORT_BATCH_BY_ID.format(tpa_export_batch_id))

    def get_lineitems_by_batch_id(self, tpa_export_batch_id):
        """Get the details of a Third Party Export.

        Parameters:
            tpa_export_batch_id (str): Unique ID to find an Export Batch Lineitems. (required)

        Returns:
            Dict in Export schema.
        """
        return self._get_request({}, Exports.GET_EXPORT_BATCH_LINEITEMS.format(tpa_export_batch_id))