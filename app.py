from flask import Flask
import subprocess
import datetime

app = Flask(__name__)

def get_git_commit_hash():
    """Get the short Git commit hash for the current repo."""
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8').strip()
        return commit_hash
    except Exception:
        return "unknown"

@app.route('/')
def home():
    # Current timestamp (UTC)
    deploy_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Get current commit hash
    commit = get_git_commit_hash()
    
    return f"""
    <h1>🚀 Flask App Deployed via CI/CD Pipeline</h1>
    <p><strong>Status:</strong> Live and running on EC2</p>
    <p><strong>Deployed at:</strong> {deploy_time}</p>
    <p><strong>Commit:</strong> {commit}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
