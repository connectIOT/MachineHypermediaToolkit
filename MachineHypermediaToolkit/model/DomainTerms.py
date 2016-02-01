
import MachineHypermediaToolkit.terms as v

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

_dtype = "dtype"
_dval = "dval"

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
           "currentstate": _property,
           "targetstate": _property,
           "delaytime": _property,
           "currentbrightness": _property,
           "targetbrightness": _property,
           "movebrightness": _property,
           "stepbrightness": _property,
           "transitiontime": _property,
           "currentcolorh": _property,
           "currentcolors": _property,
           "targetcolorh": _property,
           "targetcolors": _property
           }

_propertyType = {
    "currentstate": {_dtype: v._bv, _dval: False },
    "targetstate": {_dtype: v._bv, _dval: False },
    "delaytime": {_dtype: v._v, _dval: 0 },
    "currentbrightness": {_dtype: v._v, _dval: 0 },
    "currentcolorh": {_dtype: v._v, _dval: 0 },
    "currentcolors": {_dtype: v._v, _dval: 0 },
    "targetcolorh": {_dtype: v._v, _dval: 0 },
    "targetcolors": {_dtype: v._v, _dval: 0 },
    "targetbrightness": {_dtype: v._v, _dval: 0 },
    "movebrightness": {_dtype: v._v, _dval: 0 },
    "stepbrightness": {_dtype: v._v, _dval: 0 },
    "transitiontime": {_dtype: v._v, _dval: 0 }
     }


""" this list replaces lookup of the domain model property "hasEvent, etc. """
_collections = [
                "events",
                "actions",
                "properties",
                "capabilities",
                ]

_templates = [
    {
        v._rt: [_change, _brightness],
        v._template: [{v._n: "targetbrightness", v._v: "$targetbrightness" },
                      {v._n: "transitiontime", v._v: "$transitiontime" }]
     },
    {
        v._rt: [_move, _brightness],
        v._template: [{v._n: "movebrightness", v._v: "$movebrightness" }]
     },
    {
        v._rt: [_step, _brightness],
        v._template: [{v._n: "stepbrightness", v._v: "$stepbrightness" },
                      {v._n: "transitiontime", v._v: "$transitiontime" }]
     },
    {
        v._rt: [_change, _colorhs],
        v._template: [{v._n: "targetcolorh", v._v: "$targetcolorh" },
                      {v._n: "targetcolors", v._v: "$targetcolors" },
                      {v._n: "transitiontime", v._v: "$transitiontime" }]
     },
    {
        v._rt: [_change, _onoff],
        v._template: [{v._n: "targetstates", v._bv: "$targetstate" },
                      {v._n: "delaytime", v._v: "$delaytime" }]
     }         
]