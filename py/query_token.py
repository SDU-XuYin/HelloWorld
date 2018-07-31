# coding=utf-8
import time
from api.wallet import WalletClient
import json
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
_, resp = walletclient.query_wallet_balance({"Bc-Invoke-Mode":"sync"}, "did:axn:17e8db57-a0fa-4028-b17f-802d01602194")
print resp