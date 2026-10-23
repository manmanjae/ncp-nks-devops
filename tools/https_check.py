from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from time import perf_counter
import sys


def check_url(url):
    exit_code = 0
    start = perf_counter()

    try:
        with urlopen(url, timeout=5) as response:
            status_code = response.status

        print(f"HTTP 상태: {status_code}")

    except HTTPError as error:
        exit_code = 1
        print(f"HTTP 오류: {error.code}")

    except URLError as error:
        exit_code = 1
        print(f"연결 오류: {error.reason}")

    finally:
        elapsed = perf_counter() - start
        print(f"소요 시간: {elapsed * 1000:.1f} ms")

    return exit_code


def main():
    if len(sys.argv) != 2:
        print("사용법: python3 tools/https_check.py URL")
        return 2

    return check_url(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
