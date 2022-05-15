from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import runalldef as runalldef

app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def home():
    return render_template('homepage.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      fname = secure_filename(f.filename)
      f.save(secure_filename(f.filename))
      runalldef.runall(fname)
      return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=False)



