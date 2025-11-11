import ast, base64, runpy
from Crypto.Cipher import AES

with open("fgngdutusrttddyjtndhttffjgdffjgdjggjfchggxjnhxgxjxjgjgcxjgrsutddjtxjcgckykdsyjsjyicyicyjvmmcggjssdafjckyfkydykffhkckkhcfykgfgcj", "rb") as f:
    key = f.read()

with open("jawllwsmdbdgegwiowlskdndneguwiqkwkrbrbdbdhsuekjebrbrhdisowlkwnebrhduwkkwkenrbfhf", "r") as f:
    data = ast.literal_eval(f.read())

nonce = base64.b64decode(data["nonce"])
ciphertext = base64.b64decode(data["cipher"])
tag = base64.b64decode(data["tag"])

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

exec(plaintext)
