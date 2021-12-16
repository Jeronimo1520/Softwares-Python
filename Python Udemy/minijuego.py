print('''
                  ~.                       
            Ya...___|__..ab.     .   .  
             Y88b  \88b  \88b   (     )  
              Y88b  :88b  :88b   `.oo'   
              :888  |888  |888  ( (`-'   
     .---.    d88P  ;88P  ;88P   `.`.    
    / .-._)  d8P-"""|"""'-Y8P      `.`.  
   ( (`._) .-.  .-. |.-.  .-.  .-.   ) ) 
    \ `---( O )( O )( O )( O )( O )-' /  
     `.    `-'  `-'  `-'  `-'  `-'  .' CJ 
       `---------------------------'
''')
print("Welcome to The escape of the Viking ship.")
print("Your mission is to escape from the vikings.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction=input("Hurry, the vikings are going to cacth you, where do you wanna go? type left or rigth\n")
direction_lower=direction.lower()

if direction_lower == "rigth":
  print("Sadly, when your were running that direction, you fell into a trap. Game over.")
elif direction_lower == "left":
  swim_wait=input("You get to a port, what do your prefer? type swim or wait\n")
  swim_wait_lower=swim_wait.lower()

  if swim_wait_lower == "swim":
    print("While your were swimming, something catched you, it was the Kraken. Game over.")
  elif swim_wait_lower == "wait":
    doors=input("A magic portal appeared, you decide to go in. There are three doors: red, yellow, blue. Wich door?\n")
    doors_lower=doors.lower()

    if doors_lower=="blue":
      print("Oh no, this room is full of serpents. Game over.")
    elif doors_lower=="red":
      print("It can't be, the vikings were waiting for you there, bad luck. Game over")
    elif doors_lower=="yellow":
      
      print('''
        
                                ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.  
      ''')
      print("Congratulations, it was a door to your home, you escaped from the vikings. You win!")
    else:
      print("Game over")
  
  else:
    print("Game over")

else:
  print("Game over.")
