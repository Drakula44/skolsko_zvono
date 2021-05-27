from flask_script import Manager
from main import app
from flask_script import Command


class Hello(Command):

    def run(self):
        print("hello world")


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('hello', Hello())
    print("hello world")
    manager.run()


