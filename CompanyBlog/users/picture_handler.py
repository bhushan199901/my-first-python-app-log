import os
from PIL import Image
from flask import url_for, current_app


def add_profilepic(pic_upload, username):

    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username)+'.'+ext_type

    filepath = os.path.join(current_app.root_path,'static/profile_pics', storage_filename)

    output_size = (130, 130)

    picture = Image.open(pic_upload)
    picture.thumbnail(output_size)

    return storage_filename

