def format_message(message, log_class=1):
    #TODO: Add for mating for different meassage types
    return message


class EmuLog:
    INFO = 1
    ERROR = 2
    TIMEOUT = 3

    def __init__(self):
        self.log_file = open("Emu_log.log","w")
        

    def __del__(self):
        self.log_file.close()
    
    def get_logger(self):
        return self

    def log(self,message,):
        self.log_file.write(message)
