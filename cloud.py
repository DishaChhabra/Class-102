import dropbox
src = input('enter source file : ')
dest = input('enter destination file: ')

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def upload(self, src, dest):
        dbx = dropbox.Dropbox(self.accessToken)
        #r=read b=binary
        with open(src,'rb') as file:
            dbx.files_upload(file.read(),dest)

new = TransferData('sl.BD4Ux064yBwWbWnfizRBOQteR2Rn5DXDCDW2p0w68uDrb6VeuyO57svWfYeJ8ScYqcZSqgHHazaws_KjikBgTaaI-rr43inq7P33KkxbrFgq6lLzycRxEOxW7084bU4ZyvezUkQ')
new.upload(src, dest)
print('data has been transferred')