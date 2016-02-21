from ferris import Controller


class Products(Controller):

    def list(self):
        self.response.content_type = 'application/json'

