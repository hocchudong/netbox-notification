from utils import format_timestamp
from config import nb

# Created Event for VM
def created_event_vm(webhook_data):
    event = webhook_data.get("event", {})
    timestamp = webhook_data.get("timestamp", {})
    time = format_timestamp(timestamp)
    username = webhook_data.get("username", {})
    model = webhook_data.get("model", {})
    
    vm_data = webhook_data.get("data", {})
    vm_name = vm_data.get("name",{})
    vm_site = vm_data.get("site", {})
    if vm_site:
        vm_site_name = vm_site.get("name",{})
    else:
        vm_site_name = "Not in any Site!"
    vm_cluster = vm_data.get("cluster",{})
    if vm_cluster:
        vm_cluster_name = vm_cluster.get("name",{})
    else:
        vm_cluster_name = "Not in any cluster!"
    vm_device = vm_data.get("device",{})
    if vm_device:
        vm_device_name = vm_device.get("name",{})
    else:
        vm_device_name = "Not assign on any Device!"
    vm_tenant = vm_data.get("tenant",{})
    if vm_tenant:
        vm_tenant_name = vm_tenant.get("name",{})
    else:
        vm_tenant_name = "Not belong to any Tenant!"
    vm_ip = vm_data.get("primary_ip4",{})
    if vm_ip:
        vm_ip_addr = vm_ip.get("address",{})
    else:
        vm_ip_addr = "Not have IP!!"
    vm_os = vm_data.get("platform",{})
    if vm_os:
        vm_os_name = vm_os.get("name",{})
    else:
        vm_os_name = "No OS yet!"
    vm_cpu = vm_data.get("vcpus",{})
    vm_ram = vm_data.get("memory",{})
    vm_disk = vm_data.get("disk",{})
    vm_des = vm_data.get("description",{})
    vm_com = vm_data.get("comments")
    msg = (
        f"*Event: *{event} \n"
        f"*Object Type:* {model}\n"
        f"*Created by:* {username}\n"
        f"*At: *{time}UTC\n"
        f" \n"
        f"*Detail*\n"
        f"*VM Name:* {vm_name}\n"
        f"*VM IP:* {vm_ip_addr}\n"
        f"*VM OS:* {vm_os_name}\n"
        f"*VM Size:* CPU-{vm_cpu}/RAM-{vm_ram}/DISK-{vm_disk} \n"
        f"*VM Description:* {vm_des}\n"
        f"*VM Comments:* {vm_com}\n"
        f"*VM Site:* {vm_site_name}\n"
        f"*VM Cluster:* {vm_cluster_name}\n"
        f"*VM Device:* {vm_device_name}\n"
        f"*VM Tenant:* {vm_tenant_name}\n"
    )
    return msg
# Config data for Updated Event
def prechange_config(prechange_data):
    site_id = prechange_data.get("site", {})
    if site_id:
        site = nb.dcim.sites.get(site_id)
        site_name = site.name
    else:
        site_name = "No site yet!"
    primary_ip4_id = prechange_data.get("primary_ip4")
    if not primary_ip4_id:
        primary_ip4_name = "No Ip yet!"
    else:
        primary_ip4 = nb.ipam.ip_addresses.get(primary_ip4_id)
        primary_ip4_name = primary_ip4.address
    vm_name = prechange_data.get("name",{})
    vm_cluster_id = prechange_data.get("cluster",{})
    if vm_cluster_id:
        vm_cluster = nb.virtualization.clusters.get(vm_cluster_id)
        vm_cluster_name = vm_cluster.name
    else:
        vm_cluster_name = "No cluster"
    vm_device_id = prechange_data.get("device",{})
    if vm_device_id:
        vm_device = nb.dcim.devices.get(vm_device_id)
        vm_device_name = vm_device.name
    else:
        vm_device_name = "No device"
    vm_platform_id = prechange_data.get("platform",{})
    if vm_platform_id:
        vm_platform = nb.dcim.platforms.get(vm_platform_id)
        vm_platform_name = vm_platform.name
    else:
        vm_platform_name = "No Platform"
    vm_cpu = prechange_data.get("vcpus",{})
    vm_memory = prechange_data.get("memory",{})
    vm_disk = prechange_data.get("disk",{})
    vm_des = prechange_data.get("description",{})
    vm_comments = prechange_data.get("comments",{})
    data = {
        "Site": site_name,
        "VM Name": vm_name,
        "VM Ip": primary_ip4_name,
        "Platform": vm_platform_name,
        "VM Device": vm_device_name,
        "VM Cluster": vm_cluster_name,
        "VM CPU": vm_cpu,
        "VM Memory": vm_memory,
        "VM Disk": vm_disk,
        "Comments": vm_comments,
        "Description": vm_des
    }
    return data
