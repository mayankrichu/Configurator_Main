from __init__ import create_app

#importing app from __init__.py
#added one more comment111
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, debug=True)