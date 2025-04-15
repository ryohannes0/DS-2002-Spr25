#!/bin/bash

AWS_REGION="us-east-1"

aws s3 cp "$1" s3://"$2"/ --region "$AWS_REGION"
aws s3 presign s3://"$2"/"$1" --expires-in "$3" --region "$AWS_REGION"

