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
        }      
    ]
}


def selfTest():
    print json.dumps(light, sort_keys=False, indent=2, separators=(',', ': '))
    
if __name__ == "__main__" :
    selfTest()
