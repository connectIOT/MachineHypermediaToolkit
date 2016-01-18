
""" these terms should come from the base schema and domain schema """
_index = "index"
_capability = "capability"
_thing = "thing"
_action = "action"
_event = "event"
_property = "property"
_actuation = "actuation"
_subscription = "subscription"
_notification = "notification"

""" these terms are from the domain schema """
_light = "light"
_onoff = "onoff"
_brightness = "brightness"
_colorhs = "colorhs"
_change = "change"
_move = "move" 
_step = "step"
_stop = "stop"

""" this table is a stub for using the appropriate application schema 
    to determine the WoT resource type of a particular domain type """
_domainType = {
           _index: _index,
           _light: _thing,
           _onoff: _capability,
           _brightness: _capability,
           _colorhs: _capability,
           _change: _action,
           _move: _action,
           _step: _action,
           _stop: _action,
           "currentState": _property,
           "targetState": _property,
           "delayTime": _property,
           "currentBrightness": _property,
           "targetBrightness": _property,
           "moveBrightness": _property,
           "stepBrightness": _property,
           "transitionTime": _property
           }

""" this list replaces lookup of the domain model property "hasEvent, etc. """
_collections = [
                "events",
                "actions",
                "properties",
                "capabilities",
                ]
