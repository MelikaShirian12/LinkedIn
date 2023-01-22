from AI_settings import ClusteringMatrix
from Graph import Graph
from MyEdge import EdgeClass
from MyUser import UserClass

def showMenu():
    print('1.LogIn\n2.SignUp\n3.Show All users\n4.Search')
    inp = input('>> ')
    return inp
def login(username , password):
    try:
        user = UserClass.findInFile(username , password , UserClass._local_users_file_path)
        if user != None:
            #go to login
            return user
        else:
            return None
    except Exception:
        return None

def loginByEmail(email):
    try:
        user = UserClass.searchByEmail(email , '****' , UserClass._main_users_file_path)
        if user != None:
            #go to login
            return user
        else:
            return None
    except Exception:
        return None






def signup(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties):
    u = UserClass()
    u.setData1(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties , [])
    u.saveFile(UserClass._local_users_file_path)

def loginMenu(user = UserClass):

    print('Name : ' + user.name)
    print('specialties : ' , end='')
    for sp in user.specialties:
        print(sp , end=' ')
    print('Recommended users : ' , end= ' , ')
    # BFSTraverse = Graph.BFS(user)
    # matrix = ClusteringMatrix(len(tmp))
    # m.setScore(user, tmp)
    # print()










#################################
Graph.setGraph()
G = Graph.getInstance()
G.make_edges()



print('Welcome to Unlinked Out')
inp = showMenu()

while True:
    if inp == '1':
        username = input('Enter Username >> ')
        password = input('Enter Password >> ')
        user = login(username , password)
        user2 = loginByEmail(username)
        if user is not None:
            loginMenu(user)
        elif user2 is not None:
            loginMenu(user2)

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
        tmp = Graph.BFS(G.vertices[3])
        for user in list(tmp.keys()) :
            print(user.name)
        for val in list(tmp.values()) :
            print(val)
        print(len(tmp))
        m = ClusteringMatrix(len(tmp))
        x = m.setScore(G.vertices[3] , tmp)
        m.showPlt()
        print(m.matrix)


        print()



    print('\n###############################################\n')

    inp = showMenu()