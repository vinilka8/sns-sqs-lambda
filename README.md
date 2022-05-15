# sns-sqs-lambda

Lambda_handler: Main centric function for other utils methods, 
  1. It's prepare the list of messages and pass it for processing
  2. Call manage_put_item to store pre-processed data in DynamoDB

Processing_messages: Function that pre-process messages 
  1. Using regex, it finds phone, email, postalcode and stores it in list of Dictionaries

Manage_put_item: Function that creates a corpus for butch upload
  1. Generate uuid for the unique key
  2. Generates the corpus for butch upload
  3. Put the induvidual item to DynamoDB
