
import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["review_text"],
                    "Values": [ [ "value" ], [ "value" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/41654fb2238f449daf8dc7954f22ee9b/services/128f31001e794cd19ab042010d1f4a0e/execute?api-version=2.0&details=true'
api_key = 'FrykEwu75lBeqhdG/Iz8NdwmY0GOrAJVNl+f+BcXCPChMrDkYRL4S/F7E33YxFRkJrese1giJ9NrWOBxJjWgag==' # API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))   