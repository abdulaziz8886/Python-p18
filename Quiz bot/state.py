from aiogram.fsm.state import State, StatesGroup
class user_form(StatesGroup):
    login = State()
    parol = State()
    parol2 = State()
    tell = State()
    finish = State()

class kirish_form(StatesGroup):
    login = State()
    parol = State()


class login_almash(StatesGroup):
    login1 = State()
    login2 = State()


class parol_almash(StatesGroup):
    parol1 = State()
    parol2 = State()


class taklifForm(StatesGroup):
    taklif = State()


class chiqishForm(StatesGroup):
    chiqish = State()


class FanForm(StatesGroup):
    name = State()


class SavolForm(StatesGroup):
    savol = State()
    a = State()
    b = State()
    c = State()
    tj = State()
    finish = State()
    finish2 = State()



class Fandelete(StatesGroup):
    a = State()
    fan = State()
    finish = State()


class SavolDel(StatesGroup):
    fan = State()
    savol = State()
    final = State()


class TestIshla(StatesGroup):
    fan = State()
    savol = State()

class foydalanuvchi(StatesGroup):
    user = State()
    finish = State()
    

class cntForm(StatesGroup):
    first = State()


















    