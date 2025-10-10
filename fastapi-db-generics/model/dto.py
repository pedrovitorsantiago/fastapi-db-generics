from model.models import PersonBase, AddressBase
from typing import List, Optional

#DTOs para Address
class AddressRead(AddressBase):
    id: int

class AddressCreate(AddressBase):
    person_id: int # ID da pessoa para vincular o endereço

class AddressUpdate(AddressBase):
    street: Optional[str] = None
    number: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    neighborhood: Optional[str] = None


#DTOs para Person
class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

class PersonRead(PersonBase):
    id: int

# Schema especial para retornar a pessoa com seus endereços
class PersonReadWithAddresses(PersonRead):
    addresses: List[AddressRead] = []
