# -*- coding: utf-8 -*-


#---- Job Result outcomes
SUCCESS_JOB_RESULT = 'success'
FAIL_JOB_RESULT = 'fails'

#---- Action names
PROVISION_ACTION = 'provision'
DEPROVISION_ACTION = 'deprovision'
SERVICE_CHANGE_ACTION = 'service_change'
UPDATE_CUSTOMER_PON_INFO_ACTION = 'update_customer_pon_info'
UPDATE_CUSTOMER_SERIALNUMBER_ACTION = 'update_customer_serialnumber'

#---- Event Exchange
PROVISION_EXCHANGE = 'events_delayed'
DIAGNOSTIC_EXCHANGE = 'events'

#---- Event Names
PROVISION_JOB_EVENT_NAME = 'provision.new'
DEPROVISION_JOB_EVENT_NAME = 'provision.remove'
JOB_RESULT_EVENT_NAME = 'job_result'
PROVISION_RETRY_EVENT_NAME = 'provision.retry'

EVENT_WITH_NO_DELAY = 0
