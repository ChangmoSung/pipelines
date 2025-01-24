import os
import requests
from typing import Literal, List, Optional
from datetime import datetime
from pymongo import MongoClient

from blueprints.function_calling_blueprint import Pipeline as FunctionCallingBlueprint

result = {}
class Pipeline(FunctionCallingBlueprint):
    class Tools:
    def __init__(self):
        self.citation = True
        self.description = "A tool to fetch active tickets from MongoDB."

    def run(self, prompt: str, context: dict) -> list:
        print("Testing pipelines")

        # Return results
        return True
