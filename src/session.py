import boto3
class session:
    session = ""
    def get_session(self):
        return self.session
    def create_session(self, profile_name="Default"):
        self.session = boto3.Session(profile_name=profile_name)