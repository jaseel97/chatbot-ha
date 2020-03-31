## happy path
* greet
    - utter_greet
* search_property
    - ha_form
    - form{"name": "ha_form"}
    - form{"name": null}
    - action_fetch_properties
* thank
    - utter_welcome

## unhappy path
* greet
    - utter_greet
* search_property
    - ha_form
    - form{"name": "ha_form"}
* chitchat
    - utter_chitchat
    - ha_form
    - form{"name": null}
    - action_fetch_properties
* thank
    - utter_welcome
* goodbye
    - utter_goodbye

## very unhappy path
* greet
    - utter_greet
* search_property
    - ha_form
    - form{"name": "ha_form"}
* chitchat
    - utter_chitchat
    - ha_form
* chitchat
    - utter_chitchat
    - ha_form
* chitchat
    - utter_chitchat
    - ha_form
    - form{"name": null}
    - action_fetch_properties
* thank
    - utter_welcome

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## chitchat
* chitchat
  - utter_chitchat

## say hi and bye
* greet
 - utter_greet
* goodbye
 - utter_goodbye

## straigh to search
* search_property
    - ha_form
    - form{"name": "ha_form"}
    - form{"name": null}
    - action_fetch_properties