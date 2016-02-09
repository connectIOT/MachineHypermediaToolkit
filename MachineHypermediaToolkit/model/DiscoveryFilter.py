import MachineHypermediaToolkit.terms  as v
import DomainTerms as d
import json

_filter = [
    {
        v._rt: d._light,
        v._label: d._light,
        v._has: [
                 {
                  v._rt: d._brightness,
                  v._label: d._brightness,
                  v._has:[
                    {
                        v._rt: d._currentbrightness,
                        v._label: d._currentbrightness
                    },
                    {
                        v._rt: d._targetbrightness,
                        v._label: d._targetbrightness
                    },
                    {
                        v._rt: d._transitiontime,
                        v._label: d._transitiontime
                    },
                    {
                        v._rt: d._change,
                        v._label: d._change
                    }
                ]
            },
            {
                v._rt: d._colorhs,
                v._label: d._colorhs,
                v._has:[
                    {
                        v._rt: d._currentcolorh,
                        v._label: d._currentcolorh
                    },
                    {
                        v._rt: d._currentcolors,
                        v._label: d._currentcolors
                    },
                    {
                        v._rt: d._targetcolorh,
                        v._label: d._targetcolorh
                    },
                    {
                        v._rt: d._targetcolors,
                        v._label: d._targetcolors
                    },
                    {
                        v._rt: d._transitiontime,
                        v._label: d._transitiontime
                    },
                    {
                        v._rt: d._change,
                        v._label: d._change
                    }
                ]
             },
            {
                v._rt: d._onoff,
                v._label: d._onoff,
                v._has:[
                    {
                        v._rt: d._currentstate,
                        v._label: d._currentstate
                    },
                    {
                        v._rt: d._targetstate,
                        v._label: d._targetstate
                    },
                    {
                        v._rt: d._delaytime,
                        v._label: d._delaytime
                    },
                    {
                        v._rt: d._change,
                        v._label: d._change
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
