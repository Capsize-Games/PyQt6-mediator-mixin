from PyQt6_mediator_mixin.enums import SignalCode as DefaultSignalCode

_signal_code = DefaultSignalCode


def get_signal_code():
    return _signal_code


def set_signal_code(signal_code):
    global _signal_code
    _signal_code = signal_code
