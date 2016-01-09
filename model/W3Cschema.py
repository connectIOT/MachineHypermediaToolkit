import terms as v
import json

W3Cschema = { 
    v._context: "http://schema.org",
    v._schema: [
        {v._class: "WoTinteractionModel",
        v._subClassOf: "InteractionModel",
        v._usedBy: ["W3C_WoT_IG"],
        v._uses: [v._thing, v._event, v._action, v._property, 
                    v._capability, v._index, 
                    v._actuation, v._subscription, v._notification, 
                    v._value, v._params],
        v._description: """Base class for W3C Thing Model Interactions"""
        },
        {v._class: v._index,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._index, v._thing],
        v._uses: [v._thing, v._capability, v._index],
        v._description: """Index class"""
        },
        {v._class: v._capability,
        v._subClassOf: v._index,
        v._usedBy: [v._index, v._thing],
        v._uses: [v._event, v._action, v._property, v._capability],
        v._description: """Capability class"""
        },
        {v._class: v._thing,
        v._subClassOf: v._capability,
        v._usedBy: [v._index],
        v._uses: [v._event, v._action, v._property, v._capability, v._index],
        v._description: """Thing class"""
        },
        {v._class: v._event,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._uses: [v._subscription, v._notification, v._params],
        v._description: """Event class"""
        },
        {v._class: v._action,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._uses: [v._actuation, v._notification, v._params],
        v._description: """Action class"""
        },
        {v._class: v._property,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._thing, v._capability],
        v._uses: [v._value],
        v._description: """Property class"""
        },
        {v._class: v._subscription,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._event],
        v._uses: [v._notification, v._params],
        v._description: """Subscription class"""
        },
        {v._class: v._actuation,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._action],
        v._uses: [v._notification, v._params],
        v._description: """Actuation class"""
        },
        {v._class: v._notification,
        v._subClassOf: "WoTinteractionModel",
        v._usedBy: [v._subscription, v._actuation, v._params],
        v._uses: [],
        v._description: """Notification class"""
        }
    ]
}

def serialize():
    return json.dumps(W3Cschema)

if __name__ == "__main__" :
    print serialize()
