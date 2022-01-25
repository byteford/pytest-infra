

from random import random


class s3_obj:
    location = ""
    all_locations = []
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
    
    def upload_file(self):
        print("upload", self.location)
        return self.location

    def delete_file(self):
        print("delete", self.location)


    def is_file_in_location(self):
        return random() > 0.5

    def read_file(self):
        return dict()

