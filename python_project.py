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

print(language_translator)

(json_normalize(language_translator.list_identifiable_languages().get_result(), "languages"))

test_text="hello how are you"

translation1 = language_translator.translate(\
    text=test_text, model_id='en-fr')

translation_en_fr = translation1.get_result()

french_translation =translation_en_fr['translations'][0]['translation']
print(french_translation)

translation2 = language_translator.translate(\
    text=test_text, model_id='en-de')

translation_en_gr = translation2.get_result()

german_translation = translation_en_gr['translations'][0]['translation']

print(german_translation)