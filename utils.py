import os


def project_dir_name():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    project_dir = os.path.abspath(current_dir + "/../") + "/"
    return project_dir


def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
