class ConversationMemory:
    def __init__(self, max_turns: int = 5):
        self.history = []
        self.max_turns = max_turns

    def update(self, user_input: str, assistant_response: str):
        self.history.append(
            f"User: {user_input}\nAdvisor: {assistant_response}"
        )
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    def get_context(self) -> str:
        return "\n".join(self.history)