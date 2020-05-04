import json
import requests
from fylesdk import WrongParamsError, InvalidTokenError, NoPrivilegeError, NotFoundItemError, ExpiredTokenError, \
    InternalServerError, FyleSDKError


def post_request(jobs_url, access_token, data):
    """
    Post request
    :param jobs_url:
    :param access_token:
    :param data:
    :return:
    """

    api_headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer {0}'.format(access_token)
    }

    response = requests.post(
        jobs_url,
        headers=api_headers,
        json=data
    )

    if response.status_code == 200:
        result = json.loads(response.text)
        return result

    elif response.status_code == 400:
        raise WrongParamsError('Some of the parameters are wrong', response.text)

    elif response.status_code == 401:
        raise InvalidTokenError('Invalid token, try to refresh it', response.text)

    elif response.status_code == 403:
        raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

    elif response.status_code == 404:
        raise NotFoundItemError('Not found item with ID', response.text)

    elif response.status_code == 498:
        raise ExpiredTokenError('Expired token, try to refresh it', response.text)

    elif response.status_code == 500:
        raise InternalServerError('Internal server error', response.text)

    else:
        raise FyleSDKError('Error: {0}'.format(response.status_code), response.text)


def delete_request(jobs_url, access_token, job_id):
    """
    delete request
    :param jobs_url:
    :param access_token:
    :param job_id:
    :return:
    """

    api_headers = {
        'Authorization': 'Bearer {0}'.format(access_token)
    }
    response = requests.delete(
        '{0}{1}'.format(jobs_url, job_id),
        headers=api_headers,
    )

    if response.status_code == 200:
        result = json.loads(response.text)
        return result

    elif response.status_code == 400:
        raise WrongParamsError('Some of the parameters are wrong', response.text)

    elif response.status_code == 401:
        raise InvalidTokenError('Invalid token, try to refresh it', response.text)

    elif response.status_code == 403:
        raise NoPrivilegeError('Forbidden, the user has insufficient privilege', response.text)

    elif response.status_code == 404:
        raise NotFoundItemError('Not found item with ID', response.text)

    elif response.status_code == 498:
        raise ExpiredTokenError('Expired token, try to refresh it', response.text)

    elif response.status_code == 500:
        raise InternalServerError('Internal server error', response.text)

    else:
        raise FyleSDKError('Error: {0}'.format(response.status_code), response.text)
