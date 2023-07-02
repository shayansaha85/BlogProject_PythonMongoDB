from flask import *
import json
import insertJSON

app = Flask(__name__)

@app.route('/createBlog', methods = ['POST'])
def createBlog():
    apiOutput = {}
    input_json = request.get_json(force=True)
    data = input_json
    insertJSON.insertBlog(data)
    return { "message" : "BLOG CREATED" }

@app.route('/retrieveBlog', methods = ['GET'])
def retrieveBlog():
    id = request.args.get('id')
    return { "id" : id, "message" : "BLOG BODY" }

@app.route("/updateBlog", methods = ["POST"])
def updateBlog():
    input_json = request.get_json(force=True)
    id = input_json['id']
    heading = input_json['heading']
    blog = input_json['blog']

    return { "message" : "BLOG_UPDATED", "info" :  [ { "id" : id, "heading" : heading, "blog" : blog } ]}

@app.route("/deleteBlog", methods = ['GET'])
def deleteBlog():
    id = request.args.get('id')
    return { "message" : str(id) + " BLOG DELETED" }

@app.route("/listBlogs", methods = ['GET'])
def listBlogs():
    return { "BLOGS" : [ {"id" : "TID1", "heading" : "THEADING1", "blog" : "TBLOG1"}, {"id" : "TID2", "heading" : "THEADING2", "blog" : "TBLOG2"}, {"id" : "TID3", "heading" : "THEADING3", "blog" : "TBLOG3"}  ] }

@app.route("/addComment", methods = ['POST'])
def addComment():
    input_json = request.get_json(force=True)
    id = input_json['id']
    comment = input_json['comment']

    return { 'message' : "COMMENT ADDED" }

@app.route("/listComments", methods = ['GET'])
def listComments():
    id = request.args.get('id')

    return {"COMMENTS" : ["comment1","comment2","comment3","comment4"]}

app.run()