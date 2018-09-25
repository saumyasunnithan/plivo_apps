from plivo import plivoxml

response = (plivoxml.ResponseElement()
            .add(plivoxml.SpeakElement('Go Green, Go Plivo.')))
print(response.to_string())

