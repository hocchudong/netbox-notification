from utils import format_timestamp
from config import nb

# Created Event for device
def created_event(webhook_data):
    event = webhook_data.get("event", {})
    timestamp = webhook_data.get("timestamp", {})
    time = format_timestamp(timestamp)
    username = webhook_data.get("username", {})
    model = webhook_data.get("model", {})
    
    device_data = webhook_data.get("data", {})
    device_id = device_data.get("id", {})
    device_name = device_data.get("name", {})
    device_site = device_data.get("site", {}).get("name", {})
    device_rack = device_data.get("rack", {})
    if device_rack:
        device_rack_name = device_rack.get("name",{})
    else:
        device_rack_name = "Not in any rack"
    device_positon = device_data.get("position")
    device_tenant = device_data.get("tenant",{})
    device_serial = device_data.get("serial",{})
    if device_tenant:
        device_tenant_name = device_tenant.get("name")
    else:
        device_tenant_name = "No Tenant yet!"
    device_location = device_data.get("location")
    if device_location:
        device_location_name = device_location.get("name")
    else:
        device_location_name = "No Location!"
    device_info = nb.dcim.devices.get(id=device_id)

    device_role = device_info.role.name
    device_type = device_info.device_type.model
    device_des = device_data.get("description",{})
    device_comments = device_data.get("comments")
    custom_fields = device_data.get("custom_fields")
    device_owner = custom_fields.get("device_owner",{})
    contact = custom_fields.get("contact")
    if contact:
        contact_name = contact.get("name")
    else:
        contact_name = "No contact!"
    msg = (
        f"*Event: *{event} \n"
        f"*Object Type:* {model}\n"
        f"*Created by:* {username}\n"
        f"*At: *{time}UTC\n"
        f" \n"
        f"*Detail*\n"
        f"*Device Name:* {device_name}\n"
        f"*Device Role*: {device_role}\n"
        f"*Device Type*: {device_type}\n"
        f"*Device Serial:* {device_serial}\n"
        f"*Device Owner:* {device_owner}\n"
        f"*Tenant:* {device_tenant_name}\n"
        f"*Site:* {device_site}\n"
        f"*Location:* {device_location_name}\n"
        f"*Rack:* {device_rack_name}\n"
        f"*Position:* {device_positon}\n"
        f"*Contact:* {contact_name}\n"
        f"*Description:* {device_des}\n"
        f"*Comment:* {device_comments}\n"
    )
    return msg

# Config data to updated event
def prechange_config(prechange_data):
    description = prechange_data.get('description', {})
    comments = prechange_data.get('comments', {})
    site_id = prechange_data.get("site", {})
    site = nb.dcim.sites.get(site_id)
    site_name = site.name
    device_type_id = prechange_data.get('device_type', {})
    device_type = nb.dcim.device_types.get(device_type_id)
    device_type_name = device_type.model
    device_role_id = prechange_data.get('role', {})
    device_role_name = nb.dcim.device_roles.get(device_role_id)
    device_name = prechange_data.get("name", {})
    rack_id = prechange_data.get("rack", {})
    
    if not rack_id:
        rack_name = "Unknow rack"
        position = "Unknow position"
    else:
        rack = nb.dcim.racks.get(rack_id)
        rack_name = rack.name
        position = prechange_data.get("position")
    primary_ip4_id = prechange_data.get("primary_ip4")
    if not primary_ip4_id:
        primary_ip4_name = "No Ip yet!"
    else:
        primary_ip4 = nb.ipam.ip_addresses.get(primary_ip4_id)
        primary_ip4_name = primary_ip4.address
    customfields = prechange_data.get("custom_fields")
    contact_id = customfields.get("contact")
    if contact_id:
        contact = nb.tenancy.contacts.get(contact_id)
        contact_name = contact.name
    else:
        contact_name = "No contact!"
        
    data = {
        "Description": description,
        "Comments": comments,
        "Site": site_name,
        "Device Type": device_type_name,
        "Device Role": device_role_name,
        "Device Name": device_name,
        "Rack": rack_name,
        "Position": position,
        "Ipv4": primary_ip4_name,
        "Contact": contact_name
    }
    return data

