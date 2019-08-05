from .api_base import ApiBase
import requests

class Files(ApiBase):
    """Class for Expenses APIs."""

    POST_FILE = '/api/tpa/v1/files'
    CREATE_UPLOAD_URL = '/api/tpa/v1/files/{0}/upload_url'
    CREATE_DOWNLOAD_URL = '/api/tpa/v1/files/{0}/download_url'
    GET_FILE_BY_ID = '/api/tpa/v1/files/{0}'

    def post(self, file_name):
        """Create an File.

        Parameters:
            file_name (str): Name of the file with extention.
        
        Returns:
            ID from the new File.
        """

        data = {
            "name": file_name
        }
        return self._post_request(data, Files.POST_FILE)
        

    def create_upload_url(self, file_id):
        """Create an File.

        Parameters:
            file_id (str): Special string representing a file with prefix 'f'
        
        Returns:
            AWS S3 upload url.
        """

        return self._post_request({}, Files.CREATE_UPLOAD_URL.format(file_id))
    
    def create_download_url(self, file_id):
        """Create an File.

        Parameters:
            file_id (str): Unique ID to find an File. File Id is our internal Id, it starts with prefix f always. (required)
        
        Returns:
            AWS S3 download url.
        """

        return self._post_request({}, Files.CREATE_DOWNLOAD_URL.format(file_id))


    def upload_file_to_aws(self, content_type, data, url):
        """Create an File.

        Parameters:
            content_type (str): Content type of file. Example application/json for JSON
            data (file): File data as binary string.
            url (str): AWS S3 upload URL.
        
        Returns:
            AWS S3 upload url.
        """

        headers = {"Content-Type": content_type}
        requests.put(url=url, data=data, headers=headers)


    def get_by_id(self, file_id):
        """Get a File by Id.

        Parameters:
            file_id (str): Unique ID to find an File. File Id is our internal Id, it starts with prefix f always. (required)

        Returns:
            Dict in File schema.
        """

        return self._get_request({}, Files.GET_FILE_BY_ID.format(file_id))