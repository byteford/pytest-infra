import boto3
class session:
    session = ""
    def get_session(self):
        return self.session
    def __init__(self):
        self.session = boto3.Session()