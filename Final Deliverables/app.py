from flask import Flask, render_template, request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf

app = Flask(__name__, template_folder="templates/templates")

model = load_model('models/mnistCNN.h5')
print("Loaded model from disk")

@app.route('/')
def upload_file():
    return render_template('Home.html')
@app.route('/Upload')  
def upload_file1():
    return render_template('Upload.html')
@app.route('/Draw')
def upload_file2():
    return render_template('Draw.html')
@app.route('/Guidelines')
def upload_file3():
    return render_template('Guidelines.html')

@app.route('/Predict',methods=['POST'])
def upload_image_file():
   if request.method=='POST':
     if request.files["file"]:
       img = Image.open(request.files['file'].stream).convert("L")
       img = img.resize((28,28))
       im2arr = np.array(img)
       im2arr = im2arr.reshape(1,28,28,1)
    
       y_pred = np.argmax(model.predict(im2arr))
    
       if(y_pred == 0):
        return render_template("Upload.html", showcase = str(y_pred))
        return '0'
       elif(y_pred == 1):
        return render_template("Upload.html", showcase = str(y_pred))
        return '1'
       elif(y_pred == 2):
        return render_template("Upload.html", showcase = str(y_pred))
        return '2'
       elif(y_pred == 3):
        return render_template("Upload.html", showcase = str(y_pred))
        return '3'
       elif(y_pred == 4):
        return render_template("Upload.html", showcase = str(y_pred))
        return '4'
       elif(y_pred == 5):
        return render_template("Upload.html", showcase = str(y_pred))
        return '5'
       elif(y_pred == 6):
        return render_template("Upload.html", showcase = str(y_pred))
        return '6'
       elif(y_pred == 7):
        return render_template("Upload.html", showcase = str(y_pred))
        return '7'
       elif(y_pred == 8):
        return render_template("Upload.html", showcase = str(y_pred))
        return '8'
       else:
        return render_template("Upload.html", showcase = str(y_pred))
        return '9'
     else :
        return render_template("Upload.html")
        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)
