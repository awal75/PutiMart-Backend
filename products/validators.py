from django.core.exceptions import ValidationError

def max_file_size(file):
    max_size=10  #mb
    max_size_in_bytes=max_size*1024*1024
    if file.size >max_size_in_bytes:
        raise ValidationError('The file size can not be gater {max_size}Mb')