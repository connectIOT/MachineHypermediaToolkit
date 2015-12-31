""" ApplicationModel is derived from ResourceModel class and adds the ability
    for an application to use an instance of the model as a discovery template,
    passing it to a discovery handler that creates queries on indices and 
    catalogs to identify resources that match those specified in the template.
"""
from ResourceModel import ResourceModel

class ApplicationModel(ResourceModel):
    pass