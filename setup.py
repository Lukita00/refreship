from dotenv import load_dotenv
import os

load_dotenv()

AZURE_AUTOMATION = os.getenv("AZURE_AUTOMATION")
NOME             = os.getenv("NOME")