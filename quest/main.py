from operator import truediv
import sys
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from threading import Thread
from random import randint
import pathlib

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
mw = Ui_MainWindow()
mw.setupUi(MainWindow)


mw.health_pic.setPixmap(QtGui.QPixmap(pathlib.Path(__file__).parent.resolve().__str__()+"\\img\\heart.webp"))
mw.weight_pic.setPixmap(QtGui.QPixmap(pathlib.Path(__file__).parent.resolve().__str__()+"\\img\\weight.png"))
mw.respect_pic.setPixmap(QtGui.QPixmap(pathlib.Path(__file__).parent.resolve().__str__()+"\\img\\respect.png"))
mw.borrow_lebght_pic.setPixmap(QtGui.QPixmap(pathlib.Path(__file__).parent.resolve().__str__()+"\\img\\home.png"))

mw.win_or_lose_frame.move(190,210)
mw.win_or_lose_frame.hide()
mw.night_plate.move(190,250)
mw.night_plate.hide()
mw.fight_frame.move(360, 45)
mw.fight_frame.hide()
mw.dig_frame.move(360, 70)
mw.dig_frame.hide()
mw.eat_frame.move(360, 70)
mw.eat_frame.hide()
mw.battle_lose.move(190, 250)
mw.battle_lose.hide()
mw.battle_win.move(190, 250)
mw.battle_win.hide()

int_health = int(100)
int_weight = int(30)
int_respect = int(20)
int_borrow_lenght = int(10)
int_day_counter = int(1)

WoL = True

def hide_all_frame():
    mw.fight_frame.hide()
    mw.dig_frame.hide()
    mw.eat_frame.hide()
    mw.stats_frame.hide()
    mw.choose.hide()

def set_new_stats():
    mw.health.setNum(int_health)
    mw.weight.setNum(int_weight)
    mw.respect.setNum(int_respect)
    mw.borrow_lenght.setNum(int_borrow_lenght)
    mw.day.setNum(int_day_counter)

def lose():
    hide_all_frame()
    mw.win_or_lose_label.setText("Вы проиграли :(")
    mw.win_or_lose_frame.show()

def win():
    hide_all_frame()
    mw.win_or_lose_label.setText("Вы выиграли :)")
    mw.win_or_lose_frame.show()

def stats_check():
    global WoL
    if int_health <= 0 or int_weight <= 0 or int_respect <= 0 or int_borrow_lenght <= 0:
        lose()
        WoL = False
    elif int_respect > 100:
        win()
        WoL = False

def night():
    thread_1 = Thread(target = night_)
    thread_1.start()

def night_():
    hide_all_frame()
    mw.night_plate.show()
    time.sleep(1)
    mw.night_plate.hide()
    mw.stats_frame.show()
    mw.choose.show()
    global int_health
    global int_weight       
    global int_respect
    global int_borrow_lenght
    global int_day_counter
    int_health += 20
    int_weight -= 5
    int_respect -= 2
    int_borrow_lenght -= 2
    int_day_counter +=1
    set_new_stats()
    stats_check()

def click_dig_button():
    mw.choose.hide()
    mw.dig_frame.show()

def click_eat_button():
    mw.choose.hide()
    mw.eat_frame.show()

def click_fight_button():
    mw.choose.hide()
    mw.fight_frame.show()

def click_sleep_button():
    global int_health
    global int_weight       
    global int_respect
    global int_borrow_lenght
    int_health += 20
    int_weight -= 5
    int_respect -= 2
    int_borrow_lenght -= 2
    set_new_stats()
    night()
    stats_check()

def click_back_button():
    mw.fight_frame.hide()
    mw.dig_frame.hide()
    mw.eat_frame.hide()
    mw.choose.show()

def replay_button():
    global int_health
    global int_weight       
    global int_respect
    global int_borrow_lenght
    global int_day_counter
    global WoL
    WoL = True
    int_health = 100
    int_weight = 30
    int_respect = 20
    int_borrow_lenght = 10
    int_day_counter = 1
    set_new_stats()
    mw.win_or_lose_frame.hide()
    mw.stats_frame.show()
    mw.choose.show()

