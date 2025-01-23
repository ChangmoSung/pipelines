import os
import requests
from typing import Literal, List, Optional
from datetime import datetime
from pymongo import MongoClient

from blueprints.function_calling_blueprint import Pipeline as FunctionCallingBlueprint


class Pipeline(FunctionCallingBlueprint):
    class Tools:
        def __init__(self, pipeline) -> None:
            self.pipeline = pipeline

        def get_current_time(
            self,
        ) -> str:
            """
            Get the current time.

            :return: The current time.
            """

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            return f"Current Time = {current_time}"

        def calculator(self, equation: str) -> str:
            """
            Calculate the result of an equation.

            :param equation: The equation to calculate.
            """

            # Avoid using eval in production code
            # https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
            try:
                result = eval(equation)
                return f"{equation} = {result}"
            except Exception as e:
                print(e)
                return "Invalid equation"

    def __init__(self):
        super().__init__()
        # Optionally, you can set the id and name of the pipeline.
        # Best practice is to not specify the id so that it can be automatically inferred from the filename, so that users can install multiple versions of the same pipeline.
        # The identifier must be unique across all pipelines.
        # The identifier must be an alphanumeric string that can include underscores or hyphens. It cannot contain spaces, special characters, slashes, or backslashes.
        # self.id = "my_tools_pipeline"
        self.name = "My Tools Pipeline"
        self.valves = self.Valves(
            **{
                **self.valves.model_dump(),
                "pipelines": ["*"],  # Connect to all pipelines
            },
        )
        self.tools = self.Tools(self)

        self.client = MongoClient("mongodb+srv://zofiq-pod:4HQy7EIi4TNby6cK@zofiq-mongo.9pudj.mongodb.net/?appName=Zofiq-Mongo")
        self.db = self.client["connectwiseData"]
        self.collection = self.db["tickets"]

    def run(self, prompt, context):
        print('Testing run method')
        """
        This method runs when the pipeline is called.
        It queries MongoDB based on user prompt and returns the results.
        """
        query = {"status": "active"}  # Example query, modify based on the prompt
        
        result = self.collection.find(query)
        print('Testing pipeline Mongo result', result)

        return list(result)
