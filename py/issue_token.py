# coding=utf-8
from api.wallet import WalletClient
import json
import time
from rest.api.api import Client
ent_sign_param = {
    "creator": "did:axn:17e8db57-a0fa-4028-b17f-802d01602194",
    "nonce": "0",
    "privateB64": "lgdYjMbh7BKCeGxmJrempaP+/cDGMy5StdjM4ZexB0/Ku8V1uI81OlhKdnsCJVqTrXe2vGWKtXR+ciuozCgqjQ=="
}

client = Client(
    "qYIwhZPTp1532489219", # eg: "z_pGym-Tp15288809805" # 企业用户申请的API-KEY
    "/usr/local/lib/python2.7/dist-packages/py_common-2.0.1-py2.7.egg/cryption/ecc/certs", # eg: /usr/local/lib/python2.7/site-packages/py_common-1.5.0-py2.7.egg/cryption/ecc/certs
    ent_sign_param,
    "http://139.198.15.132:9143")

walletclient = WalletClient(client)

# header {"Bc-Invoke-Mode": "sync"} for sync invoke mode. {} or header {"Bc-Invoke-Mode": "async"} for async invoke mode.
# read wallet-sdk-py README "Using callback URL to receive blockchain transaction event" for more details
header = {"Bc-Invoke-Mode": "sync"}
payload = {
    "issuer": "did:axn:17e8db57-a0fa-4028-b17f-802d01602194", # 数字凭证的发行方钱包DID
    "owner": "did:axn:17e8db57-a0fa-4028-b17f-802d01602194", # 数字资产的持有人钱包ID，如企业用户钱包DID(did:axn:***2fc68-f51e-4aff-b6e4-427cce3ed1af)
    "asset_id": "did:axn:9b906590-1c93-4734-8cf6-473995fbdfca", # 创建数字资产存证接口返回的poe_id,如：did:axn:***a94a9-eff4-4f15-88bf-f2054701e87c
    "amount": 2000, # 发行金额
     "fee": {
         "amount": 10
     } # 发行手续费、可不填
 }

params = {
    "creator": "did:axn:17e8db57-a0fa-4028-b17f-802d01602194", # 数字资产的持有人钱包ID，如企业用户钱包DID
    "created": str(int(time.time())),
    "nonce": "0", # your nonce for ed25519 signture
    "privateB64": "lgdYjMbh7BKCeGxmJrempaP+/cDGMy5StdjM4ZexB0/Ku8V1uI81OlhKdnsCJVqTrXe2vGWKtXR+ciuozCgqjQ==", # register wallet response private_key
    "payload": payload
 }

_, response = walletclient.issue_colored_token(header, payload, params)
print response