from fastapi.params import Depends
from sqlalchemy.ext.asyncio import  AsyncSession
from typing import Annotated

from app.core.session import get_session

from app.services.handler_json import DecoderFile

from app.repositories.add_data import AddOrm



async def to_go_load_test_data(session_db: AsyncSession):
    builds = DecoderFile.unpacking_json('app/db/builds.json')

    model = AddOrm(session_db)
    await model.loading_builds(builds)

    organisations = DecoderFile.unpacking_json('app/db/organisations.json')
    await model.loading_organizations(organisations)

    return 1