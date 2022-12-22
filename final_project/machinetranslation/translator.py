import json
import ibm_watson
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']



authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-10-18',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr'
).get_result()

    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en'
).get_result()
    return englishText
