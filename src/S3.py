from random import random
from botocore import exceptions

class s3_obj:
    location = []
    all_locations = []
    error = None
    log = ""

    def get_error(self):
        return self.error

    def set_location(self, location):
        split_loc = location.split("/",1)
        self.location = {"bucket": split_loc[0], "key": split_loc[1]}
        self.all_locations.append(self.location)

    def get_location(self):
        return self.location

    def cleanup_location(self, s3_client):
        print("cleanup locations")
        print(self.all_locations)
        for loc in self.all_locations:
            self.delete_file(s3_client,loc["bucket"], loc["key"])
        self.all_locations = []
        self.location = ""
        pass
    
    def upload_file(self, s3_client):
        print("upload", self.location)
        try:
            self.log = s3_client.put_object(Body=b"test_file",Bucket=self.location["bucket"],Key=self.location["key"])
        except Exception as err:
            print ("error: ", err)
            self.error = err

        return self.location

    def delete_file(self,s3_client, bucket, key):
        print("delete: ", bucket, "/", key)
        s3_client.delete_object(Bucket= bucket, Key = key)


    def is_file_in_location(self, s3_client):
        try:
            s3_client.head_object(Bucket=self.location["bucket"],Key=self.location["key"])
        except exceptions.ClientError:
            return False
        return True

    def read_file(self, s3_client):
        try:
            obj = s3_client.get_object(Bucket=self.location["bucket"],Key=self.location["key"])
            obj["Body"].read()
        except Exception as err:
            print ("error: ", err)
            self.error = err

