from tenacity import(
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log
)
import logging
from groq import APITimeoutError, RateLimitError

logger = logging.getLogger(__name__)

@retry(
    wait = wait_exponential(
        multiplier=1,
        min=2,
        max=10
    ),

    stop = stop_after_attempt(3),

    retry = retry_if_exception_type(
        (APITimeoutError,
        RateLimitError)
    ),

    before_sleep = before_sleep_log(
        logger,
        logging.WARNING
    )

)

def retry_llm_request(api_call):
    return api_call()
