def format_message(message, log_class=1):
    return message


class EmuLog:
    INFO = 1
    ERROR = 2
    TIMEOUT = 3

    def __init__(self):
        self.log_file = open("Emu_log","w")

    def log(self,message,):
        self.log_file.write(message)

