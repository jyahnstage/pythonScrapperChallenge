from flask import Flask, render_template, request, redirect, send_file
from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file


app = Flask("JopScrapper")

db = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def result():
    term = request.args.get("term")
    if term == None:
        return redirect('/')
    if term in db:
        jobs = db[term]
    else:
        wwr = extract_wwr_jobs(term)
        ro = extract_remoteok_jobs(term)
        jobs = wwr + ro
        db[term] = jobs
    return render_template("result.html", term = term, jobs = jobs)

@app.route("/export")
def export():
    term = request.args.get("term")
    if term == None:
        return redirect("/")
    if term not in db:
        return redirect(f"/result?term={term}")
    save_to_file(term, db[term])
    return send_file(f"{term}.csv", as_attachment = True)

app.run("0.0.0.0", debug=True)
