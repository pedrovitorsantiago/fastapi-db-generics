from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

#ADDRESS
class AddressBase(SQLModel):
    street: str = Field(max_length=120)
    number: Optional[str] = Field(max_length=20)
    state: str = Field(max_length=2) # UF
    city: str = Field(max_length=100)
    neighborhood: str = Field(max_length=100) # Bairro

class Address(AddressBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    person_id: int = Field(foreign_key="person.id")
    person: "Person" = Relationship(back_populates="addresses")


#PERSON
class PersonBase(SQLModel):
    name: str = Field(min_length=2, max_length=120)
    age: int = Field(ge=0, le=200)
    email: str = Field(unique=True, index=True)

class Person(PersonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    addresses: List["Address"] = Relationship(back_populates="person")
