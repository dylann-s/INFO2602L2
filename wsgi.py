#Creating an Object, import Todo for Task 8.3
import click, sys
from models import db, User, Todo
from app import app
#from sqlalchemy.exc import IntegrityError


@app.cli.command("init", help="Creates and initializes the database")
def initialize():
  db.drop_all()
  db.init_app(app)
  db.create_all()
  bob = User('bob', 'bob@mail.com', 'bobpass')
  #bob.todos.append(Todo('wash car'))
  db.session.add(bob)
  db.session.commit()
  print(bob)
  print('database intialized')

'''
#Task 8.3
@app.cli.command("init", helps = "Create and initailizes the database")
def initialize():
  db.drop_all()
  db.init_app(app)
  db.create_all()
  bob = User('bob', 'bob@mail.com', 'bobpass')
  bob.todos.append(Todo('wash car'))
  db.session.add(bob)
  db.session.commit()
  print(bob)
  print('database intialized')
'''
  #Task 3: in "shell" flask init

#Task 4.1
@app.cli.command("get-user", help = "Retrieves a User")
@click.argument('username', default='bob')
def get_user(username):
  bob = User.query.filter_by(username=username).first()
  if not bob:
    print (f'{username} not found')
    return
  print(bob)

#flask get-user
#flask get-user bob

#task 4.2

@app.cli.command('get-users')
def get_users():
  #gets all objects within a model
  users = User.query.all()
  print (users)

#flask get-users

#Task 5
@app.cli.command("change-email")
@click.argument('username', default='bob')
@click.argument('email',default='bob@mail.com')

def change_email(username,email):
  bob = User.query.filter_by(username=username).first()
  if not bob:
    print (f'{username} not found')
    return
  bob.email = email
  db.session.add(bob)
  db.session.commit()
  print(bob)

  #flask change-email bob bobby@mail.com

#Task 6 
@app.cli.command('create-user')
@click.argument('username', default = 'rick')
@click.argument('email', default = 'rick@mail.com')
@click.argument('password', default = 'rickpass')

def create_user(username, email, password):
  newuser = User(username, email,password)
  try:
    db.session.add(newuser)
    db.session.commit()
  except IntegrityError as e:    #lets the bd undo any previous steps of a transaction 
    db.session.rollback()        #print(e.orig) #optionally print the error raised by the database
    print("Username or Email already taken")  # give user a useful message
  else:
    print (newuser)

'''
flask get-users
flast create-user
flask get-users
flask create- user
'''

#Task 7 
@app.cli.command('delete-user')
@click.argument('username', default = 'bob')

def delete_user(username):
  bob = User.query.filter_by(username=username).first()
  if not bob:
    print(f'{username} not found')
    return
  db.session.delete(bob)
  db.session.commit()
  print(f'{username} deleted')

'''
flask delete-user bob
flask get-users
'''


@app.cli.command('get-todos')
@click.argument('username', default = 'bob')
def get_user_todos(username):
  bob = User.query.filter_by(username=username).first()
  if not bob:
    print(f'{username} not found')
    return
  print (bob.todos)
