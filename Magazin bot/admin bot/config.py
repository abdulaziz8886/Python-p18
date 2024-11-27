from aiogram.fsm.state import StatesGroup, State
token = "7872799380:AAH6MuOWYdDt7CeMnheUCf5TtThGzknJ-hQ"


class Admin(StatesGroup):
    start = State()    
    kategor = State()
    maxsulot = State()
    maxsulot_qosish = State()
    maxsulot_nomi = State()
    maxsulot_rasm = State()
    maxsulot_tekshir2 = State()
    maxsulot_end = State()

class User(StatesGroup):
    kategorya = State()
    maxsulot = State()
    maxsulot_soni = State()
    finaly = State()