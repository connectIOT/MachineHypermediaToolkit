import json
import terms as v

light = {
    v._context : "http://thingschema.org",
    v._label: "light",
    v. _resource:[
          {v._name: "light", 
           v._type:"light",
           "capabilities": [
                {
                    v._type:"onoff", 
                    v._name:"on", 
                    "actions":[
                        {v._name:"change", v._type:"change"}
                    ],
                    "properties": [
                        {v._name: "cst", v._type: "currentState"},
                        {v._name: "tst", v._type: "targetState"},
                        {v._name: "dt", v._type: "delayTime"}
                    ]

                }, 
                {
                    v._type:"colorhs", 
                    v._name:"chs",
                    "actions": [
                        {v._name:"change", v._type:"change"}
                    ]
                }, 
                {
                    v._type:"brightness", 
                    v._name:"brt",
                    "actions": [
                        {v._name:"change", v._type:"change"},
                        {v._name:"move", v._type:"move"}, 
                        {v._name:"step", v._type:"step"}
                    ],
                    "properties": [
                        {v._name: "cbr", v._type: "currentBrightness"},
                        {v._name: "tbr", v._type: "targetBrightness"},
                        {v._name: "mbr", v._type: "moveBrightness"},
                        {v._name: "sbr", v._type: "stepBrightness"},
                        {v._name: "tt", v._type: "transitionTime"}
                    ]
                }
            ]
        }      
    ]
}


def selfTest():
    print json.dumps(light, sort_keys=True, indent=2, separators=(',', ': '))
    
if __name__ == "__main__" :
    selfTest()
