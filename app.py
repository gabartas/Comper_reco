from recommandations import create_app


# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app()


# Main will call only is 'python app.py' command is used
if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"])
