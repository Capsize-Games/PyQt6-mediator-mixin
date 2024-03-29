from PyQt6.QtCore import QObject, pyqtSignal

from PyQt6_mediator_mixin.signal_code_factory import get_signal_code


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Signal(QObject):
    """
    This class represents a signal that can be emitted and received.
    """
    signal = pyqtSignal(object)


SIGNALS = {}


class SignalMediator(metaclass=SingletonMeta):
    """
    This class is responsible for mediating signals between classes.
    """

    def register(
        self,
        code,
        slot_function: object
    ):
        """
        Register a signal to be received by a class.

        :param code: The SignalCode of the signal to register
        :param slot_function: The function to call when the signal is received.
        """
        signal_code = get_signal_code()
        if isinstance(code, signal_code) and code not in SIGNALS:
            # Create a new Signal instance for this signal name
            SIGNALS[code] = Signal()
        # Connect the Signal's pyqtSignal to receive the method of the slot parent
        try:
            SIGNALS[code].signal.connect(slot_function)
        except Exception as e:
            print(f"Error connecting signal {code}", e)

    def emit(
        self,
        code,
        data: object = None
    ):
        """
        Emit a signal.
        :param code:
        :param data:
        :return:
        """
        signal_code = get_signal_code()
        if isinstance(code, signal_code) and code in SIGNALS:
            SIGNALS[code].signal.emit(data)
