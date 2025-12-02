This Repository contains Ansible task -
One Role ( Websvc ) which is for both Windows and Linux 

Handlers/main.yaml  ## contains handlers for both  Unix and Windows . 

Jinja2 Templates ## index.html.j2 applies for both Unix and Windows . 

Inventory structure ## For Linux ### we have used it under group_vars . localhost is used with ansible_connection=local because the Managed and Controller node are the same.
                   ## So we have used same server in  both [prod] and [dev] 
                   
                   ## For Windows ##  We have a separate windows server (13.236.135.217)



Commands to run the final playbook in Windows ##    ansible-playbook -i /home/ec2-user/nginx_inventory/inventory nginx_windows.yaml --ask-vault-password
Commands to run the final playbook in Linux ##      ansible-playbook -i inventory nginx_unix.yaml --ask-vault-pass -l dev


URLs to Verify Deployment :
Windows: http://13.236.135.217:8080/
Linux: http://3.107.237.126:8080/


                        
