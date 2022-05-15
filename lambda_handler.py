from __future__ import print_function
import processing_data, managing_data
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info('START - reading and appending messages for butch upload.')
        list_of_payload_messages = []
        for record in event['Records']:
            list_of_payload_messages.append(record["body"]["Message"])
        logger.info('END - reading and appending messages.')
        
        logger.info('NEXT - processing_data.processing_messages to be executed ... ')
        error_code, data_or_errmsg = processing_data.processing_messages(list_of_payload_messages)
        if error_code != 0:
            raise Exception(data_or_errmsg)
        else:
            logger.info('END - processing messages has been successful.')
        
        logger.info('NEXT - managing_data.manage_put_item to be executed ... ')
        error_code, data_or_errmsg = managing_data.manage_put_item(data_or_errmsg)
        if error_code != 0:
            raise Exception(data_or_errmsg)
        else:
            logger.info('END - putting items to DynamoDB has been successful.')
    except Exception:
        raise Exception('Lambda Handler has got failed due to messaging processing or put item into DB')
