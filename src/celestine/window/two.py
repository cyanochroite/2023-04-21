def main(session, frame):
    window = session.task
    window.label(frame, "title", "Page 2")
    window.button(frame, "previous", "Page 1")
    window.button(frame, "next", "Page 0")
