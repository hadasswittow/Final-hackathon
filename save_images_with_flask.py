
import datetime
import os
import base64
from flask import Flask, render_template,request
import model

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['MONGO_SETTINGS'] = {
    'db' : "testDB"
}

@app.route("/upload-image", methods=[ "POST"])
def upload_image():
    jsn = request.get_json()
    img = jsn['img']
    imgdata = base64.b64decode(img)
    filename = 'some_image.jpg'
    with open(f'images/{filename}', 'wb') as f:
        f.write(imgdata)
    return "got the image!"




if __name__ == "__main__":
   app.run(host='10.144.67.64')