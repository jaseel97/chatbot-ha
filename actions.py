from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker

# import Levenshtein
# import operator
import requests
import json

from data.districts import get_district_map
from data.towns import get_town_map

class HaForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ha_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        #return ["property_action", "property_type", "property_class", "district", "town"]
        if tracker.get_slot('property_type') in ['house','home','villa','houses','villas','appartment','appartments']:
            return ["property_action", "property_type", "district", "town"]
        else:
            return ["property_action", "property_type", "property_class", "district", "town"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_form_accepted")
        return []

class ActionFetchProperties(Action):

    def name(self) -> Text:
        """Unique identifier of the custom action"""
        return "action_fetch_properties"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Encode slot values and make api call to retrieve properties"""
        
        property_action = tracker.get_slot("property_action")
        property_type = tracker.get_slot("property_type")

        property_class = ''
        if property_type in ['house','home','villa','houses','villas','appartment','appartments']:
            property_class = 'residential'
        elif property_type in ['shop','shops','office','offices']:
            property_class = 'residential'
        else:
            property_class = tracker.get_slot("property_class")

        district = tracker.get_slot("district")
        town = tracker.get_slot("town")

        api_endpoint = 'http://api.helloaddress.com/v1/search'

        property_action_suffix_map = {
            'rent':'propertyAction=R',
            'buy':'propertyAction=S',
            'lease':'propertyAction=L'
        }
        
        property_suffix_map = {
            'residential':{
                'house':'propertyType=RA,RH',
                'appartment':'propertyType=RA',
                'land':'propertyType=RL'
            },
            'commercial':{
                'land':'propertyType=CL',
                'shop':'propertyType=CS',
                'office':'propertyType=CF',
                'building':'propertyType=CB'
            },
            'industrial':{
                'land':'propertyType=IL',
                'building':'propertyType=IB'
            },
            'agricultural':{
                'land':'propertyType=AL'
            }
        }

        api_endpoint = api_endpoint + '?' +\
        property_action_suffix_map[property_action] + '&' + \
        property_suffix_map[property_class][property_type] + '&' +\
        'districtId=' + get_district_map()[district] + '&' + \
        'townId=' + get_town_map()[get_district_map()[district]][town]

        properties_json = requests.get(api_endpoint)
        properties = json.loads(properties_json.text)['properties']

        for property in properties:
            property_link = 'http://www.helloaddress.com/property/P'+property['id']
            property_name = property['name']
            dispatcher.utter_message(property_name)
            dispatcher.utter_message("link : "+property_link+"\n")
        # print(property_action,property_type,property_class,district,town)
        # dispatcher.utter_message(template="utter_goodbye")
