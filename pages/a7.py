from flask import (
    Blueprint,
    request,
    render_template
)

bp = Blueprint(
    "a7", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A7")
def a7():
    name = request.args.get("name", "")
    return render_template("a7.html", name=name)