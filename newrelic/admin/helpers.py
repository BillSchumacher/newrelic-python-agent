from newrelic.admin import usage


def initialize_usage(usage_name, args):
    import os
    import sys
    import logging

    if len(args) == 0:
        usage(usage_name)
        sys.exit(1)

    from newrelic.config import initialize
    from newrelic.core.config import global_settings

    log_level = logging.DEBUG
    log_file = get_log_file_path(args)
    try:
        os.unlink(log_file)
    except Exception:
        pass

    config_file = args[0]
    environment = os.environ.get('NEW_RELIC_ENVIRONMENT')

    if config_file == '-':
        config_file = os.environ.get('NEW_RELIC_CONFIG_FILE')

    initialize(config_file, environment, ignore_errors=False,
               log_file=log_file, log_level=log_level)

    return global_settings()


def get_log_file_path(args):
    if len(args) >= 2:
        log_file = args[1]
    else:
        log_file = '/tmp/python-agent-test.log'
    return log_file
