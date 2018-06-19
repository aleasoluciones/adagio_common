# -*- coding: utf-8 -*-


#---- Job Result outcomes
SUCCESS_JOB_RESULT = 'success'
FAIL_JOB_RESULT = 'fails'

#---- Action names
PROVISION_ACTION = 'provision'
DEPROVISION_ACTION = 'deprovision'

#---- Event Exchange
PROVISION_EXCHANGE = 'events_delayed'
DIAGNOSTIC_EXCHANGE = 'events'

#---- Event Names
JOB_RESULT_EVENT_NAME = 'job_result'
PROVISION_RETRY_EVENT_NAME = 'provision.retry'

EVENT_WITH_NO_DELAY = 0
