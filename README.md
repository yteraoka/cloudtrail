# cloudtrail

CloudTrail のデータを取得するスクリプト

boto3 cloudtrail [lookup_events](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail/client/lookup_events.html)

[paginator](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html)

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
$ python cloudtrail.py --help
usage: cloudtrail [-h] [-k {EventId,EventName,ReadOnly,Username,ResourceType,ResourceName,EventSource,AccessKeyId}]
                  attributeValue startDate endDate

Search CloudTrail Events

positional arguments:
  attributeValue
  startDate             YYYY-MM-DD
  endDate               YYYY-MM-DD

options:
  -h, --help            show this help message and exit
  -k, --attribute-key {EventId,EventName,ReadOnly,Username,ResourceType,ResourceName,EventSource,AccessKeyId}
```
