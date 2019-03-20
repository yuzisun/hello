from bloomberg.blambda.runtime import lambda_logging

def handler(event, context):
    log = lambda_logging.get_logger("upper")
    log.info(event)
    for item in context.items():
        log.info(item)
    return event.upper()
