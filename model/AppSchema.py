import terms as v

""" terms for the light """

""" capabilities """
_light = "light"
_onOff = "onOff"
_level = "level"
_color = "color"
_colorHS = "colorHS"
_colorXY = "colorXY"
_colorRGB = "colorRGB"
_colorTemperature = "colorTemperature"

""" params """
_state = "state"
_brightness = "brightness"
_hue = "hue"
_saturation = "saturation"
_colorX = "colorX"
_colorY = "colorY"
_red = "red"
_blue = "blue"
_green = "green"
_transitionTime = "transitionTime"

_on = "on"
_off = "off"
_toggle = "toggle"


""" Actions """
_step = "step"
_move = "move"
_change = "change"
_stop = "stop"

""" Events """
_propertyValueChange = "propertyValueChange"
_actionInvoked = "actionInvoked"
_actionCompleted = "actionCompleted"

""" Properties """
_currentState = "currentState"
_currentBrightness = "currentBrightness"
_currentHue = "currentHue"
_currentSaturation = "currentSaturation"
_currentX = "currentX"
_currentY = "currentY"
_currentRed = "currentRed"
_currentBlue = "currentBlue"
_currentGreen = "currentGreen"
_currentTemperature = "currentTemperature"

_targetState = "targetState"
_targetBrightness = "targetBrightness"
_targetHue = "targetHue"
_targetSaturation = "targetSaturation"
_targetX = "targetX"
_targetY = "targetY"
_targetRed = "targetRed"
_targetBlue = "targetBlue"
_targetGreen = "targetGreen"
_targetTemperature = "targetTemperature"
_remainingTime = "remainingTime"



light = \
    [
        {
        v._className: _light,
        v._subClassOf: v._capability,
        v._domain: [v._thing, v._capability],
        v._range: [ _onOff, _level, _color],
        v._description: """ base capability for lighting control """
        },
        {
        v._className: _onOff,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_currentState, _targetState, _change, _propertyValueChange],
        v._description: """ on/off control """
        },
        {
        v._className: _level,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_currentBrightness, _targetBrightness, _change, _step, _move, _stop, _propertyValueChange],
        v._description: """ level control """
        },
        {
        v._className: _color,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._description: """ color control """
        },
        {
        v._className: _colorHS,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_currentHue, _currentSaturation, _targetHue, _targetSaturation, 
                   _change, _step, _move, _stop,
                   _propertyValueChange],
        v._description: """ HS color control """
        },
        {
        v._className: _colorXY,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_currentX, _currentY, _targetX, _targetY, 
                   _change, _step, _move, _stop,
                   _propertyValueChange],
        v._description: """ XY (CIE) Color control """
        },
        {
        v._className: _colorRGB,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_currentRed, _currentGreen, _currentBlue, 
                   _targetRed, _targetGreen, _targetBlue, 
                   _change, _step, _move, _stop,
                   _propertyValueChange],
        v._description: """ RGB Color Control """
        },
        {
        v._className: _colorTemperature,
        v._subClassOf: v._capability,
        v._domain: [_light],
        v._range: [_currentTemperature, _targetTemperature, 
                   _change, _step, _move, _stop, 
                   _propertyValueChange],
        v._description: """ color Temperature control """
        },
        {
        v._className: _change,
        v._subClassOf: v._action,
        v._domain: [_onOff, _level, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._range: [v._params],
        v._description: """ change action """
        },
    ]
