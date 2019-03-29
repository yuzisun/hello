def predict(event, context):
    log.info(event)
    for item in context.items():
        log.info(item)
    return event.upper()
