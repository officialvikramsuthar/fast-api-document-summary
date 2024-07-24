async def add_file(db, file_metadata):
    await db.files.insert_one(file_metadata)


async def get_file(db, file_id):
    return await db.files.find_one({"file_id": file_id})


async def list_files(db):
    files = await db.files.find().to_list(100)
    return [{"file_id":file["file_id"], "name":file["file_name"], "summary":file["file_summary"]} for file in files]
