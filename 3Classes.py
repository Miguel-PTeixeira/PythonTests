# abstract_pipeline.py

import copy

class DataSource:
    """Represents a source that provides raw data."""
    def __init__(self, data):
        self.data = data

    def fetch(self):
        # Imagine this being replaced by a DB read or API call
        return self.data

def Change_Data(data,idx,value):
    data[idx]=value
    return data

# Example usage
if __name__ == "__main__":
    data = ["cat", "elephant", "sun", "galaxy", "cup"]

    source = DataSource(data)

    output = Change_Data(copy.copy(source.data),0,"changed")
    print("\nOriginal Data Source:")
    print(source.data)
    print("\nProcessed Output:")
    print(output)
