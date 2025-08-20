from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_client_ip():
    # Try to respect proxies/load balancers (e.g., nginx) if they set X-Forwarded-For
    xff = request.headers.get("X-Forwarded-For", "")
    if xff:
        # X-Forwarded-For can be a list of IPs: client, proxy1, proxy2, ...
        return xff.split(",")[0].strip()
    return request.remote_addr or "Unknown"

@app.route("/")
def index():
    user_ip = get_client_ip()
    return render_template("index.html", ip=user_ip)

@app.route("/api/ip")
def api_ip():
    return jsonify({"ip": get_client_ip()})

if __name__ == "__main__":
    # Run on port 8000 as requested
    app.run(host="0.0.0.0", port=8000, debug=True)
