from flask import Flask, request, jsonify, send_from_directory
import os, json, shutil, subprocess
from datetime import datetime

app = Flask(__name__, static_folder='.')

REPO_DIR     = os.path.expanduser("~/Documents/ClaudeProjects/PatientEngageWebsite")
VERSIONS_DIR = os.path.join(REPO_DIR, ".versions")
LOG_FILE     = os.path.join(VERSIONS_DIR, "changelog.json")
PORT         = 8081

def ensure_dirs():
    os.makedirs(VERSIONS_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

def load_log():
    ensure_dirs()
    with open(LOG_FILE) as f:
        return json.load(f)

def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

def next_version(log):
    if not log:
        return "1.0"
    last = log[0].get("version", "1.0")
    parts = last.split(".")
    return f"{parts[0]}.{int(parts[1]) + 1}"

def run_git(commands, cwd):
    results = []
    for cmd in commands:
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=True)
        results.append({
            "cmd": cmd,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "ok": result.returncode == 0
        })
    return results

@app.route("/")
def index():
    return send_from_directory(".", "deploy_dashboard.html")

@app.route("/api/log")
def get_log():
    return jsonify(load_log())

@app.route("/api/deploy", methods=["POST"])
def deploy():
    ensure_dirs()
    if "file" not in request.files:
        return jsonify({"ok": False, "error": "No file provided"}), 400

    file    = request.files["file"]
    message = request.form.get("message", "Update page").strip()
    html    = file.read().decode("utf-8")
    log     = load_log()
    version = next_version(log)
    ts      = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ts_file = datetime.now().strftime("%Y%m%d_%H%M%S")

    current_path = os.path.join(REPO_DIR, "index.html")

    # Snapshot current version before overwriting
    if os.path.exists(current_path) and log:
        prev_snap = f"v{log[0]['version']}_{ts_file}_before.html"
        shutil.copy(current_path, os.path.join(VERSIONS_DIR, prev_snap))

    # Save new version snapshot
    new_snapshot = f"v{version}_{ts_file}.html"
    with open(os.path.join(VERSIONS_DIR, new_snapshot), "w", encoding="utf-8") as f:
        f.write(html)

    # Write to repo
    with open(current_path, "w", encoding="utf-8") as f:
        f.write(html)

    # Git commit and push
    git_results = run_git([
        "git add index.html",
        f'git commit -m "v{version} — {message}"',
        "git push"
    ], cwd=REPO_DIR)

    git_ok = all(r["ok"] for r in git_results)

    entry = {
        "version":   version,
        "timestamp": ts,
        "message":   message,
        "snapshot":  new_snapshot,
        "git_ok":    git_ok,
        "live_url":  "https://lennyeyecarepro.github.io/patientengage-scheduler"
    }
    log.insert(0, entry)
    save_log(log)

    return jsonify({"ok": True, "version": version, "git_ok": git_ok, "git": git_results})

@app.route("/api/restore/<version_id>", methods=["POST"])
def restore(version_id):
    ensure_dirs()
    log   = load_log()
    entry = next((e for e in log if e["version"] == version_id), None)
    if not entry:
        return jsonify({"ok": False, "error": "Version not found"}), 404

    snap_path = os.path.join(VERSIONS_DIR, entry["snapshot"])
    if not os.path.exists(snap_path):
        return jsonify({"ok": False, "error": "Snapshot file missing"}), 404

    shutil.copy(snap_path, os.path.join(REPO_DIR, "index.html"))

    ts      = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_ver = next_version(log)
    message = f"Restored to v{version_id}"

    git_results = run_git([
        "git add index.html",
        f'git commit -m "v{new_ver} — {message}"',
        "git push"
    ], cwd=REPO_DIR)

    new_entry = {
        "version":        new_ver,
        "timestamp":      ts,
        "message":        message,
        "snapshot":       entry["snapshot"],
        "git_ok":         all(r["ok"] for r in git_results),
        "live_url":       "https://lennyeyecarepro.github.io/patientengage-scheduler",
        "restored_from":  version_id
    }
    log.insert(0, new_entry)
    save_log(log)

    return jsonify({"ok": True, "version": new_ver})

if __name__ == "__main__":
    ensure_dirs()
    print(f"\n  Deploy dashboard → http://127.0.0.1:{PORT}\n")
    app.run(port=PORT, debug=False)
