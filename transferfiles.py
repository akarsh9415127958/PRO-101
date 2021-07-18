import dropbox
import os
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,folder_from,folder_to,local_path):
        
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(folder_from):
            relative_path = os.path.relpath(local_path,folder_from)
            dropbox_path = os.path.join(folder_to,relative_path)
        
        with open(folder_from, 'rb') as f:
            dbx.folder_upload(f.read(), folder_to) 
def main():
     access_token = 'oEUAXKdt22cAAAAAAAAAActCL8GmI3BdhZYLFzdsAdlYoUzSK_xaDhVcD6gX9zVa'
     transferData = TransferData(access_token)

     folder_from = input("Enter the folder path to be transfarred:-")
     folder_to = input("Enter the full folder path to upload:-")  # The full path to upload the file to, including the file name

    # API v2
     transferData.upload_file(folder_from, folder_to)
print("folder have been moved to cloud")

main()  
