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
    "id": "", # 若传的数字存证id是空，则系统会自动生成
    "name": "POE_ID_01", # poe name
    "hash": "",
    "parent_id": "",
    "owner": "did:axn:17e8db57-a0fa-4028-b17f-802d01602194", # 企业用户钱包DID，如：did:axn:***2fc68-f51e-4aff-b6e4-427cce3ed1af
    "metadata": "GhaHjjdmN2VkNGU5M2NhMzk1MmM4NDgzZGNlN2Y4YTExZmRmOTEyNmU2ZTU2NWMzNzk3MTA1NjkzMWRiMjBkZjEy" # metadata的数据格式是byte数组，需要将json格式的数据进行处理, 如 [ord(x) for x in json.dumps(json格式的metadata数据)]
}

params = {
    "creator": "did:axn:17e8db57-a0fa-4028-b17f-802d01602194", # 企业用户钱包DID，如：did:axn:***2fc68-f51e-4aff-b6e4-427cce3ed1af
    "created": str(int(time.time())),
    "nonce": "0", # your nonce for ed25519 signture
    "privateB64": "lgdYjMbh7BKCeGxmJrempaP+/cDGMy5StdjM4ZexB0/Ku8V1uI81OlhKdnsCJVqTrXe2vGWKtXR+ciuozCgqjQ==", # 企业用户交易签名凭证，如：***+oEuaelf2aecUZvG7xrWr+p43ZfjGZYfDCXfQD+ku0xY5BXP8kIKhiqzKRvfyKBKM3y7V9O1bF7X3M9mxkQ==
    "payload": payload
}
_,response = walletclient.create_poe(header, payload, params)
print response
