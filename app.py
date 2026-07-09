import os

from flask import Flask, render_template

app = Flask(__name__)


@app.context_processor
def inject_site_settings():
    return {"ga_measurement_id": os.getenv("GA_MEASUREMENT_ID", "")}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")


@app.route("/medicare-basics")
def medicare_basics():
    return render_template("medicare_basics.html")


@app.route("/home-safety-checklist")
def home_safety_checklist():
    return render_template("home_safety_checklist.html")


@app.route("/caregiver-planning-guide")
def caregiver_planning_guide():
    return render_template("caregiver_planning_guide.html")

if __name__ == "__main__":
    app.run(debug=True)
