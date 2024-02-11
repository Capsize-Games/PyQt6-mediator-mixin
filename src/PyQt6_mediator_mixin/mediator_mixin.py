from PyQt6_mediator_mixin.signal_code_factory import get_signal_code
from PyQt6_mediator_mixin.signal_mediator import SignalMediator


class MediatorMixin:
    """
    Use with any class that needs to emit and receive signals.
    Initialize with a SignalMediator instance.
    """
    def __init__(self):
        self.threads = []
        self.workers = []
        self.mediator = SignalMediator()

    def emit(
        self,
        code,
        data: object = None
    ):
        # Pass None as the second argument if no additional arguments are provided
        signal_code = get_signal_code()
        if isinstance(code, signal_code):
            self.mediator.emit(code, data)

    def register(
        self,
        code,
        slot_function: object
    ):
        """
        Accessor method for SignalMediator.register method.
        :param code:
        :param slot_function:
        :return:
        """
        signal_code = get_signal_code()
        if isinstance(code, signal_code):
            self.mediator.register(code, slot_function)
