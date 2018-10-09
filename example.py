import requests
from async_helper import Async


async def get_homepages():
    quora_future = Async.run_in_executor(None, requests.get, 'http://www.quora.com')
    reddit_future = Async.run_in_executor(None, requests.get, 'http://www.reddit.com')
    quora_response = await quora_future
    reddit_response = await reddit_future
    return quora_response.content, reddit_response.content


def main():
    quora_homepage, reddit_homepage = Async.run_until_complete(get_homepages())
    print("Quora: {}, Reddit {}".format(len(quora_homepage), len(reddit_homepage)))


if __name__ == '__main__':
    main()
