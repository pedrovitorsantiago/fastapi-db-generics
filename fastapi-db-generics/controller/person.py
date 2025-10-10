from controller.generic import create_crud_router
from model.models import Person
from model.dto import PersonCreate, PersonUpdate, PersonRead, PersonReadWithAddresses

router = create_crud_router(
    model=Person,
    create_schema=PersonCreate,
    update_schema=PersonUpdate,
    read_schema=PersonRead,               # Usado em POST, PATCH e GET (lista)
    read_one_schema=PersonReadWithAddresses, # Usado no GET /{id}
    prefix="/persons",
    tags=["persons"],
)