from tenacity import retry, stop_after_attempt, wait_exponential
from requests.exceptions import ConnectionError, Timeout


def with_retry(func):
    return retry(
        retry=lambda retry_state: isinstance(
            retry_state.outcome.exception(),
            (ConnectionError, Timeout, TimeoutError),
        ),
        stop=stop_after_attempt(3),
        wait=wait_exponential(
            multiplier=2,
            min=1,
            max=10,
        ),
        reraise=True,
    )(func)