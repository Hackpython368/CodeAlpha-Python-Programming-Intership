import os 


def organize_file(path):
    files = os.listdir(f"{path}")

    for file in files:

        source , extension = os.path.splitext(file)
        if not os.path.exists(f"{path}\\{extension[1:]}"):
            os.mkdir(f"{path}\\{extension[1:]}")
        os.rename(f"{path}\\{file}",f"{path}\\{extension[1:]}\\{file}")
