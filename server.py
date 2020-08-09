from flask import Flask, render_template, request, url_for
from PIL import Image 

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
        img = Image.open(file)
        img.save("static\converted_pdfs\converted.pdf")
        download = True

    return render_template('image.html', downloadable=download)




@app.route('/word', methods=['POST', 'GET'])
def word_to_pdf():
    return render_template('word.html')




@app.route('/ppt', methods=['POST', 'GET'])
def ppt_to_pdf():
    return render_template('ppt.html')



    

@app.route('/excel', methods=['POST', 'GET'])
def excel_to_pdf():
    return render_template('excel.html')

