import terms as v

""" terms for the light """

""" capabilities """
_light = "light"
_onOff = "onOff"
_brightness = "brightness"
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
_currentValue = "currentValue"
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
_targetValue = "targetValue"
_targetBrightness = "targetBrightness"
_targetHue = "targetHue"
_targetSaturation = "targetSaturation"
_targetX = "targetX"
_targetY = "targetY"
_targetRed = "targetRed"
_targetBlue = "targetBlue"
_targetGreen = "targetGreen"
_targetTemperature = "targetTemperature"
_moveRate = "moveRate"
_stepSize = "stepSize"
_remainingTime = "remainingTime"


light = { 
    v._schema: [
        {
        v._rdfClass: _light,
        v._rdfType: v._capability,
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [ _onOff, _brightness, _color],
        v._description: """ base capability for lighting control """
        },
        {
        v._rdfClass: _onOff,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_currentState, _targetState, _change, _propertyValueChange],
        v._description: """ on/off control """
        },
        {
        v._rdfClass: _brightness,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_currentBrightness, _targetBrightness, 
                   _change, _step, _move, _stop, 
                   _propertyValueChange],
        v._description: """ level control """
        },
        {
        v._rdfClass: _color,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._description: """ color control """
        },
        {
        v._rdfClass: _colorHS,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_currentHue, _currentSaturation, _targetHue, _targetSaturation, 
                   _transitionTime, _remainingTime,
                   _change, _step, _move, _stop,
                   _propertyValueChange],
        v._description: """ HS color control """
        },
        {
        v._rdfClass: _colorXY,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_currentX, _currentY, _targetX, _targetY, 
                   _transitionTime, _remainingTime,
                   _change, _step, _move, _stop,
                   _propertyValueChange],
        v._description: """ XY (CIE) Color control """
        },
        {
        v._rdfClass: _colorRGB,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_currentRed, _currentGreen, _currentBlue, 
                   _targetRed, _targetGreen, _targetBlue, 
                   _transitionTime, _remainingTime,
                   _change, _step, _move, _stop,
                   _propertyValueChange],
        v._description: """ RGB Color Control """
        },
        {
        v._rdfClass: _colorTemperature,
        v._rdfType: v._capability,
        v._usedBy: [_light],
        v._mayHave: [_currentTemperature, _targetTemperature, 
                   _transitionTime, _remainingTime,
                   _change, _step, _move, _stop, 
                   _propertyValueChange],
        v._description: """ color Temperature control """
        },
        {
        v._rdfClass: _change,
        v._rdfType: v._action,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [_targetValue, _transitionTime],
        v._description: """ change action """
        },
        {
        v._rdfClass: _move,
        v._rdfType: v._action,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [_moveRate],
        v._description: """ move action """
        },
        {
        v._rdfClass: _step,
        v._rdfType: v._action,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [_stepSize, _transitionTime],
        v._description: """ step action """
        },
        {
        v._rdfClass: _stop,
        v._rdfType: v._action,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [],
        v._description: """ stop action """
        },
        {
        v._rdfClass: _propertyValueChange,
        v._rdfType: v._event,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [v._params],
        v._description: """ event for changes in the value of a property """
        },
        {
        v._rdfClass: _actionInvoked,
        v._rdfType: v._event,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [v._params],
        v._description: """ event for changes in the value of a property """
        },
        {
        v._rdfClass: _actionCompleted,
        v._rdfType: v._event,
        v._usedBy: [_onOff, _brightness, _colorHS, _colorXY, _colorRGB, _colorTemperature],
        v._mayHave: [v._params],
        v._description: """ event for changes in the value of a property """
        },
    ]
}