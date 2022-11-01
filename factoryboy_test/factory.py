import factory


class BaseModel:
    def __init__(self, name):
        self.name = name
        print(f"Creating {self.__class__.__name__} object: {name}")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self)

    def __str__(self):
        return "%s object (%s)" % (self.__class__.__name__, self.name)


class Device(BaseModel):
    def __init__(
        self,
        description=None,
        site=None,
        device_type=None,
        device_role=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.description = description
        self.site = site
        self.device_type = device_type
        self.device_role = device_role


class DeviceType(BaseModel):
    def __init__(self, manufacturer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.manufacturer = manufacturer


class Manufacturer(BaseModel):
    pass


class Site(BaseModel):
    pass


class DeviceRole(BaseModel):
    pass


class DeviceFactory(factory.Factory):
    class Meta:
        model = Device

    name = factory.Sequence(lambda n: f"Device {n}")
    description = factory.Faker("sentence", nb_words=3)
    site = factory.SubFactory("factoryboy_test.factory.SiteFactory")
    device_type = factory.SubFactory("factoryboy_test.factory.DeviceTypeFactory")
    device_role = factory.SubFactory("factoryboy_test.factory.DeviceRoleFactory")


class DeviceTypeFactory(factory.Factory):
    class Meta:
        model = DeviceType

    name = factory.Sequence(lambda n: f"Device Type {n}")
    manufacturer = factory.SubFactory("factoryboy_test.factory.ManufacturerFactory")


class ManufacturerFactory(factory.Factory):
    class Meta:
        model = Manufacturer

    name = factory.Sequence(lambda n: f"Manufacturer {n}")


class DeviceRoleFactory(factory.Factory):
    class Meta:
        model = DeviceRole

    name = factory.Sequence(lambda n: f"Device Role {n}")


class SiteFactory(factory.Factory):
    class Meta:
        model = Site

    name = factory.Sequence(lambda n: f"Site {n}")


class SampleModel:
    def __init__(self, company, address):
        self.company = company
        self.address = address

    def __repr__(self):
        return str(self.__dict__)


class SampleFactory(factory.Factory):
    class Meta:
        model = SampleModel

    company = factory.Faker("company")
    address = factory.Faker("address")
