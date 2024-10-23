from dao.asset_management_service import AssetManagementService
from util.db_connection import DBConnection
from exceptions.asset_exceptions import AssetNotFoundException, AssetNotMaintainException
from datetime import datetime
import pyodbc


class AssetManagementServiceImpl(AssetManagementService):
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def add_asset(self, asset):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO assets (asset_id, aname, atype, s_no, purchase_date, loc, astatus, owner_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        try:
            cursor.execute(query, asset.asset_id, asset.name, asset.type, asset.serial_number,
                           asset.purchase_date, asset.location, asset.status, asset.owner_id)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error adding asset: {e}")
            return False

    def update_asset(self, asset):
        cursor = self.connection.cursor()
        query = """
        UPDATE assets
        SET aname = ?, atype = ?, s_no = ?, purchase_date = ?, loc = ?, astatus = ?, owner_id = ?
        WHERE asset_id = ?
        """
        try:
            cursor.execute(query, asset.name, asset.type, asset.serial_number,
                           asset.purchase_date, asset.location, asset.status,
                           asset.owner_id, asset.asset_id)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating asset: {e}")
            return False

    def delete_asset(self, asset_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM assets WHERE asset_id = ?"
        try:
            cursor.execute(query, asset_id)
            if cursor.rowcount == 0:
                raise AssetNotFoundException(f"Asset with ID {asset_id} not found.")
            self.connection.commit()
            return True
        except AssetNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print(f"Error deleting asset: {e}")
            return False

    def allocate_asset(self, allocation_id, asset_id, employee_id, allocation_date,return_date):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO asset_allocation (allocation_id,asset_id, employee_id, allocation_date,return_date)
        VALUES (?, ?, ? ,? ,?)
        """
        try:
            cursor.execute(query, allocation_id,asset_id, employee_id, allocation_date, return_date)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error allocating asset: {e}")
            return False

    def deallocate_asset(self, asset_id, employee_id, return_date):
        cursor = self.connection.cursor()
        query = """
        UPDATE asset_allocation
        SET return_date = ?
        WHERE asset_id = ? AND employee_id = ?
        """
        try:
            cursor.execute(query, return_date, asset_id, employee_id)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error deallocating asset: {e}")
            return False

    def perform_maintenance(self, maintenance_id, asset_id, maintenance_date):
        cursor = self.connection.cursor()

        maintenance_date_obj = datetime.strptime(maintenance_date, '%Y-%m-%d').date()
        try:
            # Query to get the last maintenance date
            last_maintenance_query = """
                SELECT MAX(maintenance_date)
                FROM maintenance
                WHERE asset_id = ?
                """
            cursor.execute(last_maintenance_query, asset_id)
            last_maintenance = cursor.fetchone()[0]

            if last_maintenance is not None:
                # Convert the last_maintenance to a datetime.date object if it's not already
                if isinstance(last_maintenance, datetime):
                    last_maintenance = last_maintenance.date()
                """last_maintenance_obj = last_maintenance if isinstance(last_maintenance,
                                                                      datetime) else last_maintenance.date()"""

                days_since_last_maintenance = (maintenance_date_obj - last_maintenance).days
                # Check if the last maintenance was more than 2 years ago (730 days)
                if days_since_last_maintenance > 730:
                    raise AssetNotMaintainException(f"Asset {asset_id} has not been maintained for over 2 years.")
                else:
                    print("The Asset is currently in maintenance")



            # Record the new maintenance
            '''query = """
                INSERT INTO maintenance (maintenance_id, asset_id, maintenance_date, mdescription, cost)
                VALUES (?, ?, ?, ?, ?)
                """
            cursor.execute(query, maintenance_id, asset_id, maintenance_date_obj, description, cost) '''
            self.connection.commit()
            return True
        except AssetNotMaintainException as e:
            print(e)
            return False
        except Exception as e:
            print(f"Error performing maintenance: {e}")
            return False

    def reserve_asset(self, reservation_id , asset_id, employee_id, reservation_date, start_date, end_date,status):
        cursor = self.connection.cursor()
        query = """
        INSERT INTO reservations (reservation_id, asset_id, employee_id, reservation_date, start_date1, end_date1, status1)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        try:
            cursor.execute(query, reservation_id, asset_id, employee_id, reservation_date, start_date, end_date, status)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error reserving asset: {e}")
            return False

    def withdraw_reservation(self, reservation_id):
        cursor = self.connection.cursor()
        query = "DELETE FROM reservations WHERE reservation_id = ?"
        try:
            cursor.execute(query, reservation_id)
            if cursor.rowcount == 0:
                raise AssetNotFoundException(f"Reservation with ID {reservation_id} not found.")
            self.connection.commit()
            return True
        except AssetNotFoundException as e:
            print(e)
            return False
        except Exception as e:
            print(f"Error withdrawing reservation: {e}")
            return False
