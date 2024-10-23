import unittest
from dao.asset_management_service_impl import AssetManagementServiceImpl
from entity.models import Asset, Employee
from exceptions.asset_exceptions import AssetNotFoundException, AssetNotMaintainException

class TestAssetManagement(unittest.TestCase):
    def setUp(self):
        self.service = AssetManagementServiceImpl()

    def test_add_asset(self):
        asset = Asset(110, "Laptop", "Electronics", "SNO10", "2023-01-01", "madurai", "in use", 1)
        result = self.service.add_asset(asset)
        self.assertTrue(result, "Failed to add asset")

    def test_update_asset(self):
        asset = Asset(110, "Laptop Pro", "Electronics", "SNO8", "2023-01-01", "New York", "in use", 1)
        result = self.service.update_asset(asset)
        self.assertTrue(result, "Failed to update asset")

    def test_delete_asset(self):
        asset_id=108
        result = self.service.delete_asset(asset_id)
        self.assertTrue(result, "Failed to delete asset")

    def test_allocate_asset(self):
        result = self.service.allocate_asset(310, 110, 1, "2024-01-01","2024-02-02")
        self.assertTrue(result, "Failed to allocate asset")

    def test_deallocate_asset(self):
        result = self.service.deallocate_asset(308, 1, "2024-06-01")
        self.assertTrue(result, "Failed to deallocate asset")

    def test_perform_maintenance(self):
        result = self.service.perform_maintenance(208, 109, "2024-01-01")
        self.assertTrue(result, "Failed to perform maintenance")

    def test_reserve_asset(self):
        result = self.service.reserve_asset(407, 107,2, "2024-01-01", "2024-01-02", "2024-01-10","pending")
        self.assertTrue(result, "Failed to reserve asset")

    def test_withdraw_reservation(self):
        result = self.service.withdraw_reservation(407)
        self.assertTrue(result, "Failed to withdraw reservation")

    def test_invalid_asset_id_exception(self):
        # Using an invalid asset ID that doesn't exist
        invalid_asset_id = 999  # Ensure this ID doesn't exist

        self.service.delete_asset(invalid_asset_id)

    def test_asset_not_maintained_exception(self):
        # Ensure the asset has not been maintained for more than 2 years
        maintenance_id = 206
        asset_id = 107  # Assuming the employee ID is valid
        maintenance_date = "2026-01-01"  # A future date, simulating overdue maintenance

        self.service.perform_maintenance(maintenance_id, asset_id, maintenance_date)



if __name__ == "__main__":
    unittest.main()
