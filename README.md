# sns-sqs-lambda

Event Driven Message router Assignment

For this assignment I have choised PUBLISHER -> SNS Topic -> SQS (Queue) -> Lambda data flow/architecture, given the fact that we could receive over 1000 messages from publisher, we need to ensure that no of messages is lost and all of them with 100% pre-processed and stored. 


Lambda_handler: Main centric function for other utils methods, 
  1. It's prepare the list of messages and pass it for the pre-processing
  2. Call manage_put_item to store pre-processed data in DynamoDB (data is ready for batching update to DB, but only single unit update is achieved)

Processing_messages: Function that pre-process messages 
  1. Using regex, it finds phone, email, postalcode and stores it in list of Dictionaries

Manage_put_item: Function that creates a corpus for butch upload
  1. Generate uuid for the unique key
  2. Generates the corpus for butch upload
  3. Put the induvidual item to DynamoDB
