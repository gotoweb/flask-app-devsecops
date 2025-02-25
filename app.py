import os
from flask import Flask

from pages import (
    index,
    about,
    a1,
    a2,
    a3,
    a5,
    a6,
    a7,
    a9
)

import models
from flask_wtf.csrf import CSRFProtect

### Initialize App
app = Flask(__name__)
app.url_map.strict_slashes = False

### Enable CSRF
app.config['SECRET_KEY'] = os.urandom(32)
csrf = CSRFProtect()
csrf.init_app(app)


### Register blueprints
app.register_blueprint(index.bp)
app.register_blueprint(about.bp, url_prefix="/about")
app.register_blueprint(a1.bp, url_prefix="/owasp")
app.register_blueprint(a2.bp, url_prefix="/owasp")
app.register_blueprint(a3.bp, url_prefix="/owasp")
app.register_blueprint(a5.bp, url_prefix="/owasp")
app.register_blueprint(a6.bp, url_prefix="/owasp")
app.register_blueprint(a7.bp, url_prefix="/owasp")
app.register_blueprint(a9.bp, url_prefix="/owasp")

### Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
models.db.init_app(app)
models.db.app = app
models.bootstrap(app)

### Add Security Headers
@app.after_request
def add_security_headers(r):
    r.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return r
