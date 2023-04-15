import pytest
from datetime import datetime, timedelta

def test_backup_creation(backup_manager, data_manager):
    backup_manager.trigger_backup()
    backup_file = backup_manager.get_latest_backup()
    assert backup_file is not None
    assert backup_manager.is_backup_metadata_valid(backup_file)

def test_backup_data_integrity(backup_manager, data_manager):
    sample_data = data_manager.create_sample_data()
    backup_manager.trigger_backup()
    backup_data = backup_manager.get_latest_backup_data()
    assert sample_data == backup_data

def test_backup_frequency(backup_manager):
    initial_backup_count = backup_manager.get_backup_count()
    backup_manager.wait_for_scheduled_backup()
    new_backup_count = backup_manager.get_backup_count()
    assert new_backup_count == initial_backup_count + 1

def test_recovery_process(backup_manager, data_manager):
    sample_data = data_manager.create_sample_data()
    backup_manager.trigger_backup()
    data_manager.delete_data(sample_data)
    backup_manager.trigger_recovery()
    recovered_data = data_manager.get_data()
    assert recovered_data == sample_data

def test_recovery_fallback(backup_manager, data_manager):
    sample_data_A = data_manager.create_sample_data()
    backup_manager.trigger_backup()
    sample_data_B = data_manager.create_sample_data()
    backup_manager.trigger_backup()
    backup_manager.corrupt_latest_backup()
    backup_manager.trigger_recovery()
    recovered_data = data_manager.get_data()
    assert recovered_data == sample_data_A

def test_backup_retention(backup_manager, data_manager):
    retention_period = backup_manager.get_retention_period()
    old_backup = datetime.now() - timedelta(days=retention_period + 1)
    new_backup = datetime.now() - timedelta(days=retention_period - 1)
    
    backup_manager.create_backup_with_timestamp(old_backup)
    backup_manager.create_backup_with_timestamp(new_backup)
    backup_manager.enforce_retention_policy()
    
    backups = backup_manager.get_all_backups()
    assert old_backup not in backups
    assert new_backup in backups
