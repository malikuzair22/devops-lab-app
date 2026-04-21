from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Lab App Mid</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', sans-serif;
            overflow: hidden;
        }

        .container {
            text-align: center;
            padding: 60px 80px;
            background: rgba(255,255,255,0.05);
            border-radius: 24px;
            border: 1px solid rgba(255,255,255,0.15);
            backdrop-filter: blur(20px);
            box-shadow: 0 25px 60px rgba(0,0,0,0.5);
            animation: fadeIn 1s ease;
        }

        .emoji { font-size: 72px; margin-bottom: 20px; animation: bounce 2s infinite; }

        h1 {
            font-size: 52px;
            font-weight: 800;
            background: linear-gradient(90deg, #f093fb, #f5576c, #fda085, #f6d365);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }

        p.subtitle {
            color: rgba(255,255,255,0.6);
            font-size: 18px;
            margin-bottom: 40px;
            letter-spacing: 1px;
        }

        .badges {
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }

        .badge {
            padding: 8px 20px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 600;
            color: white;
            letter-spacing: 0.5px;
        }

        .badge.docker  { background: linear-gradient(135deg, #0db7ed, #086dd7); }
        .badge.aws     { background: linear-gradient(135deg, #ff9900, #e07000); }
        .badge.k8s     { background: linear-gradient(135deg, #326ce5, #1a4ab5); }
        .badge.jenkins { background: linear-gradient(135deg, #d33833, #a02020); }
        .badge.git     { background: linear-gradient(135deg, #f05032, #b83010); }
        .badge.flask   { background: linear-gradient(135deg, #38ef7d, #11998e); }

        .status {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(56, 239, 125, 0.15);
            border: 1px solid rgba(56, 239, 125, 0.4);
            color: #38ef7d;
            padding: 10px 24px;
            border-radius: 50px;
            font-size: 15px;
            font-weight: 600;
        }

        .dot {
            width: 10px; height: 10px;
            background: #38ef7d;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }

        .circles {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .circle {
            position: absolute;
            border-radius: 50%;
            opacity: 0.08;
            animation: float 8s infinite ease-in-out;
        }

        .circle:nth-child(1) { width:400px; height:400px; background:#f093fb; top:-100px; left:-100px; animation-delay:0s; }
        .circle:nth-child(2) { width:300px; height:300px; background:#4facfe; bottom:-80px; right:-80px; animation-delay:2s; }
        .circle:nth-child(3) { width:200px; height:200px; background:#fda085; top:50%; left:10%; animation-delay:4s; }

        @keyframes fadeIn  { from { opacity:0; transform:translateY(30px); } to { opacity:1; transform:translateY(0); } }
        @keyframes bounce  { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-12px); } }
        @keyframes pulse   { 0%,100% { opacity:1; } 50% { opacity:0.3; } }
        @keyframes float   { 0%,100% { transform:translateY(0) scale(1); } 50% { transform:translateY(-30px) scale(1.05); } }
    </style>
</head>
<body>
    <div class="circles">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
    </div>

    <div class="container">
        <div class="emoji">🚀</div>
        <h1>Hello DevOps World</h1>
        <p class="subtitle">Containerized · Deployed · Automated</p>

        <div class="badges">
            <span class="badge flask">🐍 Flask</span>
            <span class="badge docker">🐳 Docker</span>
            <span class="badge aws">☁️ AWS EC2</span>
            <span class="badge k8s">⚙️ Kubernetes</span>
            <span class="badge jenkins">🔧 Jenkins</span>
            <span class="badge git">🌿 GitHub</span>
        </div>

        <div class="status">
            <div class="dot"></div>
            App is Running Successfully
        </div>
    </div>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)