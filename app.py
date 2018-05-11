from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import time

import numpy as np
import tensorflow as tf
import sys
import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


# @app.route("/generate")
# def generate():
#     return render_template("process.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))

    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
    print(destination)
        
    #os.system('python3 testbarchart1.py')
    from test1 import namee
    outp=namee(destination)
    print("Hey")

    from testpiechart1 import name1
    name1()
    print("PieChart")
    piechartshow = "piechart.png"
    
    from testbargraph import name2
    name2()
    print("BarGraph")
    bargraphshow = "groupedbargraph.png"
    
    return render_template("index.html", image_name=filename, image_path="/home/viggi/Documents/flaskfoo/static/"+filename, out1=outp, bgshw=bargraphshow, pcshw=piechartshow)


if __name__ == "__main__":
    app.run(debug=True)
