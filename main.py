from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def splash():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Loading...</title>
<style>
    body {
        margin: 0;
        padding: 0;
        background: black;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    img.splash-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        position: absolute;
        top: 0;
        left: 0;
        animation: fadeIn 1.5s ease-in-out;
        z-index: 0;
    }
    .loader {
        border: 6px solid rgba(255, 255, 255, 0.2);
        border-top: 6px solid #ff00ff;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1s linear infinite;
        z-index: 1;
        position: relative;
        margin-top: 20px;
    }
    .loading-text {
        margin-top: 15px;
        font-size: 22px;
        font-weight: bold;
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff;
        animation: blink 1.2s infinite alternate;
        z-index: 1;
        position: relative;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes blink {
        0% { opacity: 1; }
        100% { opacity: 0.4; }
    }
</style>
<script>
    setTimeout(() => {
        window.location.href = "https://minimum-merlina-henrykinghere-9e5f9eb1.koyeb.app/";  // Apna panel ka link yaha dalna
    }, 3000);  // 3 sec splash
</script>
</head>
<body>
    <img class="splash-image" src="https://i.imgur.com/B2iRAOX.jpeg" alt="Splash">
    <div class="loader"></div>
    <div class="loading-text">Please Wait...</div>
</body>
</html>
""")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
