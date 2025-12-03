#!/usr/bin/python

## AnsibleModule is a fixed, built-in class provided by Ansible for writing custom modules.
from ansible.module_utils.basic import AnsibleModule

##creating a variable named module
##This variable will store an object (an instance) created from the class AnsibleModule.
def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            content=dict(type='str', required=True)
        )
    )
    
    file_path = f"/tmp/{module.params['name']}"

## using open() function to open a file 
## with : to automatically closes the file when done

    try:
        with open(file_path, "w") as file_handle:
            file_handle.write(module.params['content'])

        module.exit_json(
            changed=True,
            message=f"File created at {file_path}",
        )

    except Exception as error_message:
        module.fail_json(msg=f"Failed to create file: {error_message}")

run_module()

