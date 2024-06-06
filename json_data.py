import re
import os
import json
import pandas as pd

from setting import OUTPUT_FOLDER

def get_output_path(url:str):
    output_path = url.replace("https://", "").replace("/", "_").replace(".", "-")
    output_path = os.path.join(os.getcwd(), OUTPUT_FOLDER, output_path)
    return output_path

def clean_data(results, save=False, output_path='data.json'):
    cleaned_data = []
    for result in results:
        result = str(result)
        result = re.sub(r'<.*?>', '\n\n', result)
        result = re.sub('\n\n\n+', '\n\n', result)
        result = re.sub('^\n+', '', result)
        result = re.sub('\n+$', '', result)
        cleaned_data.append(result)
    
    if save:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

    return cleaned_data

def json_to_excel(json_data, output_path='output.xlsx'):
    df = pd.DataFrame(json_data)
    df.to_excel(output_path, index=False)