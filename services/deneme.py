# import paramiko
# IP = "ip adresi"
# USERNAME = "kullanıcı adı"
# PASSWORD = "şifre"
# PORT = 22
# COMMAND = "komut"
# ssh = paramiko.SSHClient()  # SSH nesnesi oluşturma
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(ip, username, password) # SSH bağlantısını kurma
# stdin, stdout, stderr = ssh.exec_command(command) # Komut çalıştırma
# print(stdout.read())
# ssh.close()