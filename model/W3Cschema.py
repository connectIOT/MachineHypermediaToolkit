import terms as v
import json


BaseSchema = { 
    v._rdfResource: [
        { v._rdfProperty: v._mayHave,
         v._range : v._rdfClass,
         v._domain: v._rdfClass,
        v._description: """ classes that this class may have instances of or links to""",
        },
        { v._rdfProperty: v._usedBy,
         v._range : v._rdfClass,
         v._domain: v._rdfClass,
        v._description: """ a class that may have or links to an instance of this class """,
        },
        { v._rdfProperty: v._params,
         v._range : v._property,
         v._domain: [v._event, v._action, v._subscription, v._actuation, v._notification],
        v._description: """ a class that may have or links to an instance of this class """,
        },
    ]
}


W3Cschema = { 
    v._context: "http://thingschema.org",
    v._label: "W3Cschema",
    v._rdfResource: [
        {v._rdfClass: "WoTinteractionModel",
        v._subClassOf: "InteractionModel",
        v._usedBy: ["W3C_WoT_IG"],
        v._mayHave: [v._thing, v._event, v._action, v._property, 
                    v._capability, v._index, 
                    v._actuation, v._subscription, v._notification, 
                    v._value, v._params],
        v._description: """Base class for W3C Thing Model Interactions"""
        },
        {v._rdfClass: v._index,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._index, v._thing],
        v._mayHave: [v._thing, v._capability, v._index],
        v._description: """Index class"""
        },
        {v._rdfClass: v._capability,
        v._subClassOf: v._index,
        v._usedBy: [v._index, v._thing],
        v._mayHave: [v._event, v._action, v._property, v._capability],
        v._description: """Capability class"""
        },
        {v._rdfClass: v._thing,
        v._subClassOf: v._capability,
        v._usedBy: [v._index],
        v._mayHave: [v._event, v._action, v._property, v._capability, v._index],
        v._description: """Thing class"""
        },
        {v._rdfClass: v._event,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [v._subscription, v._notification, v._params],
        v._description: """Event class"""
        },
        {v._rdfClass: v._action,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [v._actuation, v._notification, v._params],
        v._description: """Action class"""
        },
        {v._rdfClass: v._property,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [v._value],
        v._description: """Property class"""
        },
        {v._rdfClass: v._subscription,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._event],
        v._mayHave: [v._notification, v._params],
        v._description: """Subscription class"""
        },
        {v._rdfClass: v._actuation,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._action],
        v._mayHave: [v._notification, v._params],
        v._description: """Actuation class"""
        },
        {v._rdfClass: v._notification,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._subscription, v._actuation],
        v._mayHave: [v._params],
        v._description: """Notification class"""
        }
    ]
}

def serialize():
    return json.dumps(W3Cschema)

if __name__ == "__main__" :
    print serialize()
