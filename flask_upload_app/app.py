# app.py
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi', 'webm'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
            
        file = request.files['file']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f'Successfully uploaded {filename}')
            return redirect(url_for('index'))
        else:
            flash(f'File type not allowed. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}')
            return redirect(request.url)
            
    # GET request - display template with files
    files = []
    try:
        files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) 
                if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f)) and allowed_file(f)]
    except Exception as e:
        flash(f'Error reading files: {str(e)}')
    
    return render_template('index.html', files=files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Download route
@app.route('/download/<filename>')
def download_file(filename):
    # send file as attachment to prompt download
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    # Manual start: run with `python app.py`
    app.run(host='0.0.0.0', port=1212, debug=True, threaded=True)
