import MachineHypermediaToolkit.terms as v
import json


BaseSchema = { 
    v._resource: [
        { v._property: v._mayHave,
         v._range : v._class,
         v._domain: v._class,
        v._description: """ classes that this class may have instances of or links to""",
        },
        { v._property: v._usedBy,
         v._range : v._class,
         v._domain: v._class,
        v._description: """ a class that may have or links to an instance of this class """,
        },
        { v._property: v._params,
         v._range : v._property,
         v._domain: [v._event, v._action, v._subscription, v._actuation, v._notification],
        v._description: """ a class that may have or links to an instance of this class """,
        },
    ]
}


WoTschema = { 
    v._context: "http://thingschema.org",
    v._label: "WoTschema",
    v._resource: [
        {v._class: "WoTinteractionModel",
        v._subClassOf: "InteractionModel",
        v._usedBy: ["WoT"],
        v._mayHave: [v._thing, v._event, v._action, v._property, 
                    v._capability, v._index, 
                    v._actuation, v._subscription, v._notification, 
                    v._value, v._params],
        v._description: """Base class for WoT Thing Model Interactions"""
        },
        {v._class: v._index,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._index, v._thing],
        v._mayHave: [v._thing, v._capability, v._index],
        v._description: """Index class"""
        },
        {v._class: v._capability,
        v._subClassOf: v._index,
        v._usedBy: [v._index, v._thing],
        v._mayHave: [v._event, v._action, v._property, v._capability],
        v._description: """Capability class"""
        },
        {v._class: v._thing,
        v._subClassOf: v._capability,
        v._usedBy: [v._index],
        v._mayHave: [v._event, v._action, v._property, v._capability, v._index],
        v._description: """Thing class"""
        },
        {v._class: v._event,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [v._subscription, v._notification, v._params],
        v._description: """Event class"""
        },
        {v._class: v._action,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [v._actuation, v._notification, v._params],
        v._description: """Action class"""
        },
        {v._class: v._property,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._mayHave: [v._value],
        v._description: """Property class"""
        },
        {v._class: v._subscription,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._event],
        v._mayHave: [v._notification, v._params],
        v._description: """Subscription class"""
        },
        {v._class: v._actuation,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._action],
        v._mayHave: [v._notification, v._params],
        v._description: """Actuation class"""
        },
        {v._class: v._notification,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._subscription, v._actuation],
        v._mayHave: [v._params],
        v._description: """Notification class"""
        }
    ]
}

def serialize():
    return json.dumps(WoTschema, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == "__main__" :
    print serialize()
