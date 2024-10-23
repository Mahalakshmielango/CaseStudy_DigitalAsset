class AssetNotFoundException(Exception):
    """
    Exception raised when an asset with a specified ID is not found in the database.
    """
    def __init__(self, message="Asset not found"):
        self.message = message
        super().__init__(self.message)

class AssetNotMaintainException(Exception):
    """
    Exception raised when an asset has not been maintained for over 2 years.
    """
    def __init__(self, message="Asset has not been maintained in the last 2 years"):
        self.message = message
        super().__init__(self.message)
