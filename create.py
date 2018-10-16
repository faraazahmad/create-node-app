# get app name
def get_app_name():
    app_name = input("Enter app name: ")

# get preferred view engine
def get_view_engine():
    view_engine_list = [
        "ejs",
        "hbs",
        "hjs",
        "jade",
        "pug",
        "twig",
        "vash",
        "none"
    ]
    
    # show all available view engines
    print("Available view engines: ")
    i = 1
    for eng in view_engine_list:
        print("{}. {}    ".format(i, eng), end = '')
        i += 1
    
    choice = int(input("\nChoose view engine (1 - 8): "))
    if choice < 1 and choice > 8:
        print("Enter a valid number")
        get_view_engine()
    
    engine_string = None

    if choice is 8:
        engine_string = "--no-view"
    else:
        view_engine = view_engine_list[choice - 1]
        engine_string = "--view={}".format(view_engine)
    
    return engine_string

# generate `express ..` arguments

# run `express ..` with arguments
get_view_engine()