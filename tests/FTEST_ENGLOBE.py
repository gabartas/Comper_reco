
import datetime
import time


class TimeHandler:

    def __init__(self) -> None:
        self.start_time = 0

    def startTimer(self, textToDisplay):
        print("\t" + textToDisplay, end="")
        self.start_time = time.time()

    def stopTimer(self):
        time_to_do = time.time() - self.start_time
        print(" -->  ", time_to_do, "s")

    def getDateTime():
        return str(datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S_%f"))


def timerDecorator(text: str, func):
    timer = TimeHandler()
    timer.startTimer(text)
    dataToReturn = func
    timer.stopTimer()
    return dataToReturn


def test(text: str):
    return f"Fonction A tester avec argument {text}"


def fmain():
    print("Fonction Principale")
    data = timerDecorator("timerDeco", test("mon argument"))
    print(data)


fmain()
