import json
import MachineHypermediaToolkit.terms as v
import DomainTerms as d

light = {
    v._context : "http://thingschema.org",
    v._label: "light",
    v. _resource:[
        {
            v._name: "light", 
            v._type:d._light,
            d._capabilities: [
                {
                    v._name:"onOff", 
                    v._type:d._onoff, 
                    d._actions:[
                        {v._name:"change", v._type:d._change}
                    ],
                    d._properties: [
                        {v._name: "currentState", v._type: d._currentstate},
                        {v._name: "targetState", v._type: d._targetstate},
                        {v._name: "delayTime", v._type: d._delaytime}
                    ]

                }, 
                {
                    v._name:"colorHS",
                    v._type:d._colorhs, 
                    d._actions: [
                        {v._name:"change", v._type:d._change}
                    ],
                    d._properties: [
                        {v._name: "currentcolorh", v._type: d._currentcolorh},
                        {v._name: "currentcolors", v._type: d._currentcolors},
                        {v._name: "targetcolorh", v._type: d._targetcolorh},
                        {v._name: "targetcolors", v._type: d._targetcolors},
                        {v._name: "transitionTime", v._type: d._transitiontime}
                    ]
                }, 
                {
                    v._name:"brightness",
                    v._type:d._brightness, 
                    d._actions: [
                        {v._name:"change", v._type:d._change},
                        {v._name:"move", v._type:d._move}, 
                        {v._name:"step", v._type:d._step}
                    ],
                    d._properties: [
                        {v._name: "currentBrightness", v._type: d._currentbrightness},
                        {v._name: "targetBrightness", v._type: d._targetbrightness},
                        {v._name: "moveBrightness", v._type: d._movebrightness},
                        {v._name: "stepBrightness", v._type: d._stepbrightness},
                        {v._name: "transitionTime", v._type: d._transitiontime}
                    ]
                }
            ]
        },
        {
            v._name: "index",
            v._type:d._index,
            v._links: [
                {v._href: "/light/", v._rt: [ d._light, d._thing] },
                {v._href: "/light/onOff/", v._rt: [ d._onoff, d._capability] },
                {v._href: "/light/brightness/", v._rt: [ d._brightness, d._capability] },
                {v._href: "/light/colorHS/", v._rt: [ d._colorhs, d._capability] }
            ]
        },                
    ]
}


def selfTest():
    print json.dumps(light, sort_keys=False, indent=2, separators=(',', ': '))
    
if __name__ == "__main__" :
    selfTest()
