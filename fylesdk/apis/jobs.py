from typing import Dict

from .api_base import ApiBase


class Jobs(ApiBase):
    """Class for Jobs APIs."""

    def body_tempate(self, callback_url, callback_method, job_description, job_data_url, object_id, hours,
                     start_datetime, org_user_id, payload):
        """

        :param org_user_id: org_user_id
        :param payload: callback payload
        :param callback_url: callback URL for the job
        :param callback_method: HTTP method for callback
        :param job_description: Job description
        :param job_data_url: Job data url
        :param object_id: object id
        :param start_datetime: start datetime for job
        :param hours: repeat in hours
        :returns: response
        """
        body = {
            'template': {
                'name': 'http.main',
                'data': {
                    'url': callback_url,
                    'method': callback_method,
                    'payload': payload
                }
            },
            'job_data': {
                'description': job_description,
                'url': '' if not job_data_url else job_data_url
            },
            'job_meta_data': {
                'object_id': object_id
            },
            'trigger': {
                'type': 'interval',
                'when': {
                    'hours': hours,
                    'start_date': start_datetime
                }
            },
            'notification': {
                'enabled': False
            },
            'org_user_id': org_user_id
        }
        return body

    def trigger_now(self, callback_url: str, callback_method: str, org_user_id: str,
                    job_description: str, object_id: str, payload: any = None,
                    job_data_url: str = None, start_datetime=None, hours=None, ) -> Dict:
        """
        Trigger callback immediately

        :param org_user_id: org_user_id
        :param payload: callback payload
        :param callback_url: callback URL for the job
        :param callback_method: HTTP method for callback
        :param job_description: Job description
        :param job_data_url: Job data url
        :param object_id: object id
        :param start_datetime: start datetime for job
        :param hours: repeat in hours
        :returns: response
        """
        body = self.body_tempate(callback_url, callback_method, job_description, job_data_url, object_id, hours,
                                 start_datetime, org_user_id, payload)
        response = self._post_request(body, api_url='/v2/jobs')
        return response

    def trigger_interval(self, callback_url: str, callback_method: str,
                         job_description: str, object_id: str, hours: int,
                         start_datetime: str, org_user_id: str, job_data_url: str = None, payload: str = None) -> Dict:
        """
        Trigger callback on Interval
        :param org_user_id: org_user_id
        :param payload: payload
        :param start_datetime: start datetime for job
        :param hours: repeat in hours
        :param callback_url: callback URL for the job
        :param callback_method: HTTP method for callback
        :param job_description: Job description
        :param job_data_url: Job data url
        :param object_id: object id
        :returns: response
        """
        body = self.body_tempate(callback_url, callback_method, job_description, job_data_url, object_id, hours,
                                 start_datetime, org_user_id, payload)
        response = self._post_request(body, api_url='/v2/jobs')
        return response

    def delete(self, job_id):
        """
        Delete job
        :param job_id: id of the job to delete
        :return:
        """
        response = self.delete_job_request(job_id)
        return response
