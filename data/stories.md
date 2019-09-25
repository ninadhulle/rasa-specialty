## story_1
* greet
 - utter_greet
 - utter_ask_howcanhelp
 - utter_on_it
* inform{"prescription_count": "one", "prescriber_count":"two"}
 - utter_search_prescription
 - utter_prescription_options
* inform{"drug_name": "Lipitor", "drug_strength":"5 mg", "drug_quantity":"100"}
 - utter_ask_prescription_drug_name
* inform{"drug_quantity": "100mg", "drug_quantity_status":"Yes"}
 - utter_ask_prescription_drug_quantity
* inform{"addresses": "12, PFizer Ln, New Haven, CT"} 
 - utter_ask_address_on_file
* inform{"refill_confirmation": "yes"}
 - utter_ask_prescription_refill_confirmation
 - utter_prescription_refill_confirmation
 - utter_ask_further_query
* deny
 - utter_search_prescription
 - action_search_prescription_drug_list
 - action_order_drugs
* affirm
 - utter_ack_order
* thankyou
 - utter_goodbye