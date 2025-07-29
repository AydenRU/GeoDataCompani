from app.services.handler_json import DecoderFile


from app.repositories.add_data import AddOrm



async def to_go_load_test_data(session_db):

    builds = DecoderFile.unpacking_json('app/db/builds.json')
    await AddOrm.loading_builds(builds, session_db)

    organisations = DecoderFile.unpacking_json('app/db/organisations.json')
    await AddOrm.loading_organizations(organisations, session_db)
    return 1