from .api_base import ApiBase

class Reports(ApiBase):
    """Class for Reports APIs."""

    GET_REPORTS = '/api/tpa/v1/reports'
    GET_REPORTS_COUNT = '/api/tpa/v1/reports/count'
  
    def get(self, updated_at=None, settled_at=None, reimbursed_at=None, approved_at=None, state=None, offset=None, limit=None, exported=None):
        """Get a list of Reports.
        
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            offset (int): A cursor for use in pagination, offset is an object ID that defines your place in the list. (optional)
            limit (int): A limit on the number of objects to be returned, between 1 and 1000. (optional)
            exported (bool): If set to true, all Reports that are already submitted will alone be returned. (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            reimbursed_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            state(str): A parameter to filter reports by the state that they're in. (optional)

        Returns:
            List with dicts in Reports schema.
        """
        return self._get_request({
            'updated_at': updated_at,
            'offset': offset,
            'limit': limit,
            'settled_at': settled_at,
            'reimbursed_at': reimbursed_at,
            'approved_at': approved_at,
            'exported': exported,
            'state': state
        }, Reports.GET_REPORTS)

    def count(self, updated_at=None, exported=None, settled_at=None, reimbursed_at=None, approved_at=None, state=None):
        """Get the count of Reports that match the parameters.
        
        Parameters:
            updated_at (str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            exported (bool): If set to true, all Reports that are already submitted will alone be returned. (optional)
            settled_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            approved_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            reimbursed_at(str): Date string in yyyy-MM-ddTHH:mm:ss.SSSZ format along with operator in RHS colon pattern. (optional)
            state(str): A parameter to filter reports by the state that they're in. (optional)
            
        Returns:
            Count of Reports.
        """
        return self._get_request({
            'updated_at': updated_at,
            'exported': exported,
            'settled_at': settled_at,
            'reimbursed_at': reimbursed_at,
            'approved_at': approved_at,
            'state': state
        }, Reports.GET_REPORTS_COUNT)