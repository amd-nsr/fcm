import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("PATH_TO_FIREBASE_CREDENTIALS_FILE/serviceAccountKey/let-s-diet-firebase-adminsdk-b3jd6-8e5e0d7271.json")
firebase_admin.initialize_app(cred)

def send_push_by_token(title, msg, registration_token, dataObject=None):
    '''
        This function uses firebase-admin sdk to send a message using firebase cloud messaging
        The function uses registration_token to send the message to certin app 
    '''
    
    # Create a MulticastMessage object from the messaging module
    message = messaging.MulticastMessage(notification=messaging.Notification(title=title,
                                                                             body=msg),
                                        data=dataObject,
                                        tokens=registration_token,)

    # Send a message to the device corresponding to the provided registration token.
    # Response is a message ID string.
    response = messaging.send_multicast(message)
    print('Successfully sent message:', response)


def send_push_by_topic(title, body, topic):
    '''
        This function uses firebase-admin sdk to send a message using firebase cloud messaging
        The function uses topic_name to send the message to certin app 
    '''
    
    # Create a Message object from the messaging module
    message = messaging.Message(notification = messaging.Notification(title = title,
                                                                      body = body),
                                topic = topic,)
    # Send a message to the devices subscribed to the provided topic.
    # Response is a message ID string.
    response = messaging.send(message)
    print('Successfully sent message:', response)


if __name__ =="__main__":
    
    # Test the two functions
    
    title="Message Title
    msg = "Best regardes ^_-"
    
    registration_token = ["THE_DEVICE_TOKEN"]    
    topic = 'TOPIC_TO_LISTEN'
    
    send_push_by_token(title, msg, registration_token)
    send_push_by_topic(title, msg, topic )
