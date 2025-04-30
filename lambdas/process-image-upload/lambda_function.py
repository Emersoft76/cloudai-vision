import boto3
import json
import os

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'cloudai-vision-results')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Get bucket and image key from S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    image_key = event['Records'][0]['s3']['object']['key']
    
    # Rekognition: Detect labels
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': image_key}},
        MaxLabels=10,
        MinConfidence=75
    )
    
    labels = [label['Name'] for label in response['Labels']]
    
    # Save result in DynamoDB
    table.put_item(
        Item={
            'imageKey': image_key,
            'labels': labels
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Image processed', 'labels': labels})
    }
