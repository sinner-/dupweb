#!bin/python
from subprocess import check_output
from subprocess import CalledProcessError
from os import environ
from re import split
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__, static_url_path="")

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/list', methods=['POST'])
def list_backups():

    tmp_env = environ.copy()
    tmp_env['PASSPHRASE'] = request.form['passphrase']
    entries = []
    for entry in check_output(
            ['/usr/bin/python2.7',
             '/usr/bin/duplicity',
             '-v0',
             'list-current-files',
             request.form['path']],
            env=tmp_env).split('\n'):
        split_entry = split(" ", entry, maxsplit=5)
        if len(split_entry) > 1:
            entries.append([" ".join(split_entry[:-1]), split_entry[-1]])

    return render_template('list.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
