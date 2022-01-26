from distutils.log import error


class lambda_obj:
    name = ""
    error = None
    def run_lambda(self,name, s3_test_client):
        self.name = name
        try:
            responce = s3_test_client.invoke(FunctionName = name)
            payload = responce['Payload'].read()
            print(payload)
        except Exception as err:
            self.error = err

    def get_error(self):
        return self.error