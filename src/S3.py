from random import random
from botocore import exceptions

class s3_obj:
    location = ""
    all_locations = []
    error = None
    log = ""

    def get_error(self):
        return self.error

    def set_location(self, location):
        self.location = location
        self.all_locations.append(location)

    def get_location(self):
        return self.location

    def cleanup_location(self):
        print("cleanup locations")
        self.all_locations = []
        self.location = ""
        pass
    
    def upload_file(self, s3_client):
        print("upload", self.location)
        try:
            self.log = s3_client.put_object(Body=b"test_file",Bucket=self.location,Key="test_file")
        except Exception as err:
            print ("error: ", err)
            self.error = err

        return self.location

    def delete_file(self):
        print("delete", self.location)


    def is_file_in_location(self, s3_client):
        try:
            s3_client.head_object(Bucket=self.location,Key="test_file")
        except exceptions.ClientError:
            return False
        return True

    def read_file(self):
        return dict()