def intensivelt_button_func():
    global int_borrow_lenght
    global int_health
    int_borrow_lenght += 5
    int_health -= 30
    set_new_stats()
    stats_check()
    if WoL:
        night()

def lazily_button_func():
    global int_borrow_lenght
    global int_health
    int_borrow_lenght += 2
    int_health -= 10
    set_new_stats()
    stats_check()
    if WoL:
        night()

def withered_grass_button():
    global int_health
    global int_weight
    int_health += 10
    int_weight += 15
    set_new_stats()
    stats_check()
    if WoL:
        night()

def green_grass_button():
    global int_health
    global int_weight
    if int_respect < 30:
        int_health -= 30
        set_new_stats()
        stats_check()
        if WoL:
            night()
    else:
        int_health += 30
        int_weight += 30
        set_new_stats()
        stats_check()
        if WoL:
            night()

def victory_in_battle(ew):
    rndHp = randint(0,ew + int_weight)
    if rndHp <= int_weight:
        return True
    else:
        return False

def win_message():
    thread_2 = Thread(target = win_message_)
    thread_2.start()

def win_message_():
    hide_all_frame()
    mw.battle_win.show()
    time.sleep(1)
    mw.battle_win.hide()
    mw.stats_frame.show()
    mw.choose.show()
    
def lose_message():
    thread_3 = Thread(target = lose_message_)
    thread_3.start()

def lose_message_():
    hide_all_frame()
    mw.battle_lose.show()
    time.sleep(1)
    mw.battle_lose.hide()
    mw.stats_frame.show()
    mw.choose.show()

def result_of_winning_a_battle(ew):
    global int_health
    global int_respect
    if int_weight - ew == 0:
        int_respect += 5
        int_health -= 1
    elif ew - int_weight >= 30:
        int_respect += 20
        int_health -= 15
    elif ew - int_weight >= 15 and ew - int_weight < 30:
        int_respect += 15
        int_health -= 10
    elif ew - int_weight > 0 and ew - int_weight < 15:
        int_respect += 15
        int_health -= 5
    elif ew - int_weight < 0:
        int_respect += 5

def result_of_defeat_in_battle(ew):
    global int_health
    global int_respect
    if ew - int_weight == 0:
        int_respect -= 10
        int_health -= 10
    elif ew - int_weight > 0:
        int_health -= 20
        int_respect -= 5
    elif ew - int_weight < 0:
        int_health -= 5
        int_respect -= 20

def fight_func(enemy_weight):
    if victory_in_battle(enemy_weight):
        result_of_winning_a_battle(enemy_weight)
        set_new_stats()
        win_message()
        stats_check()
        if WoL:
            night()
    else:
        result_of_defeat_in_battle(enemy_weight)
        set_new_stats()
        lose_message()
        stats_check()
        if WoL:
            night()

def week_enemy_button():
    enem_weight = int(30)
    fight_func(enem_weight)

def average_enemy_button():
    enem_weight = int(50)
    fight_func(enem_weight)

def strong_enemy_button():
    enem_weight = int(70)
    fight_func(enem_weight)

mw.dig.clicked.connect(click_dig_button)
mw.eat.clicked.connect(click_eat_button)
mw.fight.clicked.connect(click_fight_button)
mw.sleep.clicked.connect(click_sleep_button)

mw.intensively_button.clicked.connect(intensivelt_button_func)
mw.lazily_button.clicked.connect(lazily_button_func)
mw.back_button_1.clicked.connect(click_back_button)

mw.withered_grass.clicked.connect(withered_grass_button)
mw.green_grass.clicked.connect(green_grass_button)
mw.back_button_2.clicked.connect(click_back_button)

mw.week_enemy.clicked.connect(week_enemy_button)
mw.average_enemy.clicked.connect(average_enemy_button)
mw.strong_enemy.clicked.connect(strong_enemy_button)
mw.back_button_3.clicked.connect(click_back_button)

mw.replay.clicked.connect(replay_button)
MainWindow.show()
sys.exit(app.exec_())