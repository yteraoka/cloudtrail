import boto3
import datetime
import sys
import argparse
import json

def date_type(date_str):
    return datetime.date.fromisoformat(date_str)

def custom_json(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    else:
        return str(o)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='cloudtrail', description='Search CloudTrail Events')
    parser.add_argument('attributeValue') # lips-github-action
    parser.add_argument('startDate', help='YYYY-MM-DD', type=date_type)
    parser.add_argument('endDate', help='YYYY-MM-DD', type=date_type)
    parser.add_argument('-k', '--attribute-key', choices=['EventId', 'EventName', 'ReadOnly', 'Username', 'ResourceType', 'ResourceName', 'EventSource', 'AccessKeyId'], default='Username')
    args = parser.parse_args()

    print('AttributeKey: {}'.format(args.attribute_key), file=sys.stderr)
    print('AttributeValue: {}'.format(args.attributeValue), file=sys.stderr)
    print('StartTime: {}'.format(datetime.datetime(args.startDate.year, args.startDate.month, args.startDate.day)), file=sys.stderr)
    print('EndTime: {}'.format(datetime.datetime(args.endDate.year, args.endDate.month, args.endDate.day)), file=sys.stderr)

    client = boto3.client('cloudtrail', region_name='ap-northeast-1')
    paginator = client.get_paginator('lookup_events')
    page_iterator = paginator.paginate(
        LookupAttributes=[{'AttributeKey': args.attribute_key, 'AttributeValue': args.attributeValue}],
        StartTime=datetime.datetime(args.startDate.year, args.startDate.month, args.startDate.day),
        EndTime=datetime.datetime(args.endDate.year, args.endDate.month, args.endDate.day))

    i = 0
    for page in page_iterator:
        i = i + 1
        print('page: {}'.format(i), file=sys.stderr)
        # 'NextToken': 'uS7FvxEnAox5Bt8mKbujy80p7RMOCfj+fBpVH4YQyT07pOxF8Lq034PTJ1V/2oWz'
        # 'ResponseMetadata': {
        #   'RequestId': 'f024c8f8-03e5-4a1f-a8fe-808bd7c6a2e2',
        #   'HTTPStatusCode': 200,
        #   'HTTPHeaders': {
        #     'x-amzn-requestid': 'f024c8f8-03e5-4a1f-a8fe-808bd7c6a2e2',
        #     'content-type': 'application/x-amz-json-1.1',
        #     'content-length': '80094',
        #     'date': 'Sun, 05 Jan 2025 15:25:15 GMT'
        #   },
        # 'RetryAttempts': 0
        # }

        #print(page['Events'])
        for event in page['Events']:
            event['CloudTrailEvent'] = json.loads(event['CloudTrailEvent'])
            print(json.dumps(event, default=custom_json, separators=(',', ':')))
            #print(event)

