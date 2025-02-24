#!/bin/bash

# Compress the flask-app directory
echo "packaging app"
zip -r flask-app.zip ./ -x "*.zip"

# Obtain the artifact bucket name from the CloudFormation stack
ARTIFACT_BUCKET=$(aws cloudformation describe-stacks --stack-name AppSecWorkshopStack --query 'Stacks[0].Outputs[?starts_with(OutputKey, `DevToolsArtifactBucket`)].OutputValue' --output text)

# Upload the compressed file to the artifact bucket
echo "uploading to artifact bucket"
aws s3 cp flask-app.zip s3://$ARTIFACT_BUCKET/flask-app.zip

echo "Done!"