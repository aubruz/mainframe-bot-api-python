import requests
import json


class Client(object):
    """Class that handles calls to and responses from Mainframe API

    http://developer.mainframe.com/#mainframe-server-api
    """

    def __init__(self, bot_secret, base_uri='https://api.mainframe.com/bots/v1/'):
        self.bot_secret = bot_secret
        self.base_uri = base_uri
        self.headers = {
            'Authorization': 'Mainframe-Bot ' + bot_secret,
            'Content-Type': 'application/json; charset=utf-8'
        }

    def send_message(self, conversation_id, message='', subscription_id=None, message_type=None):
        """Send a message in a conversation

        When calling this endpoint, the bot server should provide a subscription_id to indicate how the message
        is relevant to the conversation. While it is possible for the bot to send messages without a
        subscription_id, these messages might be rate-limited or even disabled to prevent abuse.
         """
        data = {'conversation_id': conversation_id, "message": message}

        # if ($message instanceof UIPayload){
        # $json["data"] = $message->toArray();
        # }else{
        # }

        if subscription_id is not None:
            data['subscription_id'] = subscription_id

        if message_type is not None:
            data['type'] = message_type

        return self._make_call('send_message', data)

    def setup_subscription(self, subscription_token, label):
        """Create a subscription"""
        data = {
            'subscription_token': subscription_token,
            'label': label,
        }

        return self._make_call('setup_subscription', data)

    def edit_subscription(self, subscription_token, label):
        """Edit a subscription"""
        data = {
            'subscription_token': subscription_token,
            'label': label,
        }

        return self._make_call('edit_subscription', data)

    def delete_subscription(self, subscription_token, label, message=None):
        """Delete a subscription"""
        data = {
            'subscription_token': subscription_token,
            'label': label,
        }

        if message is not None:
            data['message'] = message

        return self._make_call('delete_subscription', data)

    def _make_call(self, end_point, data):
        return requests.post(self.base_uri + end_point, data=json.dumps(data), headers=self.headers)
