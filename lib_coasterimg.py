import random

def get():
    coasters = [

"""
  _                     .===.
 |H|        .--.      .:'   `:.
 |H|`.     /||||\     ||     ||
 |\\||:. .'||||||`.   `:.   .:'
 |:`:.--'||||||||||`--..`=:='...                                                      
""",

"""
 +   __    ___                    /XXXXX
 |  /XX\  /   \        __        /XXXXXX
 | /XXXX\(     )      /XX\      /xXXXXXX
 |/XXXXXX\\___/__    /XXXX\    /xXXXXXXX
 /XXXXXXXX\__/XXX\__/XXXXXX\__/xXXXXXXXX
 """,

 """
                                           __
                                       _  |  |
                   Yye                |_| |--|
                .---.  e           AA | | |  |
               /.--./\  e        A
              // || \/\  e      A
             //|/|| |\/\   aa a    |\o/ o/--
            ///|\|| | \/\ .       ~o \.'\.o'
           //|\|/|| | |\/\ .      /.` \o'
          //\|/|\|| | | \/\ ( (  . \o'
  __ __ _//|/|\|/|| | | |\/`--' '
 __/__/__//|\|/|\|| | | | `--'
 |\|/|\|/|\|/|\|/|| | | | |
 """,

    ]

<<<<<<< Updated upstream
    return coasters[1]
=======
    return coasters[2]
>>>>>>> Stashed changes

    #TODO: use random.choice instead
    #return random.choice(coaster)


def sad():
    return """
     .-\"\"\"\"\"\"-.
   .'          '.
  /   O      O   \\
 :                :
 |                |
 :    .------.    :
  \\  '        '  /
   '.          .'
     '-......-'
"""
