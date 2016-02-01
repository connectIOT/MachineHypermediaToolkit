
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

_events = "events"
_actions = "actions"
_properties = "properties"
_capabilities = "capabilities"
_links = "links"

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

_currentstate = "currentstate"
_targetstate = "targetstate"
_delaytime = "delaytime"
_currentbrightness = "currentbrightness"
_targetbrightness = "targetbrightness"
_movebrightness = "movebrightness"
_stepbrightness = "stepbrightness"
_transitiontime = "transitiontime"
_currentcolorh = "currentcolorh"
_currentcolors = "currentcolors"
_targetcolorh = "targetcolorh"
_targetcolors = "targetcolors"

    
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
           _currentstate: _property,
           _targetstate: _property,
           _delaytime: _property,
           _currentbrightness: _property,
           _targetbrightness: _property,
           _movebrightness: _property,
           _stepbrightness: _property,
           _transitiontime: _property,
           _currentcolorh: _property,
           _currentcolors: _property,
           _targetcolorh: _property,
           _targetcolors: _property
           }

_propertyType = {
    _currentstate: {_dtype: v._bv, _dval: False },
    _targetstate: {_dtype: v._bv, _dval: False },
    _delaytime: {_dtype: v._v, _dval: 0 },
    _currentbrightness: {_dtype: v._v, _dval: 0 },
    _currentcolorh: {_dtype: v._v, _dval: 0 },
    _currentcolors: {_dtype: v._v, _dval: 0 },
    _targetcolorh: {_dtype: v._v, _dval: 0 },
    _targetcolors: {_dtype: v._v, _dval: 0 },
    _targetbrightness: {_dtype: v._v, _dval: 0 },
    _movebrightness: {_dtype: v._v, _dval: 0 },
    _stepbrightness: {_dtype: v._v, _dval: 0 },
    _transitiontime: {_dtype: v._v, _dval: 0 }
     }


""" this list replaces lookup of the domain model property "hasEvent, etc. """
_collections = [
                _events,
                _actions,
                _properties,
                _capabilities
                ]

_content = [
            _links
            ]

_templates = [
    {
        v._rt: [_change, _brightness],
        v._template: {v._e: [{v._n: "targetbrightness", v._v: "$targetbrightness" },
                      {v._n: "transitiontime", v._v: "$transitiontime" }] }
     },
    {
        v._rt: [_move, _brightness],
        v._template: {v._e: [{v._n: "movebrightness", v._v: "$movebrightness" }] }
     },
    {
        v._rt: [_step, _brightness],
        v._template: {v._e: [{v._n: "stepbrightness", v._v: "$stepbrightness" },
                      {v._n: "transitiontime", v._v: "$transitiontime" }] }
     },
    {
        v._rt: [_change, _colorhs],
        v._template: {v._e: [{v._n: "targetcolorh", v._v: "$targetcolorh" },
                      {v._n: "targetcolors", v._v: "$targetcolors" },
                      {v._n: "transitiontime", v._v: "$transitiontime" }] }
     },
    {
        v._rt: [_change, _onoff],
        v._template: {v._e: [{v._n: "targetstates", v._bv: "$targetstate" },
                      {v._n: "delaytime", v._v: "$delaytime" }] }
     }         
]