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

print(result_data)

