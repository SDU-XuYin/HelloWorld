import json
import time

def issue_tokens():
    payload = {
         "issuer": pub_wallet_id, # 数字凭证的发行方钱包DID
         "owner": wallet_id, # 数字资产的持有人钱包ID，如企业用户钱包DID(did:axn:***2fc68-f51e-4aff-b6e4-427cce3ed1af)
         "asset_id": poe_id, # 创建数字资产存证接口返回的poe_id,如：did:axn:***a94a9-eff4-4f15-88bf-f2054701e87c
         "amount": issue_amount, # 发行金额
         "fee": {
             "amount": 10
         } # 发行手续费、可不填
     }

     params = {
         "creator": wallet_id, # 数字资产的持有人钱包ID，如企业用户钱包DID
         "created": str(int(time.time())),
         "nonce": nonce, # your nonce for ed25519 signture
         "privateB64": private_key_base64, # register wallet response private_key
         "payload": payload
     }

     _, response = walletclient.issue_colored_token(header, payload, params)


def upload_poe():

    filename = "file path"
    poeid = "poeid" # 创建数字资产存证时返回的资产存证id

    _, resp = walletclient.upload_poe({}, filename, poeid)