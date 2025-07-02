!pip install ibm-cos-sdk pandas
import ibm_boto3
from botocore.client import Config
import pandas as pd
import types
import time
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as Params

storage = ibm_boto3.client(
    service_name='s3',
    ibm_api_key_id='CKEbkcBVEyB2BxKKxggRzWC_hoDfYcw15eJjzZfcVDyq',
    ibm_auth_endpoint='https://iam.cloud.ibm.com/oidc/token',
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud'
)

bucket_name = 'bucket-5eo7j1vg91wj5n6'
csv_file_key = 'college_feedback.csv'

csv_stream = storage.get_object(Bucket=bucket_name, Key=csv_file_key)['Body']
if not hasattr(csv_stream, 'iter'):
    def _iter(self): return 0
    csv_stream.iter = types.MethodType(_iter, csv_stream)

df = pd.read_csv(csv_stream)

wml_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "qBwroANVb2onAG4Mva7fsLh-reNWgAOGkerq7BXT8iGN"
}

project_id = "bf003078-b30e-4bf0-813b-125bc42d1817"

text_model = Model(
    model_id="google/flan-t5-xxl",
    params={Params.MAX_NEW_TOKENS: 10},
    credentials=wml_credentials,
    project_id=project_id
)

prompt_base = """
Categorize this student feedback into one of the following groups:
Academics, Facilities, or Administration.

Examples:
"The instructors explain topics with clarity." → Academics
"The syllabus needs to be reduced in size." → Academics
"The hostel bathrooms are cleaned daily." → Facilities
"The food in the canteen lacks hygiene." → Facilities
"Staff members are helpful with queries." → Administration
"There are delays in document processing." → Administration

Now categorize this:
"{input}" →
"""

categories = []
for text in df['Feedback']:
    full_prompt = prompt_base.replace("{input}", text)
    try:
        result = text_model.generate_text(prompt=full_prompt)
        output = ""
        if isinstance(result, dict):
            output = result.get("generated_text", "")
            if not output and "results" in result:
                output = result["results"][0]["generated_text"]
        elif isinstance(result, str):
            output = result
        categories.append(output.strip())
    except:
        categories.append("Error")
    time.sleep(1)

df['Category'] = categories
output_file = f"feedback_output_{int(time.time())}.csv"
df.to_csv(output_file, index=False)

storage.upload_file(Filename=output_file, Bucket=bucket_name, Key=output_file)
print(f"Output uploaded: {output_file}")
