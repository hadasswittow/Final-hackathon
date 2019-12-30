
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
    cropped = jsn['cropped']
    img_name = jsn['img_name']
    img_name += '.jpg'
    imgdata = base64.b64decode(img)
    crpdata =  base64.b64decode(cropped)
    with open(f'images/{img_name}', 'wb') as f,open(f'cropped/{img_name}', 'wb') as c:
        f.write(imgdata)
        c.write(crpdata)
    return "got the image!"




if __name__ == "__main__":
   app.run(host='10.144.68.64')
