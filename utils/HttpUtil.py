import time
import httpx

from constants.StringConstants import StringConstants
from models.HostStatistics import HostStatistics
from models.ResponseInfo import ResponseInfo
from utils.ResponseCodeUtil import ResponseCodeUtil
from utils.StringUtil import StringUtil


class HttpUtil:

    @staticmethod
    def _test_url(url):

        response_info = ResponseInfo()
        response_info.url = url
        start_time = time.time()

        try:
            with httpx.Client() as client:
                response = client.get(url=url, follow_redirects=True)
                response_info.status_code = response.status_code
                response_info.response_time = time.time() - start_time
                response_info.fail = ResponseCodeUtil.is_failed(response.status_code)

        except httpx.RequestError as e:
            response_info.error_message = f'Request error: {str(e)}'
        except Exception as e:
            response_info.error_message = f'Unexpected error: {str(e)}'

        return response_info

    @staticmethod
    def _test_and_get_url_stat(url, requests_count):

        host_statistics = HostStatistics()
        host_statistics.url = url

        for i in range(requests_count):
            response_info = HttpUtil._test_url(url)
            print(f'Attempt {i+1}: ', response_info)
            host_statistics.response_time.append(response_info.response_time)

            if response_info.error_message:
                host_statistics.error_count += 1
            else:
                if response_info.fail:
                    host_statistics.fail_count += 1
                else:
                    host_statistics.success_count += 1

        return host_statistics

    @staticmethod
    def test_server_availability(urls, requests_count) -> dict[str, HostStatistics]:

        list_of_urls = StringUtil.split_string(urls, StringConstants.COMMA)
        full_statistics = {}

        for i, url in enumerate(list_of_urls):
            print(f'Testing server availability for {url}')
            http_statistics = HttpUtil._test_and_get_url_stat(url, requests_count)
            full_statistics[url] = http_statistics

        return full_statistics