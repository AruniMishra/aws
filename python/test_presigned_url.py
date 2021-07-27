# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Unit tests for presigned_url.py functions.
"""

import boto3
import logging
import presigned_url

logger = logging.getLogger(__name__)


def test_generate_presigned_url():
    s3_client = boto3.client('s3')
    client_method = 'get_object'
    method_params = {'Bucket': 'arunipresigned', 'Key': 'prince.jpg'}
    expires = 1000

    got_url = presigned_url.generate_presigned_url(
        s3_client, client_method, method_params, expires)
    

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    print("got_url")
    print(got_url)
    assert 'arunipresigned' in got_url
    assert 'prince.jpg' in got_url


if __name__ == '__main__':
    test_generate_presigned_url()