class FiguresException(Exception):
    default_code = "error"
    default_title = "Что-то пошло не так"
    default_message = "Никто не знает что произошло :("

    def __init__(self, code=None, title=None, message=None, data=None):
        self.code = code or self.default_code
        self.title = title or self.default_title
        self.message = message or self.default_message
        self.data = data or {}


class DownloadLimitException(FiguresException):
    default_code = "download-limit"
    default_title = "какая-то фигня с загрузкой:(("    
    default_message = f"либо вы пытаетесь загрузить больше 100 кругов за день (остановитес!), либо у нас уже нет столько, сколько вы просите. ну или еще че, я хз"
