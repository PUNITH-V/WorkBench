from tenacity import wait_exponential,  stop_after_attempt, retry

def with_retry(func):
    return retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=1, max=10),
    )(func)

