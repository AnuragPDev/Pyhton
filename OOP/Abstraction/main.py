# abstraction

# reduce complexity by hiding unnecessary details
class EmailService:

    def _connect(self):
        print("connecting to email server")

    def _authentication(self):
        print("Authenticating")

    def send_email():
        