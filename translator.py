""" program to translate language """

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

URL_LT='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/3d452364-2612-44ab-9a6f-4a96e62b81e6'
APIKEY_LT='GTfwYu2q4V_HIVjUYT65p39ACFYT060tqNuKeWeSzEyS'
VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)

def englishtofrench(sample_text):

    """ english to french translation """

    if sample_text=="":
        return "No input provided"

    translation = language_translator.translate(\
        text=sample_text, model_id='en-fr')
    translation_result = translation.get_result()
    french_translation = translation_result['translations'][0]['translation']
    return french_translation



def englishtogerman(sample_text):

    """ English to german translation """

    if sample_text=="":
        return "No input provided"

    translation = language_translator.translate(\
        text=sample_text, model_id='en-de')
    translation_result = translation.get_result()
    german_translation = translation_result['translations'][0]['translation']
    return german_translation

sample1=englishtogerman("hello")
sample2=englishtofrench("hello")
print(sample2)
print(sample1)
