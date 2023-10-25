import requests

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class RandomUserAction(Action):
    def name(self) -> Text:
        return "RandomUserAction"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(text="Hello, how can I assist you?")
        response = requests.get("https://randomuser.me/api/")
#
        if response.status_code == 200:
            user_data = response.json()["results"][0]
#
            name = user_data["name"]["first"] + " " + user_data["name"]["last"]
            email = user_data["email"]
            gender = user_data["gender"]
#
            message = "Here is a random user:\n\nName: {}\nEmail: {}\nGender: {}".format(name, email, gender)
#
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't generate a random user.")

        return []
