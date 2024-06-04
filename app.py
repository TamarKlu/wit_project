import flask
from flask import  Flask, render_template, redirect
import wit_project.add
import wit_project.branch
import wit_project.checkout
import wit_project.status
import wit_project.commit



create_app = Flask(__name__)


@create_app.route('/', methods=['GET', 'POST'])
def index():
    files = wit_project.status.status()
    Changes_not_staged_for_commit = files[1]
    len_Changes_not_staged_for_commit = len( Changes_not_staged_for_commit)
    Untracked_files = files[2]
    len_Untracked_files = len(Untracked_files)
    return render_template(
        'index.html',
        Changes_not_staged_for_commit=Changes_not_staged_for_commit, 
        Untracked_files=Untracked_files,
         len_Changes_not_staged_for_commit = len_Changes_not_staged_for_commit,
         len_Untracked_files = len_Untracked_files
    )


@create_app.route('/add', methods=['GET', 'POST'])
def add():
    file_to_add = flask.request.form.get('file_to_add')
    try:
        wit_project.add.add(file_to_add)
        return "success",200
    except OSError as error:
        return str(error), 400


@create_app.route('/commit', methods=['GET', 'POST'])
def commit():
    massage = flask.request.form.get('massage')
    try:
        wit_project.commit.Commit(massage).commit()
        return "commited succesfully"
    except OSError as error:
        return str(error)

@create_app.route('/branches', methods=['GET', 'POST'])    
def branches():
    return render_template(
        'branch.html',
        branches = wit_project.branch.get_branches(),
        activted = wit_project.branch.get_activted_branch()
    )

@create_app.route('/checkout/<string:specific_branch>', methods=['GET', 'POST'])
def checkout(specific_branch):
    try:
        wit_project.checkout.Cheackout(specific_branch).checkout()
        return redirect("/")

    except OSError as error:
        return str(error)


if __name__ == '__main__':
    create_app.run(host='localhost', port=5000, debug=True)