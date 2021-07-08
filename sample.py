import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from pandas import json_normalize


url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/3d452364-2612-44ab-9a6f-4a96e62b81e6'
apikey_lt='GTfwYu2q4V_HIVjUYT65p39ACFYT060tqNuKeWeSzEyS'
version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

# function to translate English to French

def englishtofrench(input):
    if(input==""):
        return("No text provided")

    translation = language_translator.translate(\
        text=input, model_id='en-fr')
    
    translation_result = translation.get_result()
    french_translation = translation_result['translations'][0]['translation']
    
    return french_translation

sample = englishtofrench("Hi there")
print(sample)