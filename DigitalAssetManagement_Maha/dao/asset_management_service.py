from abc import ABC, abstractmethod


class AssetManagementService(ABC):
    """
    Abstract base class for Asset Management Service, defines the methods
    to be implemented for managing assets.
    """

    @abstractmethod
    def add_asset(self, asset):

        pass

    @abstractmethod
    def update_asset(self, asset):

        pass

    @abstractmethod
    def delete_asset(self, asset_id):
        pass

    @abstractmethod
    def allocate_asset(self, allocation_id,asset_id, employee_id, allocation_date,return_date):

        pass

    @abstractmethod
    def deallocate_asset(self, asset_id, employee_id, return_date):

        pass

    @abstractmethod
    def perform_maintenance(self, maintenance_id, asset_id, maintenance_date, description, cost):

        pass

    @abstractmethod
    def reserve_asset(self, reservation_id, asset_id, employee_id, reservation_date, start_date, end_date,status):

        pass

    @abstractmethod
    def withdraw_reservation(self, reservation_id):

        pass
