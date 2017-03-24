import os
from scrapy.http import Response, Request


def fake_response_from_file(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the responses directory,
                      but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.
    """
    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)
    if not file_name[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, file_name)
    else:
        file_path = file_name

    with open(file_path, 'r') as f:
        file_content = f.read()
        file_content = str.encode(file_content)

    response = Response(url=url, request=request, body=file_content)
    response.encoding = 'utf-8'

    return response

if __name__ == '__main__':
    unittest.main()
