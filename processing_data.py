import re, json


def processing_messages(list_of_payload_messages):
    try:

        list_of_dict = []
        phone_regex = re.compile(
            r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        postalcode_regex = re.compile(r'\b(?!.{0,7}[DFIOQU])[A-VXY]\d[A-Z][^-\w\d]\d[A-Z]\d\b')

        for message in list_of_payload_messages:
            message_dict = {}
            phone = phone_regex.search(message)
            if phone:
                message_dict["phone"] = phone[0]

            email = email_regex.search(message)
            if email:
                message_dict["email"] = email[0]

            postalcode = postalcode_regex.search(message)
            if postalcode:
                message_dict["postalcode"] = postalcode[0]
            list_of_dict.append(message_dict)

        return 0, list_of_dict
    except Exception:
        return 1, 'Processing message has got failed, please validate !!!'