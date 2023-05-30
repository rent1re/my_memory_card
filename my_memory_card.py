#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint
class Question():###
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
# все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []###
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский') ###
questions_list.append(q1)###
q2 = Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий')###
questions_list.append(q2)###
q3 = Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата')###
questions_list.append(q3)###



app = QApplication([])


window = QWidget()
window.setWindowTitle('Memory Card')
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос!')


RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans_hor = QHBoxLayout()
layout_ans_ver1 = QVBoxLayout()
layout_ans_ver2 = QVBoxLayout()
layout_ans_ver1.addWidget(rbtn_1)
layout_ans_ver1.addWidget(rbtn_2)
layout_ans_ver2.addWidget(rbtn_3)
layout_ans_ver2.addWidget(rbtn_4)


layout_ans_hor.addLayout(layout_ans_ver1)                                           
layout_ans_hor.addLayout(layout_ans_ver2)


RadioGroupBox.setLayout(layout_ans_hor)


#Панель результатов
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))


layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 1)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question,alignment = Qt.AlignHCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)


#layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
#layout_line2.addWidget(RadioGroupBox)


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addStretch(1)
layout_card.addLayout(layout_line1)
layout_card.addStretch(1)


#RadioGroupBox.hide() ##


layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3)
layout_card.addStretch(1)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):###
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными   ###
    answers[1].setText(q.wrong1) ###
    answers[2].setText(q.wrong2) ###
    answers[3].setText(q.wrong3) ###
    lb_Question.setText(q.question) # вопрос    ###
    lb_Correct.setText(q.right_answer) # ответ  ###
    show_question() # показываем панель вопросов 


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('-Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')

cur_question = randint(0,len(questions_list) - 1)
q = questions_list[cur_question]

def next_question():###
# этой функции нужна переменная, в которой будет указываться номер текущего вопроса
# эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
# мы заведем (ниже) свойство window.cur_question.
    window.total += 1
    #window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    #if window.cur_question >= len(questions_list):
        #window.cur_question = 0 # если список вопросов закончился - идем сначала
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили
    


def click_OK(): ###
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос

window.score = 0 
window.total = 0


btn_OK.clicked.connect(click_OK)

next_question()

window.resize(400, 300)
window.setLayout(layout_card)
window.cur_question = -1 ###  
window.show()
app.exec()