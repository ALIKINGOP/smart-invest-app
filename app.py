from flask import Flask
app = Flask(_name_)

@app.route('/')
def home():
    return "مرحبًا بك في منصة استثمر بذكاء!"

if _name_ == '_main_':
    app.run()
