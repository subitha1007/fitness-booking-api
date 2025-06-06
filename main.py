from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from pytz import timezone, all_timezones
import pytz
import uuid

app = FastAPI()

# --- In-memory data storage ---
classes_db = []
bookings_db = []

# --- IST timezone ---
IST = timezone("Asia/Kolkata")

# --- Models ---
class ClassCreate(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class ClassOut(BaseModel):
    id: int
    name: str
    datetime: str
    instructor: str
    available_slots: int

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class Booking(BaseModel):
    booking_id: str
    class_id: int
    client_name: str
    client_email: EmailStr
    booked_at: str

# --- Seed data ---
classes_db = [
    {
        "id": 1,
        "name": "Yoga",
        "datetime": IST.localize(datetime(2025, 6, 6, 7, 0)),
        "instructor": "Aarti",
        "available_slots": 5
    },
    {
        "id": 2,
        "name": "Zumba",
        "datetime": IST.localize(datetime(2025, 6, 6, 8, 30)),
        "instructor": "Vikram",
        "available_slots": 3
    },
    {
        "id": 3,
        "name": "HIIT",
        "datetime": IST.localize(datetime(2025, 6, 6, 10, 0)),
        "instructor": "Riya",
        "available_slots": 4
    },
]

# --- Endpoints ---
@app.get("/classes", response_model=List[ClassOut])
def get_classes(timezone_str: Optional[str] = Query("Asia/Kolkata")):
    if timezone_str not in all_timezones:
        raise HTTPException(status_code=400, detail="Invalid timezone")
    user_tz = timezone(timezone_str)

    result = []
    for cls in classes_db:
        class_time = cls["datetime"].astimezone(user_tz)
        result.append({
            "id": cls["id"],
            "name": cls["name"],
            "datetime": class_time.strftime("%Y-%m-%d %H:%M %Z"),
            "instructor": cls["instructor"],
            "available_slots": cls["available_slots"]
        })
    return result

@app.post("/book", response_model=Booking)
def book_class(request: BookingRequest):
    for cls in classes_db:
        if cls["id"] == request.class_id:
            if cls["available_slots"] > 0:
                cls["available_slots"] -= 1
                booking = {
                    "booking_id": str(uuid.uuid4()),
                    "class_id": cls["id"],
                    "client_name": request.client_name,
                    "client_email": request.client_email,
                    "booked_at": datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S %Z")
                }
                bookings_db.append(booking)
                return booking
            else:
                raise HTTPException(status_code=400, detail="No available slots")
    raise HTTPException(status_code=404, detail="Class not found")

@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: EmailStr):
    return [b for b in bookings_db if b["client_email"] == email]
