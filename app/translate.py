# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
import json
from flask import jsonify
"""
-------------------------------------------------
   File Name：     translate
   Description :
   Author :       burt
   date：          2019-01-31
-------------------------------------------------
   Change Activity:
                   2019-01-31:
-------------------------------------------------
"""


def translate(text, source_language, dest_language):
    try:
        cred = credential.Credential("AKIDsTosqYgBzWOzJNoQMYrt8ZsuSpxDI1OV", "4ANqiNmw9F6h5jAMjvnPoUrHVwfQ8j49")
        http_profile = HttpProfile()
        http_profile.endpoint = "tmt.ap-beijing.tencentcloudapi.com"

        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile
        client = tmt_client.TmtClient(cred, "ap-beijing", client_profile)

        req = models.TextTranslateRequest()
        param_map = {
            "SourceText": text,
            "Source": source_language,
            "Target": dest_language,
            "ProjectId": 1984
        }

        params = json.dumps(param_map)
        print('params:', params)
        req.from_json_string(params)

        resp = client.TextTranslate(req)
        print('the final result:', resp.to_json_string())

        return jsonify(json.loads(resp.to_json_string()))

    except TencentCloudSDKException as err:
        print(err)
