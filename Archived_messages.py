def show_messages(messages):
    """Display a series of short text messages"""
    print('Displaying all messages')
    for message in messages:
        print(message)

def send_messages(messages,sent_messages):
    """Display messages to be sent"""
    print('\nThese messages are about to be sent:')
    while messages:
        sent_message = messages.pop()
        print(sent_message)
        sent_messages.append(sent_message)


short_messages = ['How are you?','Hello!','Good Day','Stay safe!']
sent_messages = []
show_messages(short_messages)
send_messages(short_messages[:], sent_messages)

print('\nList checks')
print(short_messages)
print(sent_messages)