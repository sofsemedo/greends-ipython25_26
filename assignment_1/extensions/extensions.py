def get_media_type(filename):
    # corresponding filename extension (keys) to media type (values)
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Finds the last dot
    # Converts the filename to lowercase
    # Removes any blank spaces
    # If no dot is found then there is no extension
    # Splits filename from the last dothaaha until the end
    ext = '.' + filename.lower().strip().rsplit('.', 1)[-1] if '.' in filename else ''

    # Return the corresponding media type or default to application/octet-stream
    return media_types.get(ext, "application/octet-stream")

# Prompt the user for a filename
filename = input("Enter the name of the file: ")

# Fuction to display output to the console
# To informe the user about the media type associated with the file name
print(get_media_type(filename))



