from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Vercel-specific: Make sure Flask can run as a serverless function
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)
