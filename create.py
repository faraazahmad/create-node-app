from subprocess import call

# get app name
def get_app_name():
    app_name = input("Enter app name: ")
    return app_name

# get preferred view engine
def get_view_engine():
    view_engine_list = [
        "dust",
        "ejs",
        "hbs",
        "hjs",
        "jade",
        "pug",
        "twig",
        "vash",
        "none"
    ]
    
    print("Available view engines: ")
    # show all available view engines
    i = 1
    for eng in view_engine_list:
        print("{}. {}    ".format(i, eng), end = '')
        i += 1
    
    # get choice number
    choice = None
    while True:
        choice = int(input("\nChoose view engine (1 - {}): ".format(view_engine_list.__len__())))
        if choice > 0 and choice < view_engine_list.__len__():
            break
        else:
            print("Invalid input.")
    
    # select engine string
    engine_string = None
    if choice is 8:
        engine_string = "--no-view"
    else:
        view_engine = view_engine_list[choice - 1]
        engine_string = "--view={}".format(view_engine)
    
    return engine_string


def get_stylesheet_engine():
    stylesheet_engine_list = [
        "sass",
        "less",
        "stylus",
        "compass",
        "none"
    ]

    print("Available stylesheet engines: ")
    # show all available stylesheet engines
    i = 1
    for eng in stylesheet_engine_list:
        print("{}. {}    ".format(i, eng), end = '')
        i += 1
    
    # get choice number
    choice = None
    stylesheet_string = None
    length = stylesheet_engine_list.__len__() - 1
    while True:
        choice = int(input("\nChoose stylesheet engine (1 - {}): ".format(length + 1))) - 1
        if choice >= 0 and choice < length:
            stylesheet_string = "--css={}".format(stylesheet_engine_list[choice - 1])
            break
        elif choice == length:
            stylesheet_string = "--css"
            break
        else:
            print("Invalid input.")

    return stylesheet_string

def run_command(command):
    try:
        call(command)
    except Exception as e:
        print(e)

# generate command with arguments for call() function
app_name = get_app_name()
view_engine = get_view_engine()
stylesheet_engine = get_stylesheet_engine()

# final command for generating node project
create_project = ["express", "--git", app_name, stylesheet_engine, view_engine]

# execute command to create project
run_command(create_project)

# Create directories for controllers
create_controller = ["mkdir", "-p", app_name, "controllers"]
run_command(create_controller)