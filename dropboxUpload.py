import dropbox

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def upload_file(self,fileFrom,fileTo):
        dpx=dropbox.Dropbox(self.accessToken) 
        f=open(fileFrom,"rb")
        dpx.files_upload(f.read(),fileTo)  
        
def main():
    accessToken="sP6CDzxN8NwAAAAAAAAAAclML8rkJ-KdfdsWydA1FyFg-kWcS_yiW2mzbyyLsZ3x"
    transferData=TransferData(accessToken)
    fileFrom="E:/Win10/Desktop/dpx/code.txt"
    fileTo="/Dpx1/code.txt"    
    transferData.upload_file(fileFrom, fileTo)
    print("File has been moved!")
main()