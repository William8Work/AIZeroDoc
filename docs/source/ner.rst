.. AIZero documentation master file, created by
   sphinx-quickstart on Sun Mar 15 16:01:55 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NER (Named Entity Recogition)
=============================

Named entity recognition (NER) , also known as entity chunking/extraction , is a popular technique used in information extraction to identify and segment the named entities and classify or categorize them under various predefined classes. These named entities typically represent real-world objects like people, places, organization, and so on, which are often denoted by proper names.

1. API Accounts and Access Tokens
*********************************

In order to access the AIZero API services, you need to create an account and receive access tokens. The access token needs to be present in every single API calls into AIZero services in order to ensure proper authentication.


2. NER - Named Entity Recognition
*********************************

With a given blob of text, the NER service can return a list of identified entities.

**1.1 NER - API Details**

NER API can be interacted with HTTPS Restful API through standard method.

**API URL**

+----------------------+--------------------------------------------------------+
|Section               |Values                                                  |
+======================+========================================================+
|URL                   |https://nlp.aizero.org/ner                              |
+----------------------+--------------------------------------------------------+
|HTTP Method           |POST                                                    |
+----------------------+--------------------------------------------------------+

**Header Parameters**     

+----------------------+--------------------------------------------------------+
|Key                   |Values                                                  |
+======================+========================================================+
|Content-Type          |application/json                                        |
+----------------------+--------------------------------------------------------+
|Authorization         |token xxxxxxxxxx                                        |
+----------------------+--------------------------------------------------------+

**Required Parameters**

Included in the HTTP REST method, the following parameters are required to make a successful NER API call::

    { 
        "data" : "kubecon 2020 in Boston."
    }


**Status Codes**

Standard HTTP status codes are provided as the results of the API calls::

    200     Status OK. Check the response.json for the results.
    
    404     Unauthorized. Either the Access Code is missing from the header, or the code is invalid.      


**Response Sample**

The NER results are represented in the following response format::

    "text": [extracted-text-from input as name entity],
    "start_char": position1,
    "end_char": position2,
    "label": [NER type]
    
The label will return one of the following type.


**1.2 Entity Types Supported**

.. csv-table:: NER Entity Types
   :header: "TYPE", "DESCRIPTION"
   
   "PERSON", "People, including fictional."
   "NORP", "Nationalities or religious or political groups."
   "FAC", "Buildings, airports, highways, bridges, etc."
   "ORG", "Companies, agencies, institutions, etc."
   "GPE", "Countries, cities, states."
   "LOC", "Non-GPE locations, mountain ranges, bodies of water."
   "PRODUCT", "Objects, vehicles, foods, etc. (Not services.)"
   "EVENT", "Named hurricanes, battles, wars, sports events, etc."
   "WORK_OF_ART", "Titles of books, songs, etc."
   "LAW	Named", "documents made into laws."
   "LANGUAGE", "Any named language."
   "DATE", "Absolute or relative dates or periods."
   "TIME", "Times smaller than a day."
   "PERCENT", "Percentage, including ”%“."
   "MONEY", "Monetary values, including unit."
   "QUANTITY", "Measurements, as of weight or distance."
   "ORDINAL", "first, second, etc."
   "CARDINAL", "Numerals that do not fall under another type."


**1.3 Code Snippet**

The following sample codes are for your reference only. 

Python::
    
    import sys
    import json
    import flaskapi
    
    app = FlaskAPI(__name__)
    
    APP_URL = 'https://nlp.aizero.org/ner'
    
    # replace the access_token with the real one. See the Account section for more details.
    header = { 'Authorization' : 'token {}'.format(access_token) }
        
    test_content = { 
		"content": {
			"az_text": "Firing Mr. Strzok, however, removes a favorite target of Mr. Trump from the ranks of the F.B.I. and gives Mr. Bowdich and the F.B.I. director, Christopher A. Wray, a chance to move beyond the president\'s ire.",
			"az_file": "empty-url"
		}
	}


    response = app.post(APP_URL,
				data = json.dumps(test_content),
				content_type = 'application/json',
				headers = header)
    result_data = json.loads(response.json)
    

**Sample Response**

An response sample is:: 

        {
          "az_result": [
            {
              "text": "Strzok",
              "start_char": 11,
              "end_char": 17,
              "label": "PERSON"
            },
            {
              "text": "Trump",
              "start_char": 61,
              "end_char": 66,
              "label": "PERSON"
            },
            {
              "text": "F.B.I.",
              "start_char": 89,
              "end_char": 95,
              "label": "ORG"
            },
            {
              "text": "Bowdich",
              "start_char": 110,
              "end_char": 117,
              "label": "PERSON"
            },
            {
              "text": "F.B.I.",
              "start_char": 126,
              "end_char": 132,
              "label": "ORG"
            },
            {
              "text": "Christopher A. Wray",
              "start_char": 143,
              "end_char": 162,
              "label": "PERSON"
            }
          ],
          "az_process": {
            "begin_time": "2020-03-23 00:58:39.447206",
            "end_time": "2020-03-23 00:58:40.388193",
            "process_time": "0:00:00.940987"
          },
          "xreference": {
            "x-id": "something"
          }
        } 






