import hashlib
import string
from flask import Flask, request, render_template, abort
import shlex, subprocess

app = Flask(__name__)
app.debug = True

hash = hashlib.md5().hexdigest()
print "Current hash : " + hash



@app.route('/')
def hello():
    return "Hello World!"

@app.route('/puppet_kick/',methods=['POST', 'GET'])
def puppet_kick():
    searchword = request.args.get('key')
    
    if searchword == hash:
        execute = subprocess.Popen(shlex.split('puppet agent --test'),shell=True,stdout=subprocess.STDOUT)
        execute.communicate()
        
        return "Puppet kick!!!"
    else:
        return "Incorrect or missing API key :("

#@app.errorhandler(404)
#def page_not_found(error):
#    abort(404)


app.run(host='0.0.0.0')
