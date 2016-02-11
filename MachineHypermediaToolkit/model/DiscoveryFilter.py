import MachineHypermediaToolkit.terms  as v
import DomainTerms as d
import json

_filter = [
    {
        v._rt: d._light,
        v._label: "mylight",
        v._has: [
                 {
                  v._rt: d._brightness,
                  v._label: "dimmer-control",
                  v._has:[
                    {
                        v._rt: d._currentbrightness,
                        v._label: "current-level"
                    },
                    {
                        v._rt: d._targetbrightness,
                        v._label: "target-level"
                    },
                    {
                        v._rt: d._transitiontime,
                        v._label: "brightness-ramp"
                    },
                    {
                        v._rt: d._change,
                        v._label: "brightness-change"
                    }
                ]
            },
            {
                v._rt: d._colorhs,
                v._label: "color-control",
                v._has:[
                    {
                        v._rt: d._currentcolorh,
                        v._label: "current-hue"
                    },
                    {
                        v._rt: d._currentcolors,
                        v._label: "current-saturation"
                    },
                    {
                        v._rt: d._targetcolorh,
                        v._label: "target-hue"
                    },
                    {
                        v._rt: d._targetcolors,
                        v._label: "target-saturation"
                    },
                    {
                        v._rt: d._transitiontime,
                        v._label: "color-ramp"
                    },
                    {
                        v._rt: d._change,
                        v._label: "colorhs-change"
                    }
                ]
             },
            {
                v._rt: d._onoff,
                v._label: "onoff-control",
                v._has:[
                    {
                        v._rt: d._currentstate,
                        v._label: "current-onoff"
                    },
                    {
                        v._rt: d._targetstate,
                        v._label: "target-onoff"
                    },
                    {
                        v._rt: d._delaytime,
                        v._label: "onoff-delay"
                    },
                    {
                        v._rt: d._change,
                        v._label: "onoff-change"
                    }
                ]
            }
        ]
    }
]

def filterString():
    return json.dumps(_filter)
    
def selfTest():
    print json.dumps(_filter, sort_keys=False, indent=2, separators=(',', ': '))

if __name__ == "__main__" :
    selfTest()
