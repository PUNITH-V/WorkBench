
def extraction_prompt(transcript:str) -> str:
    return f"""
           Role/task: extract a support ticket from a transcript.

           Required fields:
           - customer_name: string
           - issue_category: choose only ['billing', 'technical', 'account', 'other']
           - sentiment: choose only ['positive', 'neutral', 'negative']

           Rules:
           - You must extract the required fields from the transcript.
           - you must not add any additional fields.
           - You must not make up any information. 
           - If no customer name is stated, set customer_name to "Unknown".
           - If there is no clear matching issue type, set issue_category to "other".
           - If there is no positive or negative emotional language, set sentiment to "neutral".
           -Billing: charges, invoices, refunds, subscriptions, payments
           -Technical: internet/connectivity, outages, bugs, errors, device/service malfunction
           -Account: login, password, password reset, account access
           -Other: only when none of the previous categories fit
           -Positive: thanks, gratitude, satisfaction, praise, a resolved problem
           -Negative: anger, complaint, frustration, urgent dissatisfaction
           -Neutral: no clear emotional signal
           -Determine sentiment from the customer’s current emotional language,
            not from whether they describe a past technical/billing/account problem.

           -Explicit gratitude or satisfaction, such as “thank you”, means positive,
            even if the message mentions a problem that was already fixed.
        
            Examples:

              Example 1:
               Transcript: Thank you for your help!
                customer_name: Unknown
                   issue_category: other
                   sentiment: positive

                 Example 2:
                 Transcript: I can't connect to the internet.
                  customer_name: Unknown
                 issue_category: technical
                 sentiment: neutral

                   Example 3:
                   Transcript: I'm extremely frustrated because my internet keeps disconnecting.
                    customer_name: Unknown
                     issue_category: technical
                      sentiment: negative

           --- TRANSCRIPT START ---
              {transcript}
           --- TRANSCRIPT END ---
            """
