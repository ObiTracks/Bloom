def user_upload_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>

    return 'user_files/user_' + '{}/{}'.format(instance.user.id, filename)
   