from app.models import User,Pitch,Role,Comment
from flask_script import Manager,Server
from app import create_app,db
# from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
# Creating app instance
app = create_app('test')
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
   return dict(app = app,db = db,User = User, Pitch=Pitch,Comment=Comment,Role=Role)
if __name__ == '__main__':
   manager.run()