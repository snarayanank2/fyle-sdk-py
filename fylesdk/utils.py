from .exceptions import *
import requests
import json


TOKEN_URL = 'https://staging.fyle.in/api/oauth/token'
SERVER_URL = 'https://staging.fyle.in'


def get_access_token(client_id, client_secret, refresh_token):
    """Get the access token using a HTTP post.

    Parameters:
        client_id (str): Client ID for Fyle API.
        client_secret (str): Client secret for Fyle API.
        refresh_token (str): Refresh token for Fyle API.
    """

    api_data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(TOKEN_URL, data=api_data)

    if response.status_code == 200:
        access_token = json.loads(response.text)['access_token']
        return access_token
    
    elif response.status_code == 401:
        raise UnauthorizedClientError('Wrong client secret or/and refresh token', response.text)

    elif response.status_code == 404:
        raise NotFoundClientError('Client ID doesn\'t exist', response.text)

    elif response.status_code == 500:
        raise InternalServerError('Internal server error', response.text)

    else:
        raise FyleSDKError('Error: {0}'.format(response.status_code), response.text)



def get_request(params, api_url, access_token):
    """Create a HTTP GET request.

    Parameters:
        params (dict): HTTP GET parameters for the wanted API.
        api_url (str): Url for the wanted API.
        access_token (str): Access token for Fyle API authorization.
    """

    api_headers = {'Authorization': 'Bearer {0}'.format(access_token)}
    api_params = {}

    for k in params:
        # ignore all unused params
        if not params[k] is None:
            p = params[k]

            # convert boolean to lowercase string
            if isinstance(p, bool):
                p = str(p).lower()

            api_params[k] = p

    response = requests.get(
        '{0}{1}'.format(SERVER_URL, api_url), 
        headers=api_headers, 
        params=api_params
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
    
    

def post_request(data, api_url, access_token):
    """Create a HTTP post request.

    Parameters:
        data (dict): HTTP POST body data for the wanted API.
        api_url (str): Url for the wanted API.
        access_token (str): Access token for Fyle API authorization.
    """

    api_headers = {'Authorization': 'Bearer {0}'.format(access_token)}
    
    response = requests.post(
        '{0}{1}'.format(SERVER_URL, api_url),
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
