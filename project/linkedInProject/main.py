from Graph import Graph
from MyEdge import EdgeClass
from MyUser import UserClass

user = UserClass()
def showMenu():
    print('1.LogIn\n2.SignUp\n3.Show All users\n4.Search')
    inp = input('>> ')
    return inp
def login(username , password):
    try:
        if UserClass.findInFile(username , password , UserClass._local_users_file_path) != None:
            #go to login
            print()
        else:
            print('User not found!')
    except Exception:
        print("Something went wrong!")
def signup(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties):
    u = UserClass()
    u.setData1(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties , [])
    u.saveFile(UserClass._local_users_file_path)

print('Welcome to Unlinked Out')
inp = showMenu()

while True:
    if inp == '1':
        username = input('Enter Username >> ')
        password = input('Enter Password >> ')
        login(username , password)
    elif inp == '2':
        name = input('Name >> ')
        email = input('email >> ')
        dateOfBirth = input('Date of birth >> ')
        universityLocation = input('University location >> ')
        field = input('Field >> ')
        workplace = input('Work place >> ')
        specialties = list(input('Specialties >> ').split())
        username = input('username >> ')
        password = input('password >> ')
        signup(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties)
    elif inp == '3':
        users = UserClass.getUsers(UserClass._main_users_file_path)
        i = int(1)
        for user in users:
            print(str(i) + '.' + user.name)
            i += 1
    elif inp == '4':
        name = input('Enter the name >> ')
        user = UserClass.searchByName(name, UserClass._main_users_file_path)
        if user == None :
            print('The user ' + name + ' not found')
        else:
            user.toString()
    elif inp == '5':
        q = dict
        Graph.setGraph()
        G = Graph.getInstance()
        G.make_edges()
        tmp = Graph.BFS(G.vertices[0])
        for user in list(tmp.keys()) :
            print(user.name)
        for val in list(tmp.values()) :
            print(val)



    print('\n###############################################\n')

    inp = showMenu()