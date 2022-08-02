# ARCHIVED: No longer maintained

# AWS GuardDuty Threat Intel List Lambda Updater

[Threat Intel Lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload_lists.html) are not automatically updated on AWS [GuardDuty](https://aws.amazon.com/guardduty/). In order for GuardDuty to have the lastest threat intel, we have to manually update each list. 

## Getting Started

If you already have serverless and active GuardDuty threat intel lists, you can run this lambda function locally. If you want to setup a threat intel list please refer to our [blog entry](https://www.seclytics.com/blog/2018/07/16/amazon-guardduty-threat-list-integration/).

To test the function localy you can run:

```
serverless invoke local -f update_threat_intel_sets
```

### Prerequisites

Requires serverless and a newer version of boto3

### Installing

```
npm install -g serverless
pip install boto3 --upgrade
```

## Deployment

By default, the lambda function will be deployed to *us-east* and will be executed every 30 minutes.

```
serverless deploy 
```

## Built With

* [Serverless Framework](https://github.com/serverless/serverless)

## Authors

* **Jason Pope** - [cowholio4](https://github.com/cowholio4)
