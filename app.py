import os

from flask import Flask, Response, render_template, request

app = Flask(__name__)


@app.context_processor
def inject_site_settings():
    return {
        "ga_measurement_id": os.getenv("GA_MEASUREMENT_ID", "G-V33RXLE4PV"),
        "adsense_client": os.getenv("ADSENSE_CLIENT", "ca-pub-4708215788911775"),
    }

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


@app.route("/about")
def about():
    return render_template("about.html")


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


@app.route("/senior-benefits-checklist")
def senior_benefits_checklist():
    return render_template("senior_benefits_checklist.html")


@app.route("/questions-before-hiring-caregiver")
def questions_before_hiring_caregiver():
    return render_template("questions_before_hiring_caregiver.html")


@app.route("/assisted-living-comparison")
def assisted_living_comparison():
    return render_template("assisted_living_comparison.html")


@app.route("/medication-management-tips")
def medication_management_tips():
    return render_template("medication_management_tips.html")


@app.route("/dementia-early-signs-guide")
def dementia_early_signs_guide():
    return render_template("dementia_early_signs_guide.html")


@app.route("/senior-transportation-options")
def senior_transportation_options():
    return render_template("senior_transportation_options.html")


@app.route("/complete-senior-care-planning-guide")
def complete_senior_care_planning_guide():
    return render_template("complete_senior_care_planning_guide.html")


@app.route("/sitemap.xml")
def sitemap_xml():
    base_url = request.url_root.rstrip("/")
    pages = [
        "/",
        "/about",
        "/projects",
        "/skills",
        "/contact",
        "/privacy-policy",
        "/terms",
        "/disclaimer",
        "/medicare-basics",
        "/home-safety-checklist",
        "/caregiver-planning-guide",
        "/senior-benefits-checklist",
        "/questions-before-hiring-caregiver",
        "/assisted-living-comparison",
        "/medication-management-tips",
        "/dementia-early-signs-guide",
        "/senior-transportation-options",
        "/complete-senior-care-planning-guide",
    ]

    urls = "\n".join(
        f"  <url><loc>{base_url}{path}</loc></url>" for path in pages
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "</urlset>"
    )
    return Response(sitemap, mimetype="application/xml")


@app.route("/robots.txt")
def robots_txt():
    base_url = request.url_root.rstrip("/")
    robots = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {base_url}/sitemap.xml\n"
    )
    return Response(robots, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
