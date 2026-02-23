class ResponseHandler:
    def process(self, response: str) -> str:
        if not response:
            return "⚠️ No response generated."

        return response.strip()