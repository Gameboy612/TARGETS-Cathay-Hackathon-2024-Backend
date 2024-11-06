import os
UPLOADS_FOLDER = "./uploads"
uuids = [file.rsplit(".", 1)[0] for file in os.listdir(UPLOADS_FOLDER)]
extensions = [file.rsplit(".", 1)[1] for file in os.listdir(UPLOADS_FOLDER)]

uuid = input("UUID: ").replace("../", "")
if uuid not in uuids:
    exit(1)

file_path = uuid + "." + extensions[uuids.index(uuid)]
print(os.path.exists(os.path.join(UPLOADS_FOLDER, file_path)))