def postchange_config(postchange_data):
    site_id = postchange_data.get("site", {})
    if site_id:
        site = nb.dcim.sites.get(site_id)
        site_name = site.name
    else:
        site_name = "No site yet!"
    primary_ip4_id = postchange_data.get("primary_ip4")
    if not primary_ip4_id:
        primary_ip4_name = "No Ip yet!"
    else:
        primary_ip4 = nb.ipam.ip_addresses.get(primary_ip4_id)
        primary_ip4_name = primary_ip4.address
    vm_name = postchange_data.get("name",{})
    vm_cluster_id = postchange_data.get("cluster",{})
    if vm_cluster_id:
        vm_cluster = nb.virtualization.clusters.get(vm_cluster_id)
        vm_cluster_name = vm_cluster.name
    else:
        vm_cluster_name = "No cluster"
    vm_device_id = postchange_data.get("device",{})
    if vm_device_id:
        vm_device = nb.dcim.devices.get(vm_device_id)
        vm_device_name = vm_device.name
    else:
        vm_device_name = "No device"
    vm_platform_id = postchange_data.get("platform",{})
    if vm_platform_id:
        vm_platform = nb.dcim.platforms.get(vm_platform_id)
        vm_platform_name = vm_platform.name
    else:
        vm_platform_name = "No Platform"
    vm_cpu = postchange_data.get("vcpus",{})
    vm_memory = postchange_data.get("memory",{})
    vm_disk = postchange_data.get("disk",{})
    vm_des = postchange_data.get("description",{})
    vm_comments = postchange_data.get("comments",{})
    data = {
        "Site": site_name,
        "VM Name": vm_name,
        "VM Ip": primary_ip4_name,
        "Platform": vm_platform_name,
        "VM Device": vm_device_name,
        "VM Cluster": vm_cluster_name,
        "VM CPU": vm_cpu,
        "VM Memory": vm_memory,
        "VM Disk": vm_disk,
        "Comments": vm_comments,
        "Description": vm_des
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
# Updated Event for VM
def updated_event_vm(webhook_data):
    event = webhook_data.get("event", {})
    timestamp = webhook_data.get("timestamp", {})
    time = format_timestamp(timestamp)
    username = webhook_data.get("username", {})
    object = webhook_data.get("model", {})
    
    vm_data = webhook_data.get("data", {})
    vm_name = vm_data.get("name", {})
    vm_site = vm_data.get("site", {})
    if vm_site:
        vm_site_name = vm_site.get("name")
    else:
        vm_site_name = "No site yet!"
    vm_ip = vm_data.get("primary_ip4",{})
    if vm_ip:
        vm_ip_addr = vm_ip.get("address",{})
    else:
        vm_ip_addr = "No IP yet!"
    snapshots = webhook_data.get("snapshots", {})
    prechange = snapshots.get("prechange", {})
    postchange = snapshots.get("postchange", {})
    detail = detail_config(prechange,postchange)
    
    msg = (
        f"*Event:* {event}\n"
        f"*Object Type:* {object}\n"
        f"*Object Name:* {vm_name}\n"
        f"*Object IP:* {vm_ip_addr}\n"
        f"*Site:* {vm_site_name}\n"
        f"*Edit By:* {username}\n"
        f"*Time:* {time}UTC\n"
        f" \n"
    )
    msg += detail
    return msg
# Deleted Event for VM
def deleted_event_vm(webhook_data):
    event = webhook_data.get("event", {})
    timestamp = webhook_data.get("timestamp", {})
    time = format_timestamp(timestamp)
    username = webhook_data.get("username", {})
    object = webhook_data.get("model", {})

    vm_data = webhook_data.get("data", {})
    vm_name = vm_data.get("name", {})
    vm_site = vm_data.get("site", {})
    if vm_site:
        vm_site_name = vm_site.get("name",{})
    else:
        vm_site_name = "Not in any Site!"
    vm_cluster = vm_data.get("cluster",{})
    if vm_cluster:
        vm_cluster_name = vm_cluster.get("name",{})
    else:
        vm_cluster_name = "Not in any cluster!"
    vm_ip = vm_data.get("primary_ip4",{})
    if vm_ip:
        vm_ip_addr = vm_ip.get("address",{})
    else:
        vm_ip_addr = "Not have IP!!"
    msg = (
        f"*Event:* {event}\n"
        f"*Object Type:* {object}\n"
        f"*Object Name:* {vm_name}\n"
        f"*Object IP:* {vm_ip_addr}\n"
        f"*Site:* {vm_site_name}\n"
        f"*Cluster:* {vm_cluster_name}\n"
        f"*Removed By:* {username}\n"
        f"*Time:* {time}\n"
    )
    return msg
