# Assignment 1: Base class
class Device:
    def __init__(self, brand, model):
        self._brand = brand      # Protected attribute (encapsulation)
        self._model = model

    def device_info(self):
        return f"{self._brand} {self._model}"

    def power_on(self):
        print(f"{self.device_info()} is now powered on.")


# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_megapixels = camera_megapixels
        self.installed_apps = []

    def install_app(self, app_name):
        self.installed_apps.append(app_name)
        print(f"{app_name} has been installed on {self.device_info()}.")

    def take_photo(self):
        print(
            f"Photo taken with {self.camera_megapixels}MP camera on {self.device_info()}.")

    def show_installed_apps(self):
        print(
            f"Installed apps on {self.device_info()}: {', '.join(self.installed_apps)}")


# Example usage
my_phone = Smartphone("Samsung", "Galaxy S22", "256GB", 108)
my_phone.power_on()
my_phone.install_app("Instagram")
my_phone.take_photo()
my_phone.show_installed_apps()

# Activity 2: Polymorphism Challenge


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method.")


class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


# Polymorphic behavior in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move(
