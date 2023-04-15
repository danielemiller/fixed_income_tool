import os

def latest_backup(backup_directory):
    backup_files = [
        f for f in os.listdir(backup_directory) if os.path.isfile(os.path.join(backup_directory, f))
    ]
    backup_files.sort(key=lambda x: os.path.getmtime(os.path.join(backup_directory, x)), reverse=True)
    return backup_files[0] if backup_files else None
