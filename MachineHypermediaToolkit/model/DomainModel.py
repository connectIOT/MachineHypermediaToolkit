import json
import MachineHypermediaToolkit.terms as v
import DomainTerms as d

light = {
    v._context : "http://thingschema.org",
    v._label: "light",
    v. _resource:[
        {
            v._name: "light", 
            v._type:"light",
            "capabilities": [
                {
                    v._name:"onOff", 
                    v._type:"onoff", 
                    "actions":[
                        {v._name:"change", v._type:"change"}
                    ],
                    "properties": [
                        {v._name: "currentState", v._type: "currentstate"},
                        {v._name: "targetState", v._type: "targetstate"},
                        {v._name: "delayTime", v._type: "delaytime"}
                    ]

                }, 
                {
                    v._name:"colorHS",
                    v._type:"colorhs", 
                    "actions": [
                        {v._name:"change", v._type:"change"}
                    ],
                    "properties": [
                        {v._name: "currentcolorh", v._type: "currentcolorh"},
                        {v._name: "currentcolors", v._type: "currentcolors"},
                        {v._name: "targetcolorh", v._type: "targetcolorh"},
                        {v._name: "targetcolors", v._type: "targetcolors"},
                        {v._name: "transitionTime", v._type: "transitiontime"}
                    ]
                }, 
                {
                    v._name:"brightness",
                    v._type:"brightness", 
                    "actions": [
                        {v._name:"change", v._type:"change"},
                        {v._name:"move", v._type:"move"}, 
                        {v._name:"step", v._type:"step"}
                    ],
                    "properties": [
                        {v._name: "currentBrightness", v._type: "currentbrightness"},
                        {v._name: "targetBrightness", v._type: "targetbrightness"},
                        {v._name: "moveBrightness", v._type: "movebrightness"},
                        {v._name: "stepBrightness", v._type: "stepbrightness"},
                        {v._name: "transitionTime", v._type: "transitiontime"}
                    ]
                }
            ]
        },
        {
            v._name: "index",
            v._type:"index",
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
