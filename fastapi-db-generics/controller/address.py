from fastapi import HTTPException
from sqlmodel import Session
from controller.generic import create_crud_router, Hooks
from model.models import Address, Person
from model.dto import AddressCreate, AddressUpdate, AddressRead

class AddressHooks(Hooks[Address, AddressCreate, AddressUpdate]):
    def pre_create(self, payload: AddressCreate, session: Session) -> None:
        """Valida se a pessoa (person_id) existe antes de criar o endereço."""
        if not session.get(Person, payload.person_id):
            raise HTTPException(status_code=404, detail=f"Person with id {payload.person_id} not found.")

router = create_crud_router(
    model=Address,
    create_schema=AddressCreate,
    update_schema=AddressUpdate,
    read_schema=AddressRead,
    prefix="/addresses",
    tags=["addresses"],
    hooks=AddressHooks(),
)