"""
Fyle Jobs
"""
from typing import Dict

from fylesdk import FyleSDK

from .utils import post_request, delete_request


class FyleJobsSDK:
    """
    Fyle Jobs SDK
    """

    def __init__(self, jobs_url: str, fyle_sdk_connection: FyleSDK):
        self.user_profile = fyle_sdk_connection.Employees.get_my_profile()['data']
        self.jobs_url = jobs_url
        self.access_token = fyle_sdk_connection.access_token

    def trigger_now(self, callback_url: str, callback_method: str,
                    job_description: str, object_id: str, payload: any = None,
                    job_data_url: str = None) -> Dict:
        """
        Trigger callback immediately
        :param payload: callback payload
        :param callback_url: callback URL for the job
        :param callback_method: HTTP method for callback
        :param job_description: Job description
        :param job_data_url: Job data url
        :param object_id: object id
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
            'notification': {
                'enabled': False
            },
            'org_user_id': self.user_profile['id']
        }

        response = post_request(self.jobs_url, self.access_token, body)
        return response

    def trigger_interval(self, callback_url: str, callback_method: str,
                         job_description: str, object_id: str, hours: int,
                         start_datetime: str, job_data_url: str = None) -> Dict:
        """
        Trigger callback on Interval
        :param start_datetime: start datetime for job
        :param hours: repeat in hours
        :param callback_url: callback URL for the job
        :param callback_method: HTTP method for callback
        :param job_description: Job description
        :param job_data_url: Job data url
        :param object_id: object id
        :returns: response
        """
        body = {
            'template': {
                'name': 'http.main',
                'data': {
                    'url': callback_url,
                    'method': callback_method
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
            'org_user_id': self.user_profile['id']
        }

        response = post_request(self.jobs_url, self.access_token, body)
        return response

    def delete_job(self, job_id):
        """
        Delete job
        :param job_id: id of the job to delete
        :return:
        """
        response = delete_request(self.jobs_url, self.access_token, job_id)
        return response
