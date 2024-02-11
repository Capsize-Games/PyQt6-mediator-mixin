# PyQt6 Mediator Mixin

`PyQt6 Mediator Mixin` is a Python library that enhances PyQt6's signal-slot mechanism by implementing the mediator pattern. This pattern allows classes to emit and receive signals without knowing about each other, leading to more modular and maintainable code.

Key features:

- Mediator pattern implementation for PyQt6 signals.
- Ability to extend the `SignalCode` enum for custom signals.

## Installation

```bash
pip install PyQt6_mediator_mixin
```

## Usage

```python
from PyQt6_mediator_mixin.mediator_mixin import MediatorMixin
from PyQt6_mediator_mixin.enums import SignalCode

class MyClass(MediatorMixin):
    def __init__(self):
        super().__init__()
        self.register(SignalCode.MY_SIGNAL, self.my_slot_function)

    def my_slot_function(self, data):
        print("Received signal with data:", data)

    def some_method(self):
        self.emit(SignalCode.MY_SIGNAL, "some data")
```

## Extending SignalCode Enum

```python
from enum import Enum
from PyQt6_mediator_mixin.signal_code_factory import set_signal_code

class MySignalCode(Enum):
    MY_SIGNAL_1 = 1
    MY_SIGNAL_2 = 2

set_signal_code(MySignalCode)
```

Now, `MyClass` can register and emit `MY_SIGNAL_1` and `MY_SIGNAL_2` using the `MediatorMixin`.