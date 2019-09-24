## story_1
* greet
 - utter_greet
 - utter_ask_howcanhelp
* inform{"drug_name": "Lipitor", "drug_strength":"5 mg", "drug_quantity":"100"}
 
* inform{"drug_name": "Lipitor", "drug_strength":"5 mg", "drug_quantity":"100"}
 - utter_on_it
 - utter_ask_quantity
* inform{"quantity": "100mg"}
 - utter_ask_address_on_file
* inform{"address_on_file": "yes"}
* deny
 - utter_search_prescription
 - action_search_prescription_drug_list
 - action_order_drugs
 - action_suggest
* affirm
 - utter_ack_order
* thankyou
 - utter_goodbye