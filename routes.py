# routes.py

from functools import wraps
from flask import (
    session,
    redirect,
    url_for,
    render_template,
    request,
    flash,
)
from app import app, db
from models import User, Patient

# -----------------------------------------------------------------------------
# Authentication decorator
# -----------------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated(*args, **kw):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kw)
    return decorated

# -----------------------------------------------------------------------------
# Login / Logout
# -----------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('patient_list'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# -----------------------------------------------------------------------------
# Patient List (Read)
# -----------------------------------------------------------------------------
@app.route('/patients')
@login_required
def patient_list():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

# -----------------------------------------------------------------------------
# Create Patient
# -----------------------------------------------------------------------------
@app.route('/patients/new', methods=['GET', 'POST'])
@login_required
def create_patient():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', type=int)
        diagnosis = request.form.get('diagnosis', '').strip()

        if not name:
            flash('Name is required.', 'warning')
        else:
            p = Patient(name=name, age=age, diagnosis=diagnosis)
            db.session.add(p)
            db.session.commit()
            flash(f'Patient "{name}" created.', 'success')
            return redirect(url_for('patient_list'))

    return render_template('patient_form.html', action='Create')

# -----------------------------------------------------------------------------
# View & Update Patient
# -----------------------------------------------------------------------------
@app.route('/patients/<int:patient_id>', methods=['GET', 'POST'])
@login_required
def patient_detail(patient_id):
    p = Patient.query.get_or_404(patient_id)

    if request.method == 'POST':
        p.name = request.form.get('name', p.name).strip()
        p.age = request.form.get('age', type=int, default=p.age)
        p.diagnosis = request.form.get('diagnosis', p.diagnosis).strip()
        db.session.commit()
        flash(f'Patient "{p.name}" updated.', 'success')
        return redirect(url_for('patient_list'))

    return render_template('patient_detail.html', patient=p)

# -----------------------------------------------------------------------------
# Delete Patient
# -----------------------------------------------------------------------------
@app.route('/patients/<int:patient_id>/delete', methods=['POST'])
@login_required
def delete_patient(patient_id):
    p = Patient.query.get_or_404(patient_id)
    db.session.delete(p)
    db.session.commit()
    flash(f'Patient "{p.name}" deleted.', 'info')
    return redirect(url_for('patient_list'))
