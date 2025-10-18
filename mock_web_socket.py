class MockWebSocket:
    def __init__(self):
        self.accepted: bool = False
        self.sent_messages: list = []
    
    async def accept(self):
        self.accepted = True

    
    async def send_text(self, message: str):
        self.sent_messages.append(message)