SECONDARIES_NODES = [
    # {"name": "secondary 1", "url": "ws://localhost:8001/append_msg"},
    {"name": "secondary 1", "url": "ws://secondary-1:8000/append_msg"},
    {"name": "sleepy-secondary", "url": "ws://sleepy-secondary:8000/append_msg"},
    {"name": "secondary 2", "url": "ws://secondary-2:8000/append_msg"},
    {"name": "secondary 3", "url": "ws://secondary-3:8000/append_msg"},
]

MESSAGE_REPLICATION_STATUS_FAILED = "failed"
MESSAGE_REPLICATION_STATUS_OK = "OK"