def postchange_config(postchange_data):
    description = postchange_data.get('description', {})
    comments = postchange_data.get('comments', {})
    site_id = postchange_data.get("site", {})
    site = nb.dcim.sites.get(site_id)
    site_name = site.name
    device_type_id = postchange_data.get('device_type', {})
    device_type = nb.dcim.device_types.get(device_type_id)
    device_type_name = device_type.model
    device_role_id = postchange_data.get('role', {})
    device_role = nb.dcim.device_roles.get(device_role_id)
    device_role_name = device_role
    device_name = postchange_data.get("name", {})
    rack_id = postchange_data.get("rack", {})
    if not rack_id:
        rack_name = "Unknow rack"
        position = "Unknow position"
    else:
        rack = nb.dcim.racks.get(rack_id)
        rack_name = rack.name
        position = postchange_data.get("position")
    primary_ip4_id = postchange_data.get("primary_ip4")
    if not primary_ip4_id:
        primary_ip4_name = "No Ip yet!"
    else:
        primary_ip4 = nb.ipam.ip_addresses.get(primary_ip4_id)
        primary_ip4_name = primary_ip4.address
    customfields = postchange_data.get("custom_fields")
    contact_id = customfields.get("contact")
    if contact_id:
        contact = nb.tenancy.contacts.get(contact_id)
        contact_name = contact.name
    else:
        contact_name = "No contact!"
    data = {
        "Description": description,
        "Comments": comments,
        "Site": site_name,
        "Device Type": device_type_name,
        "Device Role": device_role_name,
        "Device Name": device_name,
        "Rack": rack_name,
        "Position": position,
        "Ipv4": primary_ip4_name,
        "Contact": contact_name
    }
    
    return data

def detail_config(prechange_data, postchange_data):
    msg = f"*Detail!* \n"
    pre_data = prechange_config(prechange_data)
    post_data = postchange_config(postchange_data)
    differences = {}
    all_keys = set(pre_data.keys()).union(post_data.keys())
    for key in all_keys:
        pre_value = pre_data.get(key)
        post_value = post_data.get(key)
        if pre_value != post_value:
            differences[key] = {"prechange": pre_value, "postchange": post_value}
    for key, diff in differences.items():
        msg += f"- *{key}*: Change from *{diff['prechange']}* to *{diff['postchange']}* \n"
    return msg   

# Updated Event for device
def updated_event(webhook_data):
    event = webhook_data.get("event", {})
    timestamp = webhook_data.get("timestamp", {})
    time = format_timestamp(timestamp)
    username = webhook_data.get("username", {})
    object = webhook_data.get("model", {})
    
    device_data = webhook_data.get("data", {})
    device_name = device_data.get("name", {})
    device_site = device_data.get("site", {}).get("name", {})
    device_rack = device_data.get("rack", {})
    if device_rack:
        device_rack_name = device_rack.get("name", {})
    else:
        device_rack_name = "Not in any Rack"
    device_positon = device_data.get("position")
    custom_fields = device_data.get("custom_fields",{})
    contact = custom_fields.get("contact",{})
    if contact:
        contact_name = contact.get("name",{})
    else:
        contact_name = "No contact yet!"
    snapshots = webhook_data.get("snapshots", {})
    prechange = snapshots.get("prechange", {})
    postchange = snapshots.get("postchange", {})
    detail = detail_config(prechange,postchange)
    
    msg = (
        f"*Event:* {event}\n"
        f"*Object Type:* {object}\n"
        f"*Object Name:* {device_name}\n"
        f"*Site:* {device_site}\n"
        f"*Rack:* {device_rack_name}\n"
        f"*Position:* {device_positon}\n"
        f"*Contact:* {contact_name} \n"
        f"*Edit By:* {username}\n"
        f"*Time:* {time}UTC\n"
        f" \n"
    )
    msg += detail
    return msg

# Deleted Event for device
def deleted_event(webhook_data):
    event = webhook_data.get("event", {})
    timestamp = webhook_data.get("timestamp", {})
    time = format_timestamp(timestamp)
    username = webhook_data.get("username", {})
    object = webhook_data.get("model", {})

    device_data = webhook_data.get("data", {})
    device_name = device_data.get("name", {})
    device_site = device_data.get("site", {}).get("name", {})
    device_rack = device_data.get("rack", {})
    if device_rack:
        device_rack_new = device_rack.get("name",{})
    else:
        device_rack_new = "Not in any rack"
    device_positon = device_data.get("position")
    
    msg = (
        f"*Event:* {event}\n"
        f"*Object Type:* {object}\n"
        f"*Object Name:* {device_name}\n"
        f"*Site:* {device_site}\n"
        f"*Rack:* {device_rack_new}\n"
        f"*Position:* {device_positon}\n"
        f"*Removed By:* {username}\n"
        f"*Time:* {time}\n"
    )
    return msg

