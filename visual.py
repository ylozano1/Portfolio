import json
from watson_developer_cloud import VisualRecognitionV3

# Create an instance of your Watson Visual Recognition service
instance = VisualRecognitionV3(version='2016-05-20', api_key='0512ae9bc7d86ddb2dfbfed98961356a00d508ec')

# Classify the image using Watson Visual Recognition
img = instance.classify(images_url='https://pbs.twimg.com/media/Ccs9lxVUUAEhp3C.jpg')

# Print the JSON results
#print(json.dumps(img, indent=2))

# Format the results to be more readable
for results in img['images'][0]['classifiers'][0]['classes']:
    print('\n There is a ' + str(round((results['score']*100),1)) + ' percent chance the image contains: '+ results['class'])
