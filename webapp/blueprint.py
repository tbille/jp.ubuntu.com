import flask


jp_website = flask.Blueprint(
    "jp_website",
    __name__,
    template_folder="/templates",
    static_folder="/static",
)


@jp_website.route("/")
def homepage():
    return flask.render_template("index.html")


@jp_website.route("/openstack")
def openstack():
    return flask.render_template("openstack.html")


@jp_website.route("/iot")
def iot():
    return flask.render_template("iot.html")


@jp_website.route("/ai-ml")
def ai_ml():
    return flask.render_template("ai-ml.html")


@jp_website.route("/kubernetes")
def k8s():
    return flask.render_template("kubernetes.html")


@jp_website.route("/enterprise-support")
def enterprise_support():
    return flask.render_template("enterprise-support/index.html")


@jp_website.route("/enterprise-support/plans-and-pricing")
def enterprise_support_plans():
    return flask.render_template("enterprise-support/plans-and-pricing.html")


@jp_website.route("/download")
def download():
    return flask.render_template("download.html")


@jp_website.route("/contact-us")
def contact_us():
    return flask.render_template("contact-us.html")


@jp_website.route("/thank-you")
def thank_you():
    return flask.render_template("thank-you.html")


@jp_website.route("/favicon.ico")
def favicon():
    return flask.redirect(
        "https://res.cloudinary.com/canonical/image/fetch/q_auto,f_auto/"
        "https://assets.ubuntu.com/v1/088fd1bf-favicon.ico"
    )


@jp_website.route("/robots.txt")
def robots():
    return flask.Response("", mimetype="text/plain")


@jp_website.route("/_status/check")
def check():
    return "OK"
