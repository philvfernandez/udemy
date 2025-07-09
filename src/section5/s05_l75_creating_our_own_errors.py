class RuntimeErrorWithCode(TypeError):
    """
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

# raise MyCustomError("I am a custom error", 500)

## Will print doc string given above
error = RuntimeErrorWithCode('An error happened', 500)
print(error.__doc__)
