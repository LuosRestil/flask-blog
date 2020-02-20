from flaskblog import create_app
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors

app = create_app()

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)

if __name__ == '__main__':
    app.run()
