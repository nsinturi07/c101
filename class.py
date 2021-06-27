import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token
    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open (file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
        access_token='0pZ9UknxcZQAAAAAAAAAAQ9XEgihTRYXcyeiKAxrdlnY-RUZLxhCxC2UKuStrpLg'
        transferdata=TransferData(access_token)
        file_from= input("enter file path")
        file_to= input("enter file destination")
        transferdata.upload_file(file_from, file_to)
        print("file uploaded")
main()