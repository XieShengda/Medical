from fastapi import FastAPI, Path, BackgroundTasks

import config
import execute
from config import db_connection
from response_body import ResponseBody
from status import Status

app = FastAPI()


## mysql

def execute_read_by_sql(sql):
    with db_connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def execute_write_by_sql(sql):
    with db_connection.cursor() as cursor:
        rowcount = cursor.execute(sql)
        db_connection.commit()
        return rowcount


@app.on_event("shutdown")
async def shutdown():
    db_connection.close()


## start business code

@app.get("/image/{record_id}")
async def get_image_by_id(record_id: int = Path(title='Record id most greater than 0', gt=0)):
    data = execute_read_by_sql("SELECT * FROM {0} where id = {1}".format(config.IMAGE_TABLE_NAME, record_id))
    if len(data) == 0:
        return ResponseBody.error_404()
    return ResponseBody.ok(data)


@app.get("/process/{record_id}")
async def process(background_tasks: BackgroundTasks,
                  record_id: int = Path(title='Record id most greater than 0', gt=0)):
    rowcount = update_status_by_id(record_id, Status.Processing.value)
    if rowcount == 0:
        return ResponseBody.error_404()

    background_tasks.add_task(infer_async, record_id)

    return ResponseBody.ok(
        data=execute_read_by_sql(
            "SELECT id, status FROM {0} where id = {1}".format(config.IMAGE_TABLE_NAME, record_id)))


def infer_async(record_id: int):
    # todo 进行推理，推理结束之后改状态
    execute.infer()
    update_status_by_id(record_id, Status.Completed.value)


def update_status_by_id(record_id: int, status: int):
    return execute_write_by_sql(
        "UPDATE {0} SET status = {2} WHERE id = {1} and status = {3}".format(config.IMAGE_TABLE_NAME, record_id, status,
                                                                             status - 1))
