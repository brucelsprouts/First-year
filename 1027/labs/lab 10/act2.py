class Fan:
    OFF = 0
    ON = 1
    _state = OFF

    def __init__(self):
        # Initial state
        Fan._state = Fan.OFF  #1

    def turn_on(self):
        Fan._state = Fan.ON

    def turn_off(self):
        Fan._state = Fan.OFF  #2

    def get_stateValue(self):
        if Fan._state == Fan.ON:
            return "Fan is On"
        else:
            return "Fan is OFF"  #3

# Usage
fan1 = Fan()
fan1.turn_on()
print("Fan is", fan1.get_stateValue())  # Output: Fan is On
fan1.turn_off()
print("Fan is", fan1.get_stateValue())  # Output: Fan is OFF
