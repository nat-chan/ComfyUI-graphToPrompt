import argparse
import json

import requests


def post_json_to_server(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    response = requests.post("http://localhost:8189/graph_to_prompt", json=data)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response json: {response.json()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Post JSON to server")
    parser.add_argument("filepath", type=str, help="Path to the JSON file to post")
    args = parser.parse_args()
    post_json_to_server(args.filepath)
