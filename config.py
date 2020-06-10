import os

basedir = os.path.abspath(os.path.dirname(__file__))
basedir_option_check = 'sqlite:///' + os.path.join(basedir, 'app.db')

class Config():
    """
    Setting all configuration variable as the class attributes instead of doing as below:
        app.config['SECRET_KEY'] = 'you-will-never-guess'
    """
    SECRET_KEY= "you-will-never-guess" or os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') or os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

if __name__ == '__main__':
    print(f'{basedir_option_check}')