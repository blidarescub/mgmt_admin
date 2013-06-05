import hashlib
import string
from flask import Flask, request, render_template, abort
import shlex, subprocess
import sys

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
        command = shlex.split('puppet agent --test')
        task = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        (stdout, stderr) = task.communicate()
        while True:
            out = task.stdout.read(1)
            if out == '' and process.poll() != None:
                break
            if out != '':
                sys.stdout.write(out)
                sys.stdout.flush()
        return stdout
    else:
        return "Incorrect or missing API key :("

#@app.errorhandler(404)
#def page_not_found(error):
#    abort(404)


app.run(host='0.0.0.0')
