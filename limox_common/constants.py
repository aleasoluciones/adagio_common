# -*- coding: utf-8 -*-


#---- Job Result outcomes
SUCCESS_JOB_RESULT = 'success'
FAIL_JOB_RESULT = 'fails'

#---- Action names
PROVISION_ACTION = 'provision'
DEPROVISION_ACTION = 'deprovision'
SERVICE_CHANGE_ACTION = 'service_change'
SERVICE_CHANGE_PROVISION_ACTION = 'service_change_provision_action'
SERVICE_CHANGE_DEPROVISION_ACTION = 'service_change_deprovision_action'

#---- Event Exchange
PROVISION_EXCHANGE = 'events_delayed'
DIAGNOSTIC_EXCHANGE = 'events'

#---- Event Names
PROVISION_JOB_EVENT_NAME = 'provision.new'
DEPROVISION_JOB_EVENT_NAME = 'provision.remove'
JOB_RESULT_EVENT_NAME = 'job_result'
PROVISION_RETRY_EVENT_NAME = 'provision.retry'

EVENT_WITH_NO_DELAY = 0
