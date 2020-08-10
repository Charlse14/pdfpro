from flask import Flask, render_template, request, url_for, send_from_directory
from PIL import Image 
import os

app = Flask(__name__)

# it is a home page
@app.route('/home')
@app.route('/')
def hello_world():
    return render_template('index.html')





# it is rendering different page based on the click   

@app.route('/img', methods=['POST', 'GET'])

def image_to_pdf():

    download = False

    if request.method == 'POST':

        file = request.files['myfile']
        img = Image.open(file).convert('RGB')

        path = os.getcwd()
        path_list = ['static', 'client', 'pdfs']

        for i in path_list:
            path = os.path.join(path, i)

        if not os.path.exists(path):
            os.makedirs(path)

        joined_path = os.path.join(path, 'converted.pdf')
        a = img.save(joined_path)

        download = True

    return render_template('image.html', downloadable=download)


@app.route('/download')
def download_converted_pdf():

    path = os.getcwd()
    path_list = ['static', 'client', 'pdfs']

    print('hit path')

    for i in path_list:
        path = os.path.join(path, i)

    return send_from_directory(str(path), filename='converted.pdf', as_attachment=True)





@app.route('/word', methods=['POST', 'GET'])
def word_to_pdf():
    return render_template('word.html')




@app.route('/ppt', methods=['POST', 'GET'])
def ppt_to_pdf():
    return render_template('ppt.html')



    

@app.route('/excel', methods=['POST', 'GET'])
def excel_to_pdf():
    return render_template('excel.html')

