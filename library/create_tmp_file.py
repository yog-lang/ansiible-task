#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            content=dict(type='str', required=True)
        )
    )

    file_path = f"/tmp/{module.params['name']}"

    try:
        with open(file_path, "w") as f:
            f.write(module.params['content'])

        module.exit_json(
            changed=True,
            message=f"File created at {file_path}",
        )

    except Exception as e:
        module.fail_json(msg=f"Failed to create file: {e}")

run_module()

