import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'cloudai-vision-results')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    image_key = event['pathParameters']['imageKey']
    
    try:
        response = table.get_item(Key={'imageKey': image_key})
        item = response.get('Item', {})
        
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Image analysis not found'})
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps({'imageKey': image_key, 'labels': item['labels']})
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
