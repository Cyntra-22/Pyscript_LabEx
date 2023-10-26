class Calculator:
    def __init__(self, num_first, num_second, sign_click, cal_type):
        self.num_first = num_first
        self.num_second = num_second
        self.sign_click = sign_click
        self.cal_type = cal_type


demo_calculator = Calculator("", "", "", "")
answer = Element("typing-text")
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."]
sign = ["equal-to", "ac", "backspace"]


def numbers_clicked(args):
    typed_in = args.target.innerText

    if typed_in in numbers and demo_calculator.sign_click == "":
        answer.element.innerText += typed_in
        demo_calculator.num_first = answer.element.innerText

    elif typed_in in numbers and demo_calculator.sign_click != "":
        Element("typing-text").element.innerHTML += typed_in
        demo_calculator.num_second += typed_in   


def sign_clicked(args):
    if args.target.id == "equal-to":
       calculate()
    elif args.target.id == "delete":
       delete()
    elif args.target.id == "ac":
        clear_all()
    elif args.target.id not in sign:
        demo_calculator.cal_type = args.target.id
        demo_calculator.sign_click = args.target.innerText
        Element("typing-text").element.innerHTML += "<span>" + demo_calculator.sign_click + "</span>"


def calculate():
    new_total = 0
    try:
        if demo_calculator.cal_type == "multiply":
            new_total = float(demo_calculator.num_first) * float(demo_calculator.num_second)
        elif demo_calculator.cal_type == "divid":
            if float(demo_calculator.num_second) == 0:
                new_total = "infinity"
            else:
                new_total = float(demo_calculator.num_first) / float(demo_calculator.num_second)

        elif demo_calculator.cal_type == "minus":
            new_total = float(demo_calculator.num_first) - float(demo_calculator.num_second)
        elif demo_calculator.cal_type == "plus":
            new_total = float(demo_calculator.num_first) + float(demo_calculator.num_second)

        Element("answer").element.innerText = new_total

    except Exception:
        Element("answer").element.innerText = "Infinity"  


def clear_all():
    demo_calculator.num_first = ""
    demo_calculator.num_second = ""
    demo_calculator.cal_type = ""
    demo_calculator.sign_click = ""
    Element("typing-text").element.innerHTML = ""
    Element("answer").element.innerText = ""


def delete():

    currentText = Element("typing-text").element.innerHTML
    Element("typing-text").element.innerHTML = currentText.slice(0, -1)



