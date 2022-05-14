from __future__ import print_function
import processing_data, managing_data

def lambda_handler(event, context):
    try:
        list_of_payload_messages = []
        for record in event['Records']:
            list_of_payload_messages.append(record["body"]["Message"])

        error_code, data_or_errmsg = processing_data.processing_messages(list_of_payload_messages)
        if error_code != 0:
            raise Exception(data_or_errmsg)

        error_code, data_or_errmsg = managing_data.manage_put_item(data_or_errmsg)
        if error_code != 0:
            raise Exception(data_or_errmsg)

        #error_code, data_or_errmsg = processing_data.put_item(data_or_errmsg)
        #if error_code != 0:
        #    raise Exception(data_or_errmsg)
    except Exception:
        raise Exception('Lambda Handler has got failed due to messaging processing or put item into DB')