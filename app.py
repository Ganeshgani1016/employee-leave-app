from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CORO PORTAL</h1>
    <h3>Employee Attendance Dashboard</h3>
    <p>Total Employees: 500</p>
    <p>Present: 450</p>
    <p>Absent: 50</p>
    <p>Attendance %: 90%</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
