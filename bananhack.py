import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

keyboard = Controller()

# Driver pour le navigateur
print('Driver loading ...')
service = Service(executable_path="Driver/geckodriver.exe")
driver = webdriver.Firefox(service=service)
print('Driver loaded')

def open_website():
    """
    ouverture de la page login de bananobet
    """
    # Ouverture du site
    print('Connexion to website ...')
    driver.get("https://www.bananobet.com")

    # Acces à la page login
    print('Connexion to login page ...')
    login = driver.find_element(By.LINK_TEXT, 'Login To Play')
    login.click()
    print('Connected')

def get_sold():
    """
    récupère et retourne la valeur du solde totale du joueur
    """
    sold = driver.find_element(By.ID, 'userBalance')
    return sold.text

def alttab():
    """
    definie la fonction appuie sur ALT + TAB
    """
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    time.sleep(1)

def tab():
    """
    definie la fonction appuie sur TAB
    """
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

def untab():
    """
    definie la fonction appuie sur SHIFT + TAB
    """
    keyboard.press(Key.shift)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.shift)

def reset():
    """
    definie la fonction reset de la mise
    """
    untab()
    keyboard.type("0.01")
    tab()

def martinguale():
    """
    definie la fonction du calcule de la martinguale qui va te rendre riche baby !
    """
    # X2
    tab()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    untab()
    time.sleep(0.3)

    # +1
    untab()
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    tab()
    time.sleep(0.3)

def roll():
    """
    definie la fonction de lancer des dés
    """
    a = 0
    
    while a < 8 :
        tab()
        a = a + 1
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    while a > 0 :
        untab()
        a = a - 1
    time.sleep(2)

def get_result(sold):
    """
    determine si c'est une victoire ou un défaite
    """
    
    newsold = get_sold()

    # si c'est une victoire
    if newsold > sold :
        return  0
    
    # si c'est une défaite
    elif newsold < sold :
        return  1

    # la couleur ne correspond ni à une victoire, ni à une défaite
    else:
        return 2

def roll_win():
    """
    en cas de victoire ou 1er mise
    """
    reset()
    roll()

def roll_loose():
    """
    en cas de défaite
    """
    martinguale()
    roll()

def new_log():
    """
    Création du fichier log avec la date et l'heure de début
    """
    # Recuperation de la date et heure :
    t = time.ctime()
    sold = get_sold()
    
    # écriture des infos
    with open("log.txt", "w") as f:
        txt = f"----- START ----- \n"\
        f"{t} \n"\
        f"Sold : {sold} \n\n"
        f.write(txt)

def final_log(win, loose, rolled, s_start, s_end):
    """
    Ecriture du résumué de la partie dans log.txt
    """
    # calcule de la durée de la partie
    s = s_end - s_start

    # récupère le sold total du joueur
    sold = get_sold()

    # Recuperation de la date et heure :
    t = time.ctime()

    # écriture des infos
    with open("log.txt", "a") as f:
        txt = f"----- END ----- \n"\
        f"{t} \n"\
        f"New sold : {sold} \n"\
        f"Total games : {rolled} \n"\
        f"Won : {win} \n"\
        f"Lost : {loose} \n"\
        f"Duration : {s}s"
        f.write(txt)

def play(max_win, max_loose):
    """
    lancer la partie
    """
    #max_win = 100 # gain max
    #max_loose = 10 # perte max
    win = 0 # nbr de victoires
    loose = 0 # nbr de defaites
    loose_row = 0 # nbre de pertes consecutives
    rolled = 0 # nbr de parties jouées
    result = 2 # 0 quand la partie est gagné et 1 quand s'est perdu
    s_start = 0 # secondes depuis epoch
    s_end = 0 # secondes depuis epoch

    print("Playing ...")
    
    # Création du log
    new_log()

    # selection du navigateur
    alttab()

    # start Chrono
    s_start = time.time()

    sold = get_sold()

    # 1ere mise
    roll_win()
    rolled += 1

    result = get_result(sold)

    # si la limite de perte consécutive n'est pas atteinte
    while loose_row < max_loose :
    
        # si c'est une victoire
        if result == 0 :
            print('win')
            win += 1 # incremente le nbr de victoires
            loose_row = 0 # remise a 0 des pertes consecutives

            # si la limite de gain n'est pas atteinte
            if rolled < max_win :
                # relance les dés
                sold = get_sold()
                roll_win()
                rolled += 1
                result = get_result(sold)
            else:
                print("Max win limit")
                break
    
        # si c'est une défaite
        elif result == 1 :
            print('Loose')
            # incrémente les compteurs de défaites
            loose += 1
            loose_row += 1

            # relance les dés
            sold = get_sold()
            roll_loose()
            rolled += 1
            result = get_result(sold)
    
        # si ne reconnais ni une victoire ni une defaite
        else:
            # relance l'analyse du resultat
            n = 0
            while n < 60 and result >= 2 :
                print('No result')
                print('Retry ...')
                time.sleep(1)
                result = get_result(sold)
                n += 1
            
            # si le resultat ne correspond ni à une victoire ni une défaite malgrès les tentatives
            if result >= 2 :
                sold = get_sold()
                roll()
                result = get_result(sold)
   
    # stop chrono
    s_end = time.time()
    
    # si la limite de perte est pas atteinte
    if loose_row >= max_loose :
        print("Limite de pertes consecutives atteinte")

    # écriture du compte rendu final dans le log
    final_log(win, loose, rolled, s_start, s_end)

    alttab()