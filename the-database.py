#ansi escape color for codes
BLUE = "\033[94m"
RESET = "\033[0m"

#prints cool text
print("""
██╗   ██╗██╗██████╗ ███████╗ ██████╗     ██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
██║   ██║██║██╔══██╗██╔════╝██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║   ██║██║██║  ██║█████╗  ██║   ██║    ██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  
╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║    ██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
 ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝    ██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
  ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
""")
#Variables
#list of playlist links
playlists = {"Amazing Websites and Stuff": "https://www.youtube.com/watch?v=ALUToU7PAn8&list=PLkmmMhZdHDilKIznvMa1y6GxuYDvKVY9a",
             "Google Workspace": "https://www.youtube.com/watch?v=ALUToU7PAn8&list=PLkmmMhZdHDikjLvLwxCjCFECCIipMYLp8",
             "Software Tutorials": "https://www.youtube.com/watch?v=ALUToU7PAn8&list=PLkmmMhZdHDinfEzM6nduAT6yw713K7T77",
             "Text Documents": "https://www.youtube.com/watch?v=ALUToU7PAn8&list=PLkmmMhZdHDinChuE9UqqpzMlBxUNM0RZn",
             "Windows 11": "https://www.youtube.com/watch?v=-EH9Lw1R-gM&list=PLkmmMhZdHDilvaOh_J_QkAatCzwOe5SFF",
             "Adobe Acrobat": "https://www.youtube.com/watch?v=voXhfOD4ztc&list=PLkmmMhZdHDilYPI-ndSh8_3tjpdEWmopZ",
             "OBS Studio": "https://www.youtube.com/watch?v=ghyXTqaaoUc&list=PLkmmMhZdHDikTJXnJm468412j8p51_Hgm",
             "PC Tips": "https://www.youtube.com/watch?v=-EH9Lw1R-gM&list=PLkmmMhZdHDilvaOh_J_QkAatCzwOe5SFF"
            }

#prints playlist options with color      
print("Please choose a playlist from the options below:")
for name, url in playlists.items():
    print(f"{name}: {BLUE}{url}{RESET}")
