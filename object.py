from triones.Objects import TriObject, sales_contacts

#from triones.Tenant import TenantManager

from triones.ACL import TokenManager

from triones import Console

token_path = ""


dev_token = TokenManager(token_path)

def CreateLeads():
    meta_of_leads = {
            "name" : "string",
            "information" : "string",
            "value" : "integer"
            }
    leads_obj = TriObject("Leads", prefix = "")
    leads_obj.add_fields(meta_of_leads)
    # by now, add 3 fields

    leads_obj.fields["value"].add_relation(sales_contacts.fields["value"], category="lookup")

    return leads_obj

console = Console(dev_token)

tenant = console.get_tenant("example_company")

leads_obj = CreateLeads()
tenant.add_object(leads_obj)

console.deploy(after_time="now")
