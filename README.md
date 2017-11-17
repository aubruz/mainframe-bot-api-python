# mainframe-bot-api
A python 2/3 [package](https://pypi.python.org/pypi/mainframe-bot-api) that aims to use the mainframe bot api easily.
You can use it to send messages, setup/edit/remove subrcriptions. You can build the UI response in a human read

You can find the documentation of the mainframe API [here](http://developer.mainframe.com/?http#mainframe-server-api).

If you find any bug feel free to fork the project and make a PR. Or write me an email to
[dev@jaquier.co](mailto:dev@jaquier.co).

## How to install it
With pypi:

`pip install mainframe-bot-api` or `pip3 install mainframe-bot-api` for python 3.

Then `from mainframe import Client` or any other classes that you need.

## How to use the client
### Create client
``` 
client = Client(bot_secret)
```
You can specify the API url if you want to use another the stagging one. The default one is 
"https://api.mainframe.com/bots/v1/".
```
client = Client(bot_secret, 'https://api-staging.mainframe.com/bots/v1/')
``` 

### Send message
```
client.send_message(conversation_id, 'Hello World!!')
```

### Setup subscription
```
client.setup_subscription(subscription_token, label)
```

### Edit subscription
``` 
client.edit_subscription(subscription_token, label)
```

### Delete subscription
``` 
client.delete_subscription(conversation_id, subscription_id)
```
You can add an optional message to post to the conversation (to explain the reason for removal)
``` 
client.delete_subscription(conversation_id, subscription_id, message)
```

## Response
The mainframe-bot-api package uses requests to perform the api calls.

```
response = Client.setup_subscription(subscription_token, label)

if response.status_code == 200:
    // Do something
```
