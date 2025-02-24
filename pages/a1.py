from flask import (
    Blueprint,
    request,
    render_template
)

bp = Blueprint(
    "a1", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A1")
def a1():
    name = request.args.get("name", "")
    return render_template("a1.html", name=name)