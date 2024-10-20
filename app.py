import inspect
import io
import os
import subprocess

from PIL import ImageFont
from PIL.Image import Image
from PIL.ImageDraw import ImageDraw
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

MAX_FILE_SIZE = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static\\upload'
PROCESSED_FOLDER = 'static\\processed'
work_path=os.path.abspath(__file__)
work_path=os.path.dirname(work_path)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(PROCESSED_FOLDER):
    os.makedirs(PROCESSED_FOLDER)

def save_processed_image(image_content, path):
    with open(path, 'wb') as f:
        f.write(image_content)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main_page.html')
    elif request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        if file:
            image_path=os.path.join(work_path,UPLOAD_FOLDER,file.filename)
            file.save(image_path)
            print(image_path)
            detection_result = call_yolov5_detect(image_path)
            print(detection_result)
            processed_image_path = work_path+os.path.join('\static\processed', file.filename)
            print(processed_image_path)
            if os.path.exists(processed_image_path):
                return render_template('preview_page.html', filename=file.filename, file_url=os.path.join('\static\processed', file.filename))
            else:
                return render_template('error.html')



def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def call_yolov5_detect(image_path, conf_thres=0.25, iou_thres=0.45):
    cmd = [
        'python', work_path + '/static/detect/yolov5-7.0/detect.py',
        '--source', image_path,
        '--conf-thres', str(conf_thres),
        '--iou-thres', str(iou_thres),
        '--exist-ok',
        '--project', work_path + '/static/processed',
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("An error occurred while running YOLOv5 detection:", e)
        return e.stderr


if __name__ == '__main__':
    app.run(debug=True)