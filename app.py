import os
from flask import Flask, render_template, request, send_file, flash, redirect
from werkzeug.utils import secure_filename

from utils.ocr_engine import run_ocr
from utils.image_processing import preprocess_image
from utils.form_extractor import extract_form_fields
from utils.doc_generator import create_doc_from_fields

ALLOWED_EXT = {'png','jpg','jpeg','pdf'}

app = Flask(__name__)
app.secret_key = 'secret123'

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('File tidak ditemukan')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('File kosong')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            img_path = preprocess_image(filepath)
            ocr_text = run_ocr(img_path)
            fields = extract_form_fields(ocr_text)

            doc_path = create_doc_from_fields(fields)

            return send_file(doc_path, as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, render_template, request, send_file, flash, redirect
from werkzeug.utils import secure_filename

from utils.ocr_engine import run_ocr
from utils.image_processing import preprocess_image
from utils.form_extractor import extract_form_fields
from utils.doc_generator import create_doc_from_fields

ALLOWED_EXT = {'png','jpg','jpeg','pdf'}

app = Flask(__name__)
app.secret_key = 'secret123'

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('File tidak ditemukan')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('File kosong')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            img_path = preprocess_image(filepath)
            ocr_text = run_ocr(img_path)
            fields = extract_form_fields(ocr_text)

            doc_path = create_doc_from_fields(fields)

            return send_file(doc_path, as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
