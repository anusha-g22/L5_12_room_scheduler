"""Manage room reservations, equipment allocation, and scheduling conflicts."""
import json
from datetime import datetime
from pathlib import Path

reservations = {}
equipment_pool = {"projector": 2, "microphone": 4, "webcam": 1}
conflicts = []
NEXT_RESERVATION = 1


def schedule_room(room_id, time_slot, equipment_list=None):
    """Schedule a room and reserve the requested equipment."""
    global NEXT_RESERVATION

    if equipment_list is None:
        equipment_list = []

    if not isinstance(time_slot, str):
        raise TypeError("time_slot must be a string such as '10-12'.")

    for reservation in reservations.values():
        if reservation["room"] == room_id and reservation["slot"] == time_slot:
            conflicts.append(f"{room_id} double-booked at {time_slot}")

    for equipment in equipment_list:
        if equipment not in equipment_pool:
            raise ValueError(f"Unknown equipment: {equipment}")
        if equipment_pool[equipment] <= 0:
            raise ValueError(f"No {equipment} available.")

    for equipment in equipment_list:
        equipment_pool[equipment] -= 1

    reservation_id = NEXT_RESERVATION
    reservations[reservation_id] = {
        "room": room_id,
        "slot": time_slot,
        "equipment": equipment_list.copy(),
    }
    NEXT_RESERVATION += 1

    return reservation_id


def cancel_reservation(reservation_id):
    """Cancel a reservation and return its equipment."""
    reservation = reservations.pop(reservation_id, None)

    if reservation is None:
        print(f"Reservation {reservation_id} does not exist.")
        return

    for equipment in reservation["equipment"]:
        equipment_pool[equipment] += 1


def slot_hours(time_slot):
    """Calculate the duration of a time slot in hours."""
    if not isinstance(time_slot, str):
        raise TypeError("time_slot must be a string such as '10-12'.")

    try:
        start_text, end_text = time_slot.split("-")
        start = int(start_text)
        end = int(end_text)
    except ValueError as error:
        raise ValueError(
            "Invalid time slot. Use a format such as '10-12'."
        ) from error

    if start < 0 or end <= start:
        raise ValueError("The end time must be greater than the start time.")

    return end - start


def export_schedule(file="schedule.json"):
    """Export the current reservations to a JSON file."""
    with open(file, "w", encoding="utf-8") as schedule_file:
        json.dump(reservations, schedule_file, indent=4)


def log_conflicts(file="conflicts.log"):
    """Append scheduling conflicts to a log file."""
    log_path = Path(file)

    with log_path.open("a", encoding="utf-8") as log_file:
        for conflict in conflicts:
            log_file.write(f"{datetime.now()} {conflict}\n")

    if log_path.exists():
        print(log_path.read_text(encoding="utf-8"))


def main():
    """Run the room scheduling demonstration."""
    schedule_room("Board-1", "09-11")
    schedule_room("Board-1", "09-11")
    schedule_room("Huddle-3", "10-12")

    print(
        "Slot length for Huddle-3:",
        slot_hours(reservations[3]["slot"]),
    )

    cancel_reservation(77)

    slot = input(
        "Slot for Board-2, like 10-12 (Enter for 10-12): "
    ) or "10-12"

    try:
        schedule_room("Board-2", slot, ["projector", "webcam"])
    except (TypeError, ValueError) as error:
        print(f"Could not schedule room: {error}")

    export_schedule()
    log_conflicts()

    print("Equipment left:", equipment_pool)
    print("Reservations:", reservations)


if __name__ == "__main__":
    main()
