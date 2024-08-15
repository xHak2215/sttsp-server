import paramiko
import os

kast ='>>'
client={}
sftp_client=''
        

file1 = open(f"{os.getcwd()}\\setings.conf", "r")
while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    pers, parametre = line.strip().split('-')
    client[pers] =parametre
# закрываем файл
file1.close
#except:
#    print('eror file 1') 
#    print('возможно в папке сервер оцуцтвует файл setings.conf')  
print(client)
#os.chdir('. . / ')
os.chdir('file')



def config():
    print(f'host ip: {client['host']}')
    print(f'port: {client['port']}')
    print(f'user name: {client['username']}')
    print(f'password: {client['password']}')
config()

 
def create_sftp_client(host, port, username, password):
    host=str(host)
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
 
    sftp_client = paramiko.SFTPClient.from_transport(transport)
 
    return sftp_client

def upload_file_to_server(sftp_client, local_file, remote_file):
    sftp_client.put(local_file, remote_file)
    
def download_file_from_server(sftp_client, remote_file, local_file):
    sftp_client.get(remote_file, local_file)

#sftp_client=create_sftp_client(client['host'],client['port'],client['username'],client['password'])
#print(sftp_client)

#ftp_client = create_sftp_client(client['host'],client['port'],client['username'],client['password'])
#upload_file_to_server(sftp_client, file_upload , "remote_file")

#ftp_client = create_sftp_client(client['host'],client['port'],client['username'],client['password'])
#download_file_from_server(sftp_client, "remote_file", file_download)

while True:
    server_command=input(f'sftp server{kast}')
    if server_command == 'exit':
        break
        exit()
    elif server_command =='config':
        config()
    elif server_command.startswith("upload"):
        file_upload = server_command.split("-f")[1]
        if sftp_client == 'NaN':
            print("\033[1;31;40m  error not client \n")
        ftp_client = create_sftp_client(client['host'],client['port'],client['username'],client['password'])
        upload_file_to_server(sftp_client, file_upload , "remote_file")
    elif server_command.startswith("clien"):
        try:
            key = server_command.split("-")[1]
        except IndexError:
            print('нeт оргументов, используйте -run , -close')
        if key =="run":
            sftp_client=create_sftp_client(str(client['host']),int(client['port']),str(client['username']),str(client['password']))
            print(sftp_client)
        elif key == 'close':
            try:
                sftp_client.close()
            except:
                print('error')    
    elif server_command.startswith("download"):
        file_download = server_command.split("-f")[1]
        if sftp_client == 'NaN':
            print("\033[1;31;40m  error not client \n")
        ftp_client = create_sftp_client(client['host'],client['port'],client['username'],client['password'])
        download_file_from_server(sftp_client, "remote_file", file_download)       
    elif server_command == 'help':
        print('clien , upload , download')