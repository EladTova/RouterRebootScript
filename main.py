import os
import time
import paramiko

# The following program implements a script to reboot a router
if __name__ == '__main__':

    # Getting router login credentials
    router_ip_address = input('Please enter router IP address: ')
    router_username = input('Please enter router username: ')
    router_password = input('Please enter password: ')

    # Opening SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connecting to desired router using username & password authentication
    ssh.connect(router_ip_address,
                username=router_username,
                password=router_password)

    print('Rebooting router...')

    # Rebooting the router
    stdin, stdout, stderr = ssh.exec_command('reboot')

    # Waiting for reboot process to be done
    time.sleep(15)

    # Checking if the router reboot is finished
    alive_counter = 0
    while alive_counter < 60:
        # Pinging the router to see if he is alive
        router_alive_check = os.system("ping -c 1 " + router_ip_address)

        if router_alive_check != 0:
            # At this point, the router is not up yet, so we will keep waiting
            alive_counter += 1
            time.sleep(1)
        else:
            print('Router is up')
            # Closing the connection
            ssh.close()
            break
