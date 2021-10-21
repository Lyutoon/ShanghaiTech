import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def collect_data(text, name, endtag):
    start_idx = text.find(f'name="{name}"')
    if name == 'pwdDefaultEncryptSalt':
        start_idx = text.find(f'id="{name}"')
    end_idx = text[start_idx:].find(endtag) + start_idx
    raw_data = text[start_idx:end_idx]
    res = raw_data[raw_data.find('value=')+7:-1]
    return res

def login(studentid, password):
    url = r"https://ids.shanghaitech.edu.cn/authserver/login?service="
    new_session = requests.session()
    new_session.cookies.clear()
    response = new_session.get(url)
    lt = collect_data(response.text, 'lt', r'/>')
    dllt = 'userNamePasswordLogin'
    execution = collect_data(response.text, 'execution', r'/>')
    _eventId = 'submit'
    rmShown = '1'
    key = collect_data(response.text, 'pwdDefaultEncryptSalt', r'/>')
    padded_password = b'Nu1L' * 16 + password.encode()
    pkcs7_padded_password = pad(padded_password, 16, 'pkcs7')
    iv = b'Nu1L' * 4
    aes = AES.new(key.encode(), AES.MODE_CBC, iv)
    password = base64.b64encode(aes.encrypt(pkcs7_padded_password))

    data = {
        'username':studentid,
        'password':password,
        'lt':lt,
        'dllt':dllt,
        'execution':execution,
        '_eventId':_eventId,
        'rmShown':rmShown
    }
    response = new_session.post(url, data=data)
    if "个人资料" in response.text:
        print('[+] Login successfully!')
        return new_session
    else:
        print('[+] Login failed...')