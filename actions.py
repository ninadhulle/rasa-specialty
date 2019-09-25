from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class DrugsAPI(object):
    def search(self, info):
        return "Tylenol"


class ActionSearchPresctionDrugList(Action):
    def name(self):
        return "action_search_prescription_drug_list"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for drugs in prescription")
        drugs_api = DrugsAPI()
        drugs = drugs_api.search(tracker.get_slot("prescription_no"))
        return [SlotSet("matches", drugs)]


