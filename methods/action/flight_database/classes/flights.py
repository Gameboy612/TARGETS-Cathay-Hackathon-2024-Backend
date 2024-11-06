from pymongo import ReturnDocument

from mongodb import mongodb
from methods._utilities.default_responses import SuccessResponse, ErrorResponse
import datetime

class flights:
    col = mongodb["flights"]
    @classmethod
    def query(cls, **query):
        """Wrapper for mongodb query.

        :param filter: A query document that selects which documents
            to include in the result set. Can be an empty document to include all documents.
        :param projection: a list of field names that should be
            returned in the result set or a dict specifying the fields to include or exclude. If projection is a list "_id" will always be returned. Use a dict to exclude fields from
            the result (e.g. projection={'_id': False}).
        :param session: a
            ~pymongo.client_session.ClientSession.
        :param skip: the number of documents to omit (from
            the start of the result set) when returning the results
        :param limit: the maximum number of results to
            return. A limit of 0 (the default) is equivalent to setting no limit.
        :param no_cursor_timeout: if False (the default), any
            returned cursor is closed by the server after 10 minutes of inactivity. If set to True, the returned cursor will never time out on the server. Care should be taken to ensure that cursors with no_cursor_timeout turned on are properly closed.
        :param cursor_type: the type of cursor to return. The valid
            options are defined by ~pymongo.cursor.CursorType:

        ~pymongo.cursor.CursorType.NON_TAILABLE - the result of this find call will return a standard cursor over the result set.
        ~pymongo.cursor.CursorType.TAILABLE - the result of this find call will be a tailable cursor - tailable cursors are only for use with capped collections. They are not closed when the last data is retrieved but are kept open and the cursor location marks the final document position. If more data is received iteration of the cursor will continue from the last document received. For details, see the tailable cursor documentation <https://www.mongodb.com/docs/manual/core/tailable-cursors/>_.
        ~pymongo.cursor.CursorType.TAILABLE_AWAIT - the result of this find call will be a tailable cursor with the await flag set. The server will wait for a few seconds after returning the full result set so that it can capture and return additional data added during the query.
        ~pymongo.cursor.CursorType.EXHAUST - the result of this find call will be an exhaust cursor. MongoDB will stream batched results to the client without waiting for the client to request each batch, reducing latency. See notes on compatibility below.
        :param sort: a list of (key, direction) pairs
            specifying the sort order for this query. See
            ~pymongo.cursor.Cursor.sort for details.
        :param allow_partial_results: if True, mongos will return
            partial results if some shards are down instead of returning an error.
        :param oplog_replay: **DEPRECATED** - if True, set the
            oplogReplay query flag. Default: False.
        :param batch_size: Limits the number of documents returned in
            a single batch.
        :param collation: An instance of
            ~pymongo.collation.Collation.
        :param return_key: If True, return only the index keys in
            each document.
        :param show_record_id: If True, adds a field $recordId in
            each document with the storage engine's internal record identifier.
        :param snapshot: **DEPRECATED** - If True, prevents the
            cursor from returning a document more than once because of an intervening write operation.
        :param hint: An index, in the same format as passed to
            ~pymongo.collection.Collection.create_index (e.g. [('field', ASCENDING)]). Pass this as an alternative to calling
            ~pymongo.cursor.Cursor.hint on the cursor to tell Mongo the proper index to use for the query.
        :param max_time_ms: Specifies a time limit for a query
            operation. If the specified time is exceeded, the operation will be
            aborted and ~pymongo.errors.ExecutionTimeout is raised. Pass this as an alternative to calling
            ~pymongo.cursor.Cursor.max_time_ms on the cursor.
        :param max_scan: **DEPRECATED** - The maximum number of
            documents to scan. Pass this as an alternative to calling
            ~pymongo.cursor.Cursor.max_scan on the cursor.
        :param min: A list of field, limit pairs specifying the
            inclusive lower bound for all keys of a specific index in order. Pass this as an alternative to calling
            ~pymongo.cursor.Cursor.min on the cursor. hint must also be passed to ensure the query utilizes the correct index.
        :param max: A list of field, limit pairs specifying the
            exclusive upper bound for all keys of a specific index in order. Pass this as an alternative to calling
            ~pymongo.cursor.Cursor.max on the cursor. hint must also be passed to ensure the query utilizes the correct index.
        :param comment: A string to attach to the query to help
            interpret and trace the operation in the server logs and in profile data. Pass this as an alternative to calling
            ~pymongo.cursor.Cursor.comment on the cursor.
        :param allow_disk_use: if True, MongoDB may use temporary
            disk files to store data exceeding the system memory limit while processing a blocking sort operation. The option has no effect if MongoDB can satisfy the specified sort using an index, or if the blocking sort requires less memory than the 100 MiB limit. This option is only supported on MongoDB 4.4 and above.
        """
        result = cls.col.find(**query)
        return list(result)
    
    @classmethod
    def update(cls, flightid, data: dict):
        DATA = data
        DATA["_id"] = flightid
        DATA["_last_modified"] = datetime.datetime.timestamp(datetime.datetime.now())
        
        UPDATE = {'$set': DATA}
        result = cls.col.find_one_and_update({'_id': flightid}, UPDATE, upsert=True, return_document=ReturnDocument.AFTER)

        if "_id" in result:
            return SuccessResponse({
                "_id": flightid,
                "flight": result
            }, "Updated Flight Data successfully")

        return ErrorResponse("MongoDB acccess failed")
    
