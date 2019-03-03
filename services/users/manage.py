import unittest
from flask_script import Manager
from project  import create_app,db
from project.api.models import User
import coverage


app = create_app()

manager = Manager(app)

@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def seed_db():
    db.session.add(User(username='to_yst',email='to_yst@163.com'))
    db.session.add(User(username='to_tsy',email='to_tsy@163.com'))
    db.session.commit()
    

@manager.command
def test():
    # 
    tests = unittest.TestLoader().discover('project/tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*'
    ]
)
COV.start()

@manager.command
def cov():
    # 
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0

    return 1

if __name__ =="__main__":
    manager.run()