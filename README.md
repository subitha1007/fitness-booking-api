# Fitness Booking API

A simple booking system for a fictional fitness studio built with FastAPI. This API allows clients to view available classes, book classes, and check their bookings — all with timezone support and input validation.

---

##  **FEATURES**

-- View upcoming fitness classes

-- Book a class with client name and email

-- Retrieve all bookings by email

-- Timezone-aware date & time handling (default IST)

-- In-memory database (no setup required)

-- Error handling and validation included

-- Unit testing using Pytest

---

## **TECHNOLOGIES USED**

--Python 3.9+

--FastAPI

--Pydantic

--pytz

--uuid

--pytest

---

### **SETUP INSTRUCTIONS**

#Clone the repo:
git clone https://github.com/usernam/Fitness_booking_api.git
cd Fitness_booking_api

**(Optional) Create a virtual environment:**
python -m venv venv

**Activate:**
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)

**Install dependencies:**
pip install -r requirements.txt

**Run the API:**
uvicorn main:app --reload

**Open in browser:**
http://127.0.0.1:8000/docs

---

## **API ENDPOINTS**


*GET /classes*
Returns a list of all upcoming fitness classes.
Query param: timezone_str (optional, default = Asia/Kolkata)

**Sample curl:**
curl -X GET "http://127.0.0.1:8000/classes?timezone_str=Asia/Kolkata"

*POST /book*
Accepts a booking request with class_id, client_name, and client_email. Reduces available slots if booking is successful.

*Request body:*
{
"class_id": 1,
"client_name": "Subitha",
"client_email": "subitha@example.com"
}

**Sample curl:**
*curl -X POST "http://127.0.0.1:8000/book" -H "Content-Type: application/json" -d "{"class_id":1,"client_name":"Subitha","client_email":"subitha@example.com"}"*

*GET /bookings*
Returns all bookings made using a specific email.

Query param: email (required)

**Sample curl:**
*curl -X GET "http://127.0.0.1:8000/bookings?email=subitha@example.com"*

---

## **SAMPLE SEED DATA**

[
{
"id": 1,
"name": "Yoga",
"datetime": "2025-06-06 07:00 IST",
"instructor": "Aarti",
"available_slots": 5
},
{
"id": 2,
"name": "Zumba",
"datetime": "2025-06-06 08:30 IST",
"instructor": "Vikram",
"available_slots": 3
},
{
"id": 3,
"name": "HIIT",
"datetime": "2025-06-06 10:00 IST",
"instructor": "Riya",
"available_slots": 4
}
]

---

## **TESTING**

**Run tests with:**
--pytest -v

**Expected output:**
--test_main.py::test_book_class PASSED

**KEY CONCEPTS USED**

--*FastAPI* for rapid API development

--*Pydantic* models for input validation

--*pytz* for timezone conversion

--*uuid* for generating unique booking IDs

--*In-memory list*-based DB (no setup required)

--*HTTPException* for handling error states

---

## **LOOM VIDEO**

-- Submit a Loom walkthrough video explaining the code and testing process.
**Example link:** https://drive.google.com/file/d/1Wi_1U2Mw0X06i97r2iXUyked4v6MDDSW/view?usp=drivesdk

---

## **AUTHOR**

--*Subitha M*
--*Email: subitha@example.com*
--*GitHub: https://github.com/subitha1007*

---
**LICENSE**

--*This project is for demonstration and educational use only.*

---
