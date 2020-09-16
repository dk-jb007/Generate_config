import json
import os
import jinja2

template_file = "switch_with_vlans.j2"
json_file = "/home/ram/Documents/python3-hardway/parameters.json"
output_dir = "/home/ram/Documents/python3-hardway/_output"

print("Loading json file contents to list....!")
f = open(json_file)
parameters_list = json.load(f)

print("Creating jinja2 environment....!")

env = jinja2.Environment(loader = jinja2.FileSystemLoader(searchpath = "/home/ram/Documents/python3-hardway/"),trim_blocks = True,lstrip_blocks = True)
template = env.get_template(template_file)

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

print("Creating template...!")

for parameter in parameters_list:
    result = template.render(parameter)
    f= open(os.path.join(output_dir,parameter['hostname']+"_config_with_vlans.config"),"w")
    f.write(result)
    f.close()
    print("Configuration %s created...!"%(parameter['hostname']+"_config_with_vlans.config"))
print("Nicely Done...!!")
