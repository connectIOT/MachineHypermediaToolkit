import terms as v

W3Cmodel =      [
                 {v._className: "WoTinteractionModel",
                  v._subClassOf: "InteractionModel",
                  v._domain: ["W3C_WoT_IG"],
                  v._range: [v._thing, v._event, v._action, v._property, 
                             v._capability, v._index, 
                             v._actuation, v._subscription, v._notification, 
                             v._value, v._params],
                  v._description: """Base class for W3C Thing Model Interactions"""
                  },
                 {v._className: v._index,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._index, v._thing],
                  v._range: [v._thing, v._capability, v._index],
                  v._description: """Index class"""
                  },
                 {v._className: v._capability,
                  v._subClassOf: v._index,
                  v._domain: [v._index, v._thing],
                  v._range: [v._event, v._action, v._property, v._capability],
                  v._description: """Capability class"""
                  },
                 {v._className: v._thing,
                  v._subClassOf: v._capability,
                  v._domain: [v._index],
                  v._range: [v._event, v._action, v._property, v._capability, v._index],
                  v._description: """Thing class"""
                  },
                 {v._className: v._event,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._thing, v._capability],
                  v._range: [v._subscription, v._notification, v._params],
                  v._description: """Event class"""
                  },
                 {v._className: v._action,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._thing, v._capability],
                  v._range: [v._actuation, v._notification, v._params],
                  v._description: """Action class"""
                  },
                 {v._className: v._property,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._thing, v._capability],
                  v._range: [v._value],
                  v._description: """Property class"""
                  },
                 {v._className: v._subscription,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._event],
                  v._range: [v._notification, v._params],
                  v._description: """Subscription class"""
                  },
                 {v._className: v._actuation,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._capability],
                  v._range: [v._notification, v._params],
                  v._description: """Actuation class"""
                  },
                 {v._className: v._notification,
                  v._subClassOf: "WoTinteractionModel",
                  v._domain: [v._subscription, v._actuation, v._params],
                  v._range: [],
                  v._description: """Notification class"""
                  }
                ]
