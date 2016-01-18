import json
import terms as v

light = {
    v._context : "http://thingschema.org",
    v._label: "light",
    v. _resource:[
          {v._name: "light", 
           v._type:"light",
           "capabilities": [
                {v._type:"onoff", v._name:"onoff", 
                    "actions":[{v._name:"change", v._type:"change"}]
                }, 
                {v._type:"colorhs", v._name:"colorhs",
                    "actions": [{v._name:"change", v._type:"change"}]
                }, 
                {v._type:"brightness", v._name:"brightness",
                    "actions": [
                        {v._name:"change", v._type:"change"},
                        {v._name:"move", v._type:"move"}, 
                        {v._name:"step", v._type:"step"}
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
