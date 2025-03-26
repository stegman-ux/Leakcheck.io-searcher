import colorama
from colorama import Fore
import fade
import requests
import clear
import os

def leakcheck():
    ascii_art = """   
             *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
            """
    os.system("title leakcheck.io-searcher by intrable")
    clear.clear()
    print(fade.greenblue(ascii_art))
    search = input(Fore.LIGHTBLUE_EX+"Your leakcheck.io search (Username,email) --> ")
    api = f"https://leakcheck.io/api/public?check={search}"
    res = requests.get(api)
    data = res.json()
    resultat = (f"Status  : {data['success']}")
    resultat2 = (f"fields  : {data['fields']}")
    resultat3 =(f"sources  : {data['sources']}")
    print(f"Status  : {data['success']}")
    print(f"fields  : {data['fields']}")
    print(f"sources  : {data['sources']}") # désolé je n'arrive pas a rendre un rendu plus joli pour le cmd sur les résultats si le résultat est gros ... 
    print()
    print()
    question = input(Fore.LIGHTBLUE_EX+"Do you want to save the results in a txt file ? Y/N : ") 
    if question == 'Y' or question == 'y':
      with open("result-leakcheck.io.txt", "w") as file:
         file.write(f"{resultat}")
         file.write("-------------------------------")
         file.write(f"{resultat2}")
         file.write("-------------------------------")
         file.write(f"{resultat3}")
         input(Fore.LIGHTWHITE_EX+f"The leakcheck results are enregisred in the file 'result-leakcheck.io'...")

        
    
leakcheck()