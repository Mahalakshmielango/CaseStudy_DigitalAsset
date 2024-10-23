from dao.asset_management_service_impl import AssetManagementServiceImpl
from entity.models import Asset, Employee
from exceptions.asset_exceptions import AssetNotFoundException, AssetNotMaintainException


def main():
    service = AssetManagementServiceImpl()

    while True:
        print("\n-- Digital Asset Management System --")
        print("1. Add Asset")
        print("2. Update Asset")
        print("3. Delete Asset")
        print("4. Allocate Asset")
        print("5. Deallocate Asset")
        print("6. Perform Maintenance")
        print("7. Reserve Asset")
        print("8. Withdraw Reservation")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                asset_id = int(input("Enter Asset ID: "))
                name = input("Enter Asset Name: ")
                asset_type = input("Enter Asset Type: ")
                serial_number = input("Enter Serial Number: ")
                purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
                location = input("Enter Location: ")
                status = input("Enter Status (e.g., in use, under maintenance): ")
                owner_id = int(input("Enter Owner ID: "))

                asset = Asset(asset_id, name, asset_type, serial_number, purchase_date, location, status, owner_id)
                result = service.add_asset(asset)

                if result:
                    print("Asset added successfully.")
                else:
                    print("Failed to add asset.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 2:
            try:
                asset_id = int(input("Enter Asset ID to update: "))
                name = input("Enter New Asset Name: ")
                asset_type = input("Enter New Asset Type: ")
                serial_number = input("Enter New Serial Number: ")
                purchase_date = input("Enter New Purchase Date (YYYY-MM-DD): ")
                location = input("Enter New Location: ")
                status = input("Enter New Status: ")
                owner_id = int(input("Enter New Owner ID: "))

                asset = Asset(asset_id, name, asset_type, serial_number, purchase_date, location, status, owner_id)
                result = service.update_asset(asset)

                if result:
                    print("Asset updated successfully.")
                else:
                    print("Failed to update asset.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 3:
            try:
                asset_id = int(input("Enter Asset ID to delete: "))
                result = service.delete_asset(asset_id)

                if result:
                    print("Asset deleted successfully.")
                else:
                    print("Failed to delete asset.")
            except AssetNotFoundException:
                print("Asset not found.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 4:
            try:
                allocation_id = int(input("Enter Allocation ID to allocate: "))
                asset_id = int(input("Enter Asset ID to allocate: "))
                employee_id = int(input("Enter Employee ID: "))
                allocation_date = input("Enter Allocation Date (YYYY-MM-DD): ")
                return_date = input("Enter return Date (YYYY-MM-DD): ")

                result = service.allocate_asset(allocation_id,asset_id, employee_id, allocation_date,return_date)

                if result:
                    print("Asset allocated successfully.")
                else:
                    print("Failed to allocate asset.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 5:
            try:
                asset_id = int(input("Enter Asset ID to deallocate: "))
                employee_id = int(input("Enter Employee ID: "))
                return_date = input("Enter Return Date (YYYY-MM-DD): ")

                result = service.deallocate_asset(asset_id, employee_id, return_date)

                if result:
                    print("Asset deallocated successfully.")
                else:
                    print("Failed to deallocate asset.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 6:
            try:
                maintenance_id = int(input("Enter maintenance ID for maintenance: "))
                asset_id = int(input("Enter Asset ID for maintenance: "))
                maintenance_date = input("Enter Maintenance Date (YYYY-MM-DD): ")


                result = service.perform_maintenance(maintenance_id,asset_id, maintenance_date)

                if result:
                    print("Maintenance recorded successfully.")
                else:
                    print("Failed to record maintenance.")
            except AssetNotMaintainException:
                print("Asset has not been maintained for 2 years.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 7:
            try:
                reservation_id = int(input("Enter reservation ID to reserve: "))
                asset_id = int(input("Enter Asset ID to reserve: "))
                employee_id = int(input("Enter Employee ID: "))
                reservation_date = input("Enter Reservation Date (YYYY-MM-DD): ")
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                status=input("Enter status: ")

                result = service.reserve_asset(reservation_id, asset_id, employee_id, reservation_date, start_date, end_date,status)

                if result:
                    print("Asset reserved successfully.")
                else:
                    print("Failed to reserve asset.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 8:
            try:
                reservation_id = int(input("Enter Reservation ID to withdraw: "))
                result = service.withdraw_reservation(reservation_id)

                if result:
                    print("Reservation withdrawn successfully.")
                else:
                    print("Failed to withdraw reservation.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == 9:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
