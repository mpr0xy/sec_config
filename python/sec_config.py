from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import hashlib
import json
import sys


def generate_sec_config():
  
  # Need to modify for your own configuration file
  config = {
    'APIKEY': '25468665654',
    'PKEY': 'ijdijfuadfjiajdiuweuhuaidf'
  }
  # Once you generate the sec_config, please delete the original too config  


  key = raw_input("(Remember it)plase input:")
  key = key + 'helloworld_python_live'
  key = hashlib.new("md5", key).hexdigest()

  IV_seed = 'Not war, to have sex'
  IV = SHA256.new()
  IV.update(IV_seed)
  IV = str(IV.digest())[0:16]

  obj = AES.new(key, AES.MODE_CFB, IV)
  msg = obj.encrypt(json.dumps(config))
  print 'sec_config = "' + msg.encode('hex') + '"'


def start_sec_config():

  # Need to modify for your own sec_config, it generate by generate_sec_config()
  sec_config = "91169d484d86feb15e940b761d89544a7684250b5e55f25d77bc8e69bce5035322f692e0515f0c5b9288d1ca1ddeef8f37129daefe094594c6563e2c1aaac2"
  
  key = raw_input("plase input key:")
  key = key + 'helloworld_python_live'
  key = hashlib.new("md5", key).hexdigest()

  IV_seed = 'Not war, to have sex'
  IV = SHA256.new()
  IV.update(IV_seed)
  IV = str(IV.digest())[0:16]

  obj = AES.new(key, AES.MODE_CFB, IV)
  config = obj.decrypt(sec_config.decode('hex'))
  try:
    config = json.loads(config)
  except:
    print 'key error!'
    exit()
  return config


if __name__ == '__main__':
  if len(sys.argv) == 2 and sys.argv[1] == 'generate_sec_config':
    generate_sec_config()
    exit()
  else:
    config = start_sec_config()
    # start your code here use '_config_'
    print config 


'''
ref:
http://stackoverflow.com/questions/11384658/encryption-of-a-jpg-file-using-pycrypros-aes-failing
'''