from config.settings import DBBACKUP_STORAGE_OPTIONS
from data_storage.db.utils import latest_backup

def test_backup_creation(backup_manager, data_manager):
    data_manager.backup()
    backup_file = latest_backup(DBBACKUP_STORAGE_OPTIONS['location'])
    assert backup_file is not None

def test_recovery_process(backup_manager, data_manager):
    data_manager.backup()
    backup_file = latest_backup(DBBACKUP_STORAGE_OPTIONS['location'])
    data_manager.restore(backup_file)
    # Here, you can write assertions to check if your data has been restored correctly.
    # You might need to create and store some test data before running the backup and restore commands to verify the restoration.
