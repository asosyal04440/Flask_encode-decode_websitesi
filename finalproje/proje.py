'''
#Bu projede base64 tip kodlamalar için base64,URL encoding/decoding tip kodlamalar için urllib ,ROT13 için de codecs kütüphanesi kullandım
'''

from flask import Flask, render_template, request
import base64 
import urllib.parse
import codecs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  
def index():
    '''
    GET ve POST isteklerini kabul eden bir anasayfa tanımladım
    Eğer istek POST ise formdan gelen metni ve metodu almasını istedim
    Kullanıcı encode yapmak isterse kodlama tipini kontrol etmesini ve ona göre eylemler yapmasını istedim
    Kullanıcı decode yapmak isterse kodlama tipini kontrol etmesini ve ona göre eylemler yapmasını istedim
    '''
    result = None
    originaltext = None
    action = None
    method = None

    if request.method == 'POST':
        '''
        Eğer istek POST ise formdan gelen metni ve metodu almasını istedim
        '''
        originaltext = request.form['text']
        method = request.form['method']

        if 'encode' in request.form:
            '''
            Kullanıcı encode yapmak isterse kodlama tipini kontrol etmesini ve ona göre eylemler yapmasını istedim
            '''
            if method == 'base64':
                result = base64.b64encode(originaltext.encode()).decode()
            elif method == 'url':
                result = urllib.parse.quote(originaltext)
            elif method == 'rot13':
                result = codecs.encode(originaltext, 'rot_13')
            action = 'encode'
        elif 'decode' in request.form:
            '''
            Kullanıcı decode yapmak isterse kodlama tipini kontrol etmesini ve ona göre eylemler yapmasını istedim
            '''
            if method == 'base64':
                result = base64.b64decode(originaltext.encode()).decode()
            elif method == 'url':
                result = urllib.parse.unquote(originaltext)
            elif method == 'rot13':
                result = codecs.encode(originaltext, 'rot_13')
            action = 'decode'

    return render_template('index.html', originaltext=originaltext, result=result, action=action, method=method)

if __name__ == '__main__':
    app.run(debug=True)
