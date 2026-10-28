from flask import Flask, render_template_string

app = Flask(__name__)

CHANNEL_LINK = "https://t.me/+sUuf3k54iTZmYTRk"

@app.route('/')
def index():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redirecting...</title>
        <script src="https://telegram.org/js/telegram-web-app.js"></script>
        <script>
            window.onload = function () {{
                if (window.Telegram && window.Telegram.WebApp) {{
                    window.Telegram.WebApp.ready();
                }}
                window.location.href = "{CHANNEL_LINK}";
            }};
        </script>
    </head>
    <body style="background-color: #111; color: #fff; font-family: sans-serif; text-align: center; padding-top: 50px;">
        <h3>Connecting to Channel...</h3>
        <p>If you are not redirected automatically, <a href="{CHANNEL_LINK}" style="color: #0088cc;">click here</a>.</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
