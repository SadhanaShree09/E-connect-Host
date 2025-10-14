from Mongo import Otherleave_History_Details,Permission_History_Details, Users,admin,normal_leave_details,store_Other_leave_request,get_approved_leave_history,get_remote_work_requests,attendance_details,leave_History_Details,Remote_History_Details,get_attendance_by_date,update_remote_work_request_status_in_mongo,updated_user_leave_requests_status_in_mongo,get_user_leave_requests, get_employee_id_from_db,store_Permission_request, get_all_users, get_admin_info, add_task_list, edit_the_task, delete_a_task, get_the_tasks, delete_leave, get_user_info, store_sunday_request, get_admin_info, add_an_employee, PreviousDayClockout, auto_clockout, leave_update_notification, recommend_manager_leave_requests_status_in_mongo, get_manager_leave_requests, get_only_user_leave_requests, get_admin_page_remote_work_requests, update_remote_work_request_recommend_in_mongo, get_TL_page_remote_work_requests, users_leave_recommend_notification, managers_leave_recommend_notification,auto_approve_manager_leaves,edit_an_employee,get_managers,task_assign_to_multiple_users, get_team_members, get_local_ip, get_public_ip, assigned_task, get_single_task, get_user_by_position, get_hr_assigned_tasks, get_manager_hr_assigned_tasks, get_hr_self_assigned_tasks, get_manager_only_tasks, create_notification, get_notifications, mark_notification_read, mark_all_notifications_read, get_unread_notification_count, delete_notification, get_notifications_by_type, create_task_notification, create_leave_notification, create_wfh_notification, create_system_notification, create_attendance_notification, notify_leave_submitted, notify_leave_approved, notify_leave_rejected, notify_leave_recommended, notify_wfh_submitted, notify_wfh_approved, notify_wfh_rejected, store_leave_request, store_remote_work_request, get_admin_user_ids, get_hr_user_ids, get_user_position, notify_admin_manager_leave_request, notify_hr_recommended_leave, notify_hr_pending_leaves, notify_admin_pending_leaves, get_current_timestamp_iso, Notifications, notify_manager_leave_request, get_user_manager_id
from model import Item4,Item,Item2,Item3,Csvadd,Csvedit,Csvdel,CT,Item5,Item6,Item9,RemoteWorkRequest,Item7,Item8, Tasklist, Taskedit, Deletetask, Gettasks, DeleteLeave, Item9, AddEmployee,EditEmployee,Taskassign, SingleTaskAssign, NotificationModel, NotificationUpdate, NotificationFilter
from fastapi import FastAPI, HTTPException,Path,Query, HTTPException,Form, Request, WebSocket, WebSocketDisconnect
from websocket_manager import notification_manager
from Mongo import Leave, RemoteWork, Otherleave_History_Details,Permission_History_Details, Users,admin,normal_leave_details,store_Other_leave_request,get_approved_leave_history,get_remote_work_requests,attendance_details,leave_History_Details,Remote_History_Details,get_attendance_by_date,update_remote_work_request_status_in_mongo,updated_user_leave_requests_status_in_mongo,get_user_leave_requests, get_employee_id_from_db,store_Permission_request, get_all_users, get_admin_info, add_task_list, edit_the_task, delete_a_task, get_the_tasks, delete_leave, get_user_info, store_sunday_request, get_admin_info, add_an_employee, PreviousDayClockout, auto_clockout, leave_update_notification, recommend_manager_leave_requests_status_in_mongo, get_manager_leave_requests, get_only_user_leave_requests, get_admin_page_remote_work_requests, update_remote_work_request_recommend_in_mongo, get_TL_page_remote_work_requests, users_leave_recommend_notification, managers_leave_recommend_notification,auto_approve_manager_leaves,edit_an_employee,get_managers,task_assign_to_multiple_users, get_team_members, get_local_ip, get_public_ip, assigned_task, get_single_task, get_manager_only_tasks, insert_holidays, get_holidays, calculate_working_days, calculate_user_attendance_stats, get_user_attendance_dashboard, get_team_attendance_stats, get_department_attendance_stats, get_manager_team_attendance, update_daily_attendance_stats, get_user_leave_requests_with_history, get_manager_leave_requests_with_history, get_only_user_leave_requests_with_history, get_remote_work_requests_with_history, get_admin_page_remote_work_requests_with_history, get_TL_page_remote_work_requests_with_history
from model import Item4,Item,Item2,Item3,Csvadd,Csvedit,Csvdel,CT,Item5,Item6,Item9,RemoteWorkRequest,Item7,Item8, Tasklist, Taskedit, Deletetask, Gettasks, DeleteLeave, Item9, AddEmployee,EditEmployee,Taskassign, SingleTaskAssign, HolidayYear, Holiday
from fastapi import FastAPI, HTTPException,Path,Query, HTTPException,Form, Request
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI,Body
from auth.auth_bearer import JWTBearer
from http.client import HTTPException
from datetime import datetime, timedelta, date
from dateutil import parser
from typing import Union, Dict, List, Optional
from bson import ObjectId
from bson import json_util
import json
import uvicorn
import Mongo
import pytz
import os
from typing import List,Any, Dict
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import uuid, os
from datetime import datetime
from bson import ObjectId
import asyncio
from dotenv import load_dotenv
load_dotenv() 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# GridFS setup
from pymongo import MongoClient
import gridfs
mongo_url = os.environ.get("MONGODB_URI")
client = MongoClient(
    mongo_url,
    serverSelectionTimeoutMS=30000,
    connectTimeoutMS=30000,
    socketTimeoutMS=30000
) 
db = client["RBG_AI"]  
fs = gridfs.GridFS(db)

from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import uuid, os
from datetime import datetime
from bson import ObjectId
import json
from bson import Binary, ObjectId
import shutil
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
import io
import pytz
from bson import Binary
import uvicorn
import traceback
import uuid
from bson import ObjectId
from fastapi import (
    Body,
    Depends,
    FastAPI,
    Form,
    HTTPException,
    Path,
    Query,
    Request,
    WebSocket,
    WebSocketDisconnect,
    File,
    UploadFile,
    Form,

     
)
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from ws_manager import DirectChatManager, GeneralChatManager, NotifyManager,GroupChatManager

import Mongo
from Mongo import (
    Otherleave_History_Details,
    Permission_History_Details,
    normal_leave_details,
    store_Other_leave_request,
    get_approved_leave_history,
    get_remote_work_requests,
    attendance_details,
    leave_History_Details,
    Remote_History_Details,
    get_attendance_by_date,
    update_remote_work_request_status_in_mongo,
    updated_user_leave_requests_status_in_mongo,
    get_user_leave_requests,
    get_employee_id_from_db,
    store_Permission_request,
    get_all_users,
    get_admin_info,
    add_task_list,
    edit_the_task,
    delete_a_task,
    get_the_tasks,
    delete_leave,
    get_user_info,
    store_sunday_request,
    get_admin_info,
    add_an_employee,
    PreviousDayClockout,
    auto_clockout,
    leave_update_notification,
    recommend_manager_leave_requests_status_in_mongo,
    get_manager_leave_requests,
    get_only_user_leave_requests,
    get_admin_page_remote_work_requests,
    update_remote_work_request_recommend_in_mongo,
    get_TL_page_remote_work_requests,
    users_leave_recommend_notification,
    managers_leave_recommend_notification,
    auto_approve_manager_leaves,
    edit_an_employee,
    get_managers,
    task_assign_to_multiple_users,
    task_assign_to_multiple_users_with_notification,
    get_team_members,
    assigned_task,
    get_single_task,
    get_public_ip,
    get_local_ip,
    get_allowed_contacts,
    append_chat_message,
    get_chat_history,
    chats_collection,
    threads_collection,
    groups_collection,
    update_file_status,
    get_assigned_docs,
    save_file_to_db,
    assign_docs,
    assignments_collection,
    Users,
    messages_collection,
    files_collection
    
    
    
    
)
from model import (
    
    AssignPayload,
    Message,
    ThreadMessage,
    Reaction,
    ChatHistoryResponse,
    PresencePayload,
    AssignPayload,
    ReviewPayload,
    ReviewDocument,
    GroupCreate,
    GroupUpdate,
   UpdateGroupPayload,
)
from auth.auth_bearer import JWTBearer
direct_chat_manager = DirectChatManager()

active_users: Dict[str, WebSocket] = {}
active_connections: Dict[str, WebSocket] = {}
# Task-specific chat manager


direct_chat_manager = DirectChatManager()
chat_manager = GeneralChatManager()
notify_manager = NotifyManager()
group_ws_manager = GroupChatManager()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
import atexit

# Utility function to serialize MongoDB documents to JSON
def serialize_mongo_doc(doc):
    """
    Convert MongoDB document to JSON-serializable format.
    Handles ObjectId, datetime, date, and nested structures.
    """
    if not doc:
        return None
    
    if isinstance(doc, list):
        return [serialize_mongo_doc(item) for item in doc]
    
    if not isinstance(doc, dict):
        if isinstance(doc, ObjectId):
            return str(doc)
        elif isinstance(doc, (datetime, date)):
            return doc.isoformat()
        return doc
    
    # Convert ObjectId and datetime fields to strings
    serialized = {}
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            serialized[key] = str(value)
        elif isinstance(value, datetime):
            serialized[key] = value.isoformat()
        elif isinstance(value, date):
            serialized[key] = value.isoformat()
        elif isinstance(value, list):
            # Handle lists that might contain ObjectIds, datetimes, or dicts
            serialized[key] = [serialize_mongo_doc(item) for item in value]
        elif isinstance(value, dict):
            # Recursively handle nested dictionaries
            serialized[key] = serialize_mongo_doc(value)
        else:
            serialized[key] = value
    
    return serialized

app = FastAPI()

# Get CORS origins from environment or use defaults
allowed_origins_env = os.environ.get("ALLOWED_ORIGINS", "")
if allowed_origins_env:
    origins = [origin.strip() for origin in allowed_origins_env.split(",")]
else:
    origins = [
        "https://e-connect-host-frontend.vercel.app",
        "https://econnect-frontend-wheat.vercel.app",
        "http://localhost:5173",
        "http://localhost:5174"
    ]

print(f"CORS Allowed Origins: {origins}")

# Add CORS middleware FIRST (order matters!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Add security headers after CORS
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    try:
        # Handle preflight requests
        if request.method == "OPTIONS":
            response = JSONResponse(content={}, status_code=200)
            origin = request.headers.get("origin", "")
            if origin in origins:
                response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, Accept, Origin, X-Requested-With"
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Max-Age"] = "3600"
            return response
            
        response = await call_next(request)
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        
        # Ensure CORS headers are always present
        origin = request.headers.get("origin")
        if origin in origins:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
            
        return response
    except Exception as e:
        # Ensure CORS headers are present even on errors
        print(f"Error in middleware: {str(e)}")
        traceback.print_exc()
        
        origin = request.headers.get("origin", "")
        response = JSONResponse(
            content={"error": "Internal server error", "details": str(e)},
            status_code=500
        )
        
        if origin in origins:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
            
        return response

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}  # userid -> WebSocket

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: str):
        self.active_connections.pop(user_id, None)

    async def send_personal_message(self, message: dict, user_id: str):
        ws = self.active_connections.get(user_id)
        if ws:
            await ws.send_json(message)

manager = ConnectionManager()


# Initialize APScheduler for background tasks
scheduler = BackgroundScheduler()

# Import notification automation
from notification_automation import (
    run_all_automated_checks, 
    check_and_notify_overdue_tasks,
    check_upcoming_deadlines,
    check_missed_attendance,
    check_pending_approvals
)

# Schedule the auto-clockout task to run daily at 9:30 PM (21:30 IST)
# This ensures employees who forget to clock out are automatically clocked out at end of day
scheduler.add_job(auto_clockout, 'cron', hour=21, minute=30, id='auto_clockout')

# Define sync wrapper functions for async tasks
def sync_check_upcoming_deadlines():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(check_upcoming_deadlines())
        loop.close()
    except Exception as e:
        print(f"Error in sync_check_upcoming_deadlines: {e}")

def sync_check_missed_attendance():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(check_missed_attendance())
        loop.close()
    except Exception as e:
        print(f"Error in sync_check_missed_attendance: {e}")

def sync_check_and_notify_overdue_tasks():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(check_and_notify_overdue_tasks())
        loop.close()
    except Exception as e:
        print(f"Error in sync_check_and_notify_overdue_tasks: {e}")

def sync_run_all_automated_checks():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_all_automated_checks())
        loop.close()
    except Exception as e:
        print(f"Error in sync_run_all_automated_checks: {e}")

def sync_check_pending_approvals():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(check_pending_approvals())
        loop.close()
    except Exception as e:
        print(f"Error in sync_check_pending_approvals: {e}")

# Schedule notification automation tasks
# Morning checks at 8:00 AM (upcoming deadlines, missed attendance)
scheduler.add_job(
    sync_check_upcoming_deadlines,
    'cron', hour=8, minute=0, id='morning_deadline_check'
)

scheduler.add_job(
    sync_check_missed_attendance,
    'cron', hour=10, minute=0, id='missed_attendance_check'
)

# Midday overdue tasks check at 12:00 PM
scheduler.add_job(
    sync_check_and_notify_overdue_tasks,
    'cron', hour=12, minute=0, id='midday_overdue_check'
)

# Evening comprehensive check at 6:00 PM
scheduler.add_job(
    sync_run_all_automated_checks,
    'cron', hour=18, minute=0, id='evening_comprehensive_check'
)

# Pending approvals check twice daily (10 AM and 3 PM)
scheduler.add_job(
    sync_check_pending_approvals,
    'cron', hour=10, minute=30, id='morning_approvals_check'
)

scheduler.add_job(
    sync_check_pending_approvals,
    'cron', hour=15, minute=0, id='afternoon_approvals_check'
)


# Add new job for daily attendance stats update
scheduler.add_job(
    update_daily_attendance_stats,
    'cron',
    hour=23,
    minute=59,  # Run at 11:59 PM daily
    id='daily_attendance_update'
)


# Add job to run attendance update at startup
scheduler.add_job(
    update_daily_attendance_stats,
    'date',  # Run once at startup
    id='startup_attendance_update'
)


# Start the scheduler
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

# Initialize task scheduler on application startup
@app.on_event("startup")
async def startup_event():
    """Initialize task deadline scheduler when the application starts"""
    try:
        task_scheduler = Mongo.setup_task_scheduler()
        if task_scheduler:
            print("✅ Task deadline monitoring system initialized")
        else:
            print("⚠️ Failed to initialize task deadline scheduler")
        
        # Log scheduled jobs
        print("\n📅 Scheduled Background Jobs:")
        print(f"  - Auto Clock-out: Daily at 9:30 PM IST")
        print(f"  - Deadline Check: Daily at 8:00 AM IST")
        print(f"  - Attendance Check: Daily at 10:00 AM IST")
        print(f"  - Overdue Tasks: Daily at 12:00 PM IST")
        print(f"  - Comprehensive Check: Daily at 6:00 PM IST")
        print(f"  - Attendance Stats Update: Daily at 11:59 PM IST\n")
    except Exception as e:
        print(f"❌ Error initializing task scheduler: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup scheduler when application shuts down"""
    try:
        if scheduler:
            scheduler.shutdown()
            print("✅ Background scheduler shut down successfully")
    except Exception as e:
        print(f"⚠️ Error shutting down scheduler: {e}")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def test_connection():
    return {"status": "Backend is connected", "timestamp": datetime.now().isoformat()}

@app.post('/addjson',dependencies=[Depends(JWTBearer())])
def Addjson(item:Item4):
    a=Mongo.Adddata(item.data,item.id,item.filename)
    return {'data':a}

@app.post('/Editjson',dependencies=[Depends(JWTBearer())])
def editjson(item:Item4):
    a=Mongo.Editdata(item.data,item.id,item.filename)
    return {'data':a}

@app.post('/deljson',dependencies=[Depends(JWTBearer())])
def Deljson(item:Item3):
    a=Mongo.deletedata(item.id)
    return{'data':'Successfully Deleted'}

@app.post('/Addcsvjson')
async def Addcsvjson(Data:Csvadd):
    a=Mongo.addcsv(name=Data.name,data=Data.data,id=Data.fileid)
    return a

@app.post('/Getcsvjson')
async def Getcsvjson(item:Item3):
    a=Mongo.Getcsvdata(item.id)
    return a

@app.post('/Updatecsvjson')
async def Updatecsvjson(item:Csvedit):
    print(item)
    a=Mongo.Updatecsv(data=item.data,id=item.id,fileid=item.fileid,name=item.name)
    return a

@app.post('/deletecsvjson')
async def Deletecsv(item:Csvdel):
    a=Mongo.Deletecsv(fileid=item.fileid,id=item.id )
    return a

@app.post("/signup")
def Signup(item: Item):
    jwt=Mongo.Signup(item.email,item.password,item.name)
    print(jwt)
    return jwt

@app.post("/signin")
def Signup(item: Item2):
    c=Mongo.signin(item.email,item.password)
    return c

# Google Signin
@app.post("/Gsignin")
async def Signup(item: Item5):
    try:
        jwt = Mongo.Gsignin(item.client_name, item.email)
        print("Google Signin Response:", jwt)
        
        # Ensure the response is JSON serializable
        # Convert to JSON string using bson json_util, then parse back
        json_str = json_util.dumps(jwt)
        json_data = json.loads(json_str)
        
        return JSONResponse(content=json_data, status_code=200)
    except HTTPException as http_exc:
        # Re-raise HTTPException to be handled by FastAPI
        raise http_exc
    except Exception as e:
        print(f"Error in /Gsignin: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Userid
@app.post('/id',dependencies=[Depends(JWTBearer())])
def userbyid(item:Item3):
    a=Mongo.Userbyid(item.id)
    return {'data': a}

# Time Management
@app.post('/Clockin')
def clockin(Data: CT):
    from datetime import datetime
    import pytz
    # Always use full datetime string for clock-in
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    # If Data.current_time is provided, try to parse it, else use now
    time = getattr(Data, 'current_time', None)
    if time:
        try:
            # Try to parse as datetime string
            clockin_dt = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
            time_str = clockin_dt.isoformat()
        except Exception:
            # Fallback: treat as time only, combine with today
            time_str = now.isoformat()
    else:
        time_str = now.isoformat()
    result = Mongo.Clockin(userid=Data.userid, name=Data.name, time=time_str)
    return {"message": result}

@app.post('/Clockout')
def clockout(Data: CT):
    from datetime import datetime
    import pytz
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    time = getattr(Data, 'current_time', None)
    if time:
        try:
            clockout_dt = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
            time_str = clockout_dt.isoformat()
        except Exception:
            time_str = now.isoformat()
    else:
        time_str = now.isoformat()
    result = Mongo.Clockout(userid=Data.userid, name=Data.name, time=time_str)
    return {"message": result}

@app.post('/PreviousDayClockout')
def previous_day_clockout(Data: CT):
    result = PreviousDayClockout(userid=Data.userid, name=Data.name)
    return {"message": result}

# Clockin Details
@app.get("/clock-records/{userid}")  
async def get_clock_records(userid: str = Path(..., title="The name of the user whose clock records you want to fetch")):
    try:
        clock_records = attendance_details(userid)
        return {"clock_records": clock_records}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Admin Dashboard Attendance
@app.get("/attendance/")
async def fetch_attendance_by_date(date: str = Query(None)):
    try:
        if date:
            # If date is provided, filter by that date
            attendance_data = get_attendance_by_date()
            # Filter by date if needed (the frontend sends date parameter but we return all for now)
            # You can add date filtering logic here if needed
        else:
            # If no date provided, return all attendance data
            attendance_data = get_attendance_by_date()
        
        if not attendance_data:
            return {"attendance": []}
        
        return {"attendance": attendance_data}
    except Exception as e:
        print(f"Error fetching attendance: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching attendance data: {str(e)}")


# Employee ID
@app.get("/get_EmployeeId/{name}")
async def get_employee_id(name: str = Path(..., title="The username of the user")):
    try:
        employee_id = get_employee_id_from_db(name)
        if employee_id:
            return {"Employee_ID": employee_id}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(500, str(e))


#Leave-request
@app.post('/leave-request')
async def leave_request(item: Item6):
    try:
        
        print(item.selectedDate)
        print(item.requestDate)

        # Add request time in the desired timezone
        time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I:%M:%S %p")

        # Store the leave request in MongoDB
        result = Mongo.store_leave_request(
            item.userid,
            item.employeeName,
            time,
            item.leaveType,
            item.selectedDate,  # Formatted as DD-MM-YYYY
            item.requestDate,  # Formatted as DD-MM-YYYY
            item.reason,
        )

        # Check if result is a conflict or other business logic issue
        if isinstance(result, str):
            if "Conflict" in result or "already has" in result:
                # This is a business logic conflict, not a request error
                return {
                    "success": False,
                    "status": "conflict",
                    "message": "Request processed successfully, but a scheduling conflict was detected.",
                    "details": result,
                    "suggestion": "Please select a different date or check your existing requests."
                }
            elif result == "Leave request stored successfully":
                # Success case - notify employee and appropriate approver
                try:
                    # 1. Notify employee about successful submission
                    await notify_leave_submitted(
                        userid=item.userid,
                        leave_type=item.leaveType,
                        leave_id=None
                    )
                    print(f"✅ Employee notification sent for leave submission")
                    
                    # 2. Check if the user is a manager and send appropriate notifications
                    user_position = await Mongo.get_user_position(item.userid)
                    
                    if user_position == "Manager":
                        # Manager leave request - notify admin
                        admin_ids = await Mongo.get_admin_user_ids()
                        if admin_ids:
                            await Mongo.notify_admin_manager_leave_request(
                                manager_name=item.employeeName,
                                manager_id=item.userid,
                                leave_type=item.leaveType,
                                leave_date=item.selectedDate,
                                leave_id=None
                            )
                            print(f"✅ Admin notification sent for manager leave request")
                        else:
                            print(f"⚠️ No admin found, skipping admin notification")
                    else:
                        # Regular employee leave request - notify manager
                        manager_id = await Mongo.get_user_manager_id(item.userid)
                        if manager_id:
                            await Mongo.notify_manager_leave_request(
                                employee_name=item.employeeName,
                                employee_id=item.userid,
                                leave_type=item.leaveType,
                                leave_date=item.selectedDate,
                                manager_id=manager_id,
                                leave_id=None
                            )
                            print(f"✅ Manager notification sent for employee leave approval request")
                        else:
                            print(f"⚠️ No manager found for user {item.userid}, skipping manager notification")
                        
                except Exception as notification_error:
                    print(f"⚠️ Notification error: {notification_error}")
                
                return {
                    "success": True,
                    "status": "submitted",
                    "message": "Leave request submitted successfully",
                    "details": result
                }
            else:
                # Other validation errors (Sunday, invalid dates, etc.)
                return {
                    "success": False,
                    "status": "validation_error",
                    "message": "Request validation failed",
                    "details": result,
                    "suggestion": "Please check your request details and try again."
                }

        return {"message": "Leave request processed", "result": result}
    except Exception as e:
        print(f"❌ Error in leave request: {e}")
        # Only return 500 for actual server errors, not business logic issues
        return {
            "success": False,
            "status": "error",
            "message": "An unexpected error occurred while processing your request",
            "details": str(e),
            "suggestion": "Please try again later or contact support if the issue persists."
        }

@app.post('/Bonus-leave-request')
async def bonus_leave_request(item: Item9):
    try:
        # Get the current time in IST
        time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I:%M:%S %p")

        # Store bonus leave request
        result = store_sunday_request(
            item.userid,
            item.employeeName,
            time,
            item.leaveType,
            item.selectedDate,  # Formatted as DD-MM-YYYY
            item.reason,
            item.requestDate,  # Formatted as DD-MM-YYYY
        )

        if result and result != "No bonus leave available" and "Conflict" not in str(result):
            # For successful requests, create notifications
            try:
                # 1. Notify employee about successful submission
                await Mongo.notify_leave_submitted(
                    userid=item.userid,
                    leave_type=item.leaveType,
                    leave_id=None  # No specific ID for bonus leave
                )
                print(f"✅ Employee notification sent for bonus leave submission")
                
                # 2. Check if the user is a manager and send appropriate notifications
                user_position = await Mongo.get_user_position(item.userid)
                
                if user_position == "Manager":
                    # Manager bonus leave request - notify admin
                    admin_ids = await Mongo.get_admin_user_ids()
                    if admin_ids:
                        await Mongo.notify_admin_manager_leave_request(
                            manager_name=item.employeeName,
                            manager_id=item.userid,
                            leave_type=item.leaveType,
                            leave_date=item.selectedDate,
                            leave_id=None
                        )
                        print(f"✅ Admin notification sent for manager bonus leave request")
                    else:
                        print(f"⚠️ No admin found, skipping admin notification")
                else:
                    # Regular employee bonus leave request - notify manager
                    manager_id = await Mongo.get_user_manager_id(item.userid)
                    if manager_id:
                        await Mongo.notify_manager_leave_request(
                            employee_name=item.employeeName,
                            employee_id=item.userid,
                            leave_type=item.leaveType,
                            leave_date=item.selectedDate,
                            manager_id=manager_id,
                            leave_id=None
                        )
                        print(f"✅ Manager notification sent for employee bonus leave approval request")
                    else:
                        print(f"⚠️ No manager found for user {item.userid}, skipping manager notification")
                
            except Exception as notification_error:
                print(f"⚠️ Notification error: {notification_error}")

        return {"message": "Bonus leave request processed", "result": result}
    except Exception as e:
        print(f"❌ Error in bonus leave request: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Leave History
@app.get("/leave-History/{userid}/") 
async def get_leave_History(userid: str = Path(..., title="The userid of the user")):
    try:
       
        leave_history = Mongo.normal_leave_details(userid)
        return {"leave_history" : leave_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/all_users_leave_requests/") 
async def fetch_user_leave_requests(selectedOption: str = Query(..., alias="selectedOption")):
    print(f"DEBUG: /all_users_leave_requests endpoint called - selectedOption: {selectedOption}")
    user_leave_requests = get_user_leave_requests(selectedOption) # HR sees recommended
    print(f"DEBUG: Returning {len(user_leave_requests) if user_leave_requests else 0} requests")
    return {"user_leave_requests": user_leave_requests or []}

# Admin Page To Fetch Only Managers Leave Requests
@app.get("/manager_leave_requests/")
async def fetch_manager_leave_requests(selectedOption: str = Query(..., alias="selectedOption")):
    print(f"DEBUG: /manager_leave_requests endpoint called - selectedOption: {selectedOption}")
    user_leave_requests = get_manager_leave_requests(selectedOption) # Admin sees manager requests
    print(f"DEBUG: Returning {len(user_leave_requests) if user_leave_requests else 0} requests")
    return {"user_leave_requests": user_leave_requests or []}

#TL,Manager Page To Fetch Only Users Leave Requests Under Their Team
@app.get("/only_users_leave_requests/")
async def fetch_users_leave_requests(selectedOption: str = Query(..., alias="selectedOption"), TL: str = Query(..., alias="TL")):
    print(f"DEBUG: Endpoint called - selectedOption: {selectedOption}, TL: {TL}")
    user_leave_requests = get_only_user_leave_requests(selectedOption, TL) # Manager sees new requests
    print(f"DEBUG: Returning {len(user_leave_requests) if user_leave_requests else 0} requests")
    return {"user_leave_requests": user_leave_requests or []}

#HR page
@app.get("/leave_update_reminder")
async def fetch_pending_leave():
    result = leave_update_notification()
    return result

#Admin page
@app.get("/managers_leave_recommend_reminder")
async def fetch_pending_leave():
    result = managers_leave_recommend_notification()
    return result

#TL page
@app.get("/leave_update_reminder")
async def fetch_pending_leave(TL: str = Query(..., alias="TL")):
    result = users_leave_recommend_notification(TL)
    return result

# HR Page Leave Responses
@app.put("/updated_user_leave_requests")
async def updated_user_leave_requests_status(leave_id: str = Form(...), status: str = Form(...)):
    try:
        response = updated_user_leave_requests_status_in_mongo(leave_id, status)
        
        # Create notification for leave status update
        if response and "userid" in response:
            # Properly handle different status values
            status_lower = status.lower()
            if status_lower == "approved":
                action = "Approved"
                priority = "high"
            elif status_lower in ["rejected", "reject"]:
                action = "Rejected"
                priority = "high"
            elif status_lower in ["recommended", "recommend"]:
                action = "Recommended"
                priority = "medium"
            else:
                action = status  # Use the original status for any other case
                priority = "medium"
            
            create_leave_notification(
                userid=response["userid"],
                leave_type=response.get("leave_type", "Leave"),
                action=action,
                leave_id=leave_id,
                priority=priority
            )
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   
# Admin And TL Leave Recommendation Responses
@app.put("/recommend_users_leave_requests")
async def recommend_managers_leave_requests_status(leave_id: str = Form(...), status: str = Form(...)):
    try:
        response = recommend_manager_leave_requests_status_in_mongo(leave_id, status)
        
        # Create notification for leave recommendation
        if response and "userid" in response:
            action = "Recommended" if status.lower() in ["recommended", "recommend"] else "Not Recommended"
            recommender_name = response.get("recommender_name", "Admin")
            
            # Notify the employee about the recommendation
            create_leave_notification(
                userid=response["userid"],
                leave_type=response.get("leave_type", "Leave"),
                action=action,
                leave_id=leave_id,
                priority="medium",
                manager_name=recommender_name
            )
            
            # If the leave is recommended, also notify HR for final approval
            if status.lower() in ["recommended", "recommend"]:
                try:
                    # Get employee details for HR notification
                    employee_name = response.get("employee_name", "Unknown Employee")
                    leave_type = response.get("leave_type", "Leave")
                    leave_date = response.get("leave_date", "Unknown Date")
                    recommender_name = response.get("recommender_name", "Manager/Admin")
                    
                    await Mongo.notify_hr_recommended_leave(
                        employee_name=employee_name,
                        employee_id=response["userid"],
                        leave_type=leave_type,
                        leave_date=leave_date,
                        recommended_by=recommender_name,
                        leave_id=leave_id
                    )
                    print(f"✅ HR notification sent for recommended leave: {employee_name}")
                    
                except Exception as hr_notification_error:
                    print(f"⚠️ Error sending HR notification: {hr_notification_error}")
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_leave_request")
async def delete_leave_request(item:DeleteLeave):
    try:
        def parse_date(date_str):
            try:
                # Attempt to parse as full timestamp with time and microseconds
                return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
            except ValueError:
                try:
                    # Fallback to parsing as date-only
                    return datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    raise ValueError(f"Invalid date format: {date_str}")

        # Parse selectedDate and requestDate
        selected_date_str = item.fromDate.rstrip('Z')
        request_date_str = item.requestDate.rstrip('Z')
        selected_date = parse_date(selected_date_str)
        request_date = parse_date(request_date_str)

        # Localize to UTC
        selected_date_utc = pytz.utc.localize(selected_date)
        request_date_utc = pytz.utc.localize(request_date)


        result = delete_leave(item.userid, selected_date_utc, request_date_utc, item.leavetype)
        return result


    except Exception as e:
        raise HTTPException(400, str(e))




# Remote Work Request

# TL Page Remote Work Requests (Manager view)
@app.get("/TL_page_remote_work_requests")
async def get_TL_page_remote_work_requests(TL: str = Query(..., alias="TL"), show_processed: bool = Query(False, alias="show_processed")):
    """Get TL page remote work requests with history for a given Team Lead (Manager)"""
    try:
        from Mongo import get_TL_page_remote_work_requests_with_history
        result = get_TL_page_remote_work_requests_with_history(TL, show_processed)
        return {"remote_work_requests": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/remote-work-request")
async def remote_work_request(request: RemoteWorkRequest):
    try:
        # Add request time in IST
        time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I:%M:%S %p")


        result = Mongo.store_remote_work_request(
            request.userid,
            request.employeeName,
            time,
            request.fromDate,
            request.toDate,
            request.requestDate,
            request.reason,
            request.ip
        )
        
        # Check if result is a dictionary (success) or string (error/conflict)
        if isinstance(result, dict) and result.get("success"):
            # Success case - notify employee and manager
            try:
                wfh_id = result.get("wfh_id")
                from_date = result.get("from_date")
                to_date = result.get("to_date")
                
                # 1. Notify employee about successful submission
                await Mongo.notify_wfh_submitted(
                    userid=request.userid,
                    request_date=from_date,
                    wfh_id=wfh_id
                )
                print(f"✅ Employee notification sent for WFH submission with ID: {wfh_id}")
                
                # 2. Check if user is a manager and handle notifications accordingly
                user = Mongo.Users.find_one({"_id": Mongo.ObjectId(request.userid)})
                if user and user.get("position") == "Manager":
                    # If manager is submitting WFH, notify admin
                    try:
                        await Mongo.notify_admin_manager_wfh_request(
                            manager_name=request.employeeName,
                            manager_id=request.userid,
                            request_date_from=from_date,
                            request_date_to=to_date,
                            wfh_id=wfh_id
                        )
                        print(f"✅ Admin notification sent for manager WFH request")
                    except Exception as admin_notification_error:
                        print(f"⚠️ Admin notification error: {admin_notification_error}")
                else:
                    # Regular employee - notify their manager using improved notification system
                    manager_id = await Mongo.get_user_manager_id(request.userid)
                    if manager_id:
                        # Import the improved notification function
                        from notification_automation import notify_wfh_submitted_to_manager
                        await notify_wfh_submitted_to_manager(
                            employee_name=request.employeeName,
                            employee_id=request.userid,
                            request_date_from=from_date,
                            request_date_to=to_date,
                            manager_id=manager_id,
                            wfh_id=wfh_id
                        )
                        print(f"✅ Manager notification sent for WFH approval request")
                    else:
                        print(f"⚠️ No manager found for user {request.userid}, skipping manager notification")
                    
            except Exception as notification_error:
                print(f"⚠️ Notification error: {notification_error}")
                import traceback
                traceback.print_exc()
            
            return {
                "success": True,
                "status": "submitted",
                "message": result.get("message", "Remote work request submitted successfully"),
                "details": result,
                "wfh_id": wfh_id
            }
        elif isinstance(result, str):
            if "Conflict" in result or "already has" in result:
                # This is a business logic conflict, not a request error
                return {
                    "success": False,
                    "status": "conflict",
                    "message": "Request processed successfully, but a scheduling conflict was detected.",
                    "details": result,
                    "suggestion": "Please select different dates or check your existing requests."
                }
            elif "successfully" in result:
                # Old format success - fallback
                try:
                    # 1. Notify employee about successful submission
                    await Mongo.notify_wfh_submitted(
                        userid=request.userid,
                        request_date=request.fromDate,
                        wfh_id=None
                    )
                    print(f"✅ Employee notification sent for WFH submission (fallback)")
                    
                    # 2. Check if user is a manager and handle notifications accordingly
                    user = Mongo.Users.find_one({"_id": Mongo.ObjectId(request.userid)})
                    if user and user.get("position") == "Manager":
                        # If manager is submitting WFH, notify admin
                        try:
                            await Mongo.notify_admin_manager_wfh_request(
                                manager_name=request.employeeName,
                                manager_id=request.userid,
                                request_date_from=request.fromDate,
                                request_date_to=request.toDate,
                                wfh_id=None
                            )
                            print(f"✅ Admin notification sent for manager WFH request (fallback)")
                        except Exception as admin_notification_error:
                            print(f"⚠️ Admin notification error: {admin_notification_error}")
                    else:
                        # Regular employee - notify their manager
                        manager_id = await Mongo.get_user_manager_id(request.userid)
                        if manager_id:
                            await Mongo.notify_manager_wfh_request(
                                employee_name=request.employeeName,
                                employee_id=request.userid,
                                request_date_from=request.fromDate,
                                request_date_to=request.toDate,
                                manager_id=manager_id,
                                wfh_id=None
                            )
                            print(f"✅ Manager notification sent for WFH approval request")
                        else:
                            print(f"⚠️ No manager found for user {request.userid}, skipping manager notification")
                        
                except Exception as notification_error:
                    print(f"⚠️ Notification error: {notification_error}")
                
                return {
                    "success": True,
                    "status": "submitted",
                    "message": "Remote work request submitted successfully",
                    "details": result
                }
            else:
                # Other validation errors (Sunday, too many days, etc.)
                return {
                    "success": False,
                    "status": "validation_error",
                    "message": "Request validation failed",
                    "details": result,
                    "suggestion": "Please check your request details and try again."
                }
        
        return {"message": "WFH request processed", "result": result}
    except Exception as e:
        print(f"❌ Error in WFH request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

  

# Remote Work History    
@app.get("/Remote-History/{userid}/") 
async def get_Remote_History(userid:str = Path(..., title="The name of the user whose Remote History you want to fetch")):
    try:
        Remote_History = Remote_History_Details(userid)
        return{"Remote_History": Remote_History}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

# HR Page User Remote Work Requests
@app.get("/remote_work_requests")
async def fetch_remote_work_requests():
    remote_work_requests = get_remote_work_requests()
    return {"remote_work_requests": remote_work_requests}

# Admin Page User Remote Work Requests
@app.get("/admin_page_remote_work_requests")
async def fetch_remote_work_requests():
    remote_work_requests = get_admin_page_remote_work_requests()
    return {"remote_work_requests": remote_work_requests}

async def fetch_remote_work_requests(TL: str = Query(..., alias="TL")):
    remote_work_requests = get_remote_work_requests(TL)
    return {"remote_work_requests": remote_work_requests}


# HR Remote Work Responses
@app.put("/update_remote_work_requests")
async def update_remote_work_request_status(userid: str = Form(...), status: str = Form(...), id: str = Form(...)):
    try:
        updated = update_remote_work_request_status_in_mongo(userid, status, id)
        if updated:
            # Send notification to the user about the status update
            try:
                wfh_request = Mongo.RemoteWork.find_one({"_id": Mongo.ObjectId(id)})
                if wfh_request:
                    from_date = wfh_request.get("fromDate")
                    from_date_str = from_date.strftime("%d-%m-%Y") if from_date else None
                    
                    if status.lower() == "approved":
                        # Import the improved approval notification function
                        from notification_automation import notify_wfh_approved_to_employee
                        # Get employee name for better notification
                        employee_name = wfh_request.get("employeeName", "Employee")
                        to_date = wfh_request.get("toDate")
                        to_date_str = to_date.strftime("%d-%m-%Y") if to_date else from_date_str
                        
                        await notify_wfh_approved_to_employee(
                            userid=userid,
                            employee_name=employee_name,
                            request_date_from=from_date_str,
                            request_date_to=to_date_str,
                            approved_by="HR",
                            wfh_id=id
                        )
                        print(f"✅ WFH approved notification sent to user {userid}")
                    elif status.lower() == "rejected":
                        # Import the improved rejection notification function  
                        from notification_automation import notify_wfh_rejected_to_employee
                        # Get employee name for better notification
                        employee_name = wfh_request.get("employeeName", "Employee")
                        to_date = wfh_request.get("toDate")
                        to_date_str = to_date.strftime("%d-%m-%Y") if to_date else from_date_str
                        
                        await notify_wfh_rejected_to_employee(
                            userid=userid,
                            employee_name=employee_name,
                            request_date_from=from_date_str,
                            request_date_to=to_date_str,
                            rejected_by="HR",
                            reason="Not specified",
                            wfh_id=id
                        )
                        print(f"✅ WFH rejected notification sent to user {userid}")
            except Exception as notification_error:
                print(f"⚠️ Notification error: {notification_error}")
            
            return {"message": "Status updated successfully"}
        else:
            return {"message": "Failed to update status"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# HR Remote Work Responses
@app.put("/recommend_remote_work_requests")
async def update_remote_work_request_status(userid: str = Form(...), status: str = Form(...), id: str = Form(...)):
    try:
        print(f"WFH recommendation update - User: {userid}, Status: {status}, ID: {id}")
        updated = update_remote_work_request_recommend_in_mongo(userid, status, id)
        if updated and status.lower() == "recommend":
            # Send notification to HR when WFH is recommended
            try:
                wfh_request = Mongo.RemoteWork.find_one({"_id": Mongo.ObjectId(id)})
                if wfh_request:
                    employee_name = wfh_request.get("employeeName", "Unknown Employee")
                    employee_id = wfh_request.get("userid")  # This is the actual employee ID
                    from_date = wfh_request.get("fromDate")
                    to_date = wfh_request.get("toDate")
                    from_date_str = from_date.strftime("%d-%m-%Y") if from_date else "Unknown Date"
                    to_date_str = to_date.strftime("%d-%m-%Y") if to_date else "Unknown Date"
                    
                    # Get the employee's manager name (who is doing the recommendation)
                    employee = Mongo.Users.find_one({"_id": Mongo.ObjectId(employee_id)})
                    manager_name = employee.get("TL", "Manager") if employee else "Manager"
                    
                    # Import the improved HR notification function
                    from notification_automation import notify_wfh_recommended_to_hr
                    await notify_wfh_recommended_to_hr(
                        employee_name=employee_name,
                        employee_id=employee_id,
                        request_date_from=from_date_str,
                        request_date_to=to_date_str,
                        recommended_by=manager_name,
                        wfh_id=id
                    )
                    print(f"✅ HR notification sent for recommended WFH: {employee_name} (recommended by {manager_name})")
                    
                else:
                    print(f"⚠️ WFH request not found for ID: {id}")
            except Exception as notification_error:
                print(f"⚠️ HR notification error: {notification_error}")
        
        print(id)
        updated = update_remote_work_request_recommend_in_mongo(userid, status, id)
        if updated:
            return {"message": "Recommend status updated successfully"}
        else:
            return {"message": "Failed to update recommend status"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   
# Admin Page User Leave History
@app.get("/approved-leave-history/{name}/")  # Also handle requests with trailing slash
def get_leave_history(name: str = Path(..., title= "Team lead name")):
    leave_history = get_approved_leave_history(name)
    return {"leave_history": leave_history}

# Admin ID
@app.post('/id',dependencies=[Depends(JWTBearer())])
def adminid(item:Item3):
    a=Mongo.adminbyid(item.id)
    return {'data': a}

@app.post("/admin_signup")
def adminid_Signup(item: Item):
    jwt=Mongo.admin_Signup(item.email,item.password,item.name,item.phone,item.position,item.date_of_joining)
    return jwt

@app.post("/admin_signin")
def admin_Signup(item: Item2):
    checkuser = admin.find_one({'email': item.email})
    jwt = Mongo.admin_signin(checkuser, item.password, item.email)
    email = jwt.get('email')
    admin_info = get_admin_info(email)
    print(jwt)
    return {
        "jwt": jwt,
        "Name": admin_info.get('name'),
        "Email": admin_info.get('email'),
        "Phone no": admin_info.get('phone'),
        "Position": admin_info.get('position'),
        "Date of joining": admin_info.get('date_of_joining')
    }


# Admin Signin
@app.post("/admin_Gsignin")
def admin_signup(item: Item5):
    try:
        print(item.dict())
        jwt = Mongo.admin_Gsignin(item.client_name, item.email)
        print("Admin Google Signin Response:", jwt)
        
        # Ensure the response is JSON serializable
        json_str = json_util.dumps(jwt)
        json_data = json.loads(json_str)
        
        return JSONResponse(content=json_data, status_code=200)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        print(f"Error in /admin_Gsignin: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")




from datetime import datetime
import pytz
from fastapi import HTTPException

def parse_and_format_date(date_str):
    """Parses various date formats and converts them to DD-MM-YYYY format."""
    if not date_str:
        return None


    date_str = date_str.rstrip('Z')  # Remove 'Z' if present
    formats = ["%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"]  # Possible formats


    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime("%d-%m-%Y")  # Convert to DD-MM-YYYY
        except ValueError:
            continue  # Try next format if parsing fails


    raise ValueError(f"Invalid date format: {date_str}")


@app.post('/Other-leave-request')
async def other_leave_request(item: Item7):
    try:
        # Add request time in the desired timezone
        time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%I:%M:%S %p")

        # Store the leave request in MongoDB
        result = store_Other_leave_request(
            item.userid,
            item.employeeName,
            time,  # Use the generated time
            item.leaveType,
            item.selectedDate,  # Formatted as DD-MM-YYYY
            item.ToDate,  # Formatted as DD-MM-YYYY
            item.requestDate,  # Formatted as DD-MM-YYYY
            item.reason,
        )

        # Check if result is a conflict or other business logic issue
        if isinstance(result, str):
            if "Conflict" in result or "already has" in result:
                # This is a business logic conflict, not a request error
                return {
                    "success": False,
                    "status": "conflict",
                    "message": "Request processed successfully, but a scheduling conflict was detected.",
                    "details": result,
                    "suggestion": "Please select different dates or check your existing requests."
                }
            elif result == "Leave request stored successfully":
                # Success case - notify employee and manager
                try:
                    # 1. Notify employee about successful submission
                    await Mongo.notify_leave_submitted(
                        userid=item.userid,
                        leave_type=item.leaveType,
                        leave_id=None  # No specific ID for other leave
                    )
                    print(f"✅ Employee notification sent for other leave submission")
                    
                    # 2. Check if the user is a manager and send appropriate notifications
                    user_position = await Mongo.get_user_position(item.userid)
                    
                    if user_position == "Manager":
                        # Manager other leave request - notify admin
                        admin_ids = await Mongo.get_admin_user_ids()
                        if admin_ids:
                            date_range = f"{item.selectedDate} to {item.ToDate}" if item.selectedDate != item.ToDate else item.selectedDate
                            await Mongo.notify_admin_manager_leave_request(
                                manager_name=item.employeeName,
                                manager_id=item.userid,
                                leave_type=item.leaveType,
                                leave_date=date_range,
                                leave_id=None
                            )
                            print(f"✅ Admin notification sent for manager other leave request")
                        else:
                            print(f"⚠️ No admin found, skipping admin notification")
                    else:
                        # Regular employee other leave request - notify manager
                        manager_id = await Mongo.get_user_manager_id(item.userid)
                        if manager_id:
                            date_range = f"{item.selectedDate} to {item.ToDate}" if item.selectedDate != item.ToDate else item.selectedDate
                            await Mongo.notify_manager_leave_request(
                                employee_name=item.employeeName,
                                employee_id=item.userid,
                                leave_type=item.leaveType,
                                leave_date=date_range,
                                manager_id=manager_id,
                                leave_id=None
                            )
                            print(f"✅ Manager notification sent for employee other leave approval request")
                        else:
                            print(f"⚠️ No manager found for user {item.userid}, skipping manager notification")
                        
                except Exception as notification_error:
                    print(f"⚠️ Notification error: {notification_error}")
                
                return {
                    "success": True,
                    "status": "submitted",
                    "message": "Other leave request submitted successfully",
                    "details": result
                }
            else:
                # Other validation errors (Sunday, too many days, etc.)
                return {
                    "success": False,
                    "status": "validation_error",
                    "message": "Request validation failed",
                    "details": result,
                    "suggestion": "Please check your request details and try again."
                }

        return {"message": "Leave request processed", "result": result}
    except Exception as e:
        print(f"❌ Error in other leave request: {e}")
        raise HTTPException(400, str(e))
    
@app.post('/Permission-request')
async def permission_request(item: Item8):
    try:
        result = store_Permission_request(
                item.userid,
                item.employeeName,
                item.time,
                item.leaveType,
                item.selectedDate,
                item.requestDate,
                item.timeSlot,
                item.reason,
            )

        # Check if result is a conflict or other business logic issue
        if isinstance(result, str):
            if "Conflict" in result or "already has" in result:
                # This is a business logic conflict, not a request error
                return {
                    "success": False,
                    "status": "conflict",
                    "message": "Request processed successfully, but a scheduling conflict was detected.",
                    "details": result,
                    "suggestion": "Please select different dates or check your existing requests."
                }
            elif result == "Leave request stored successfully":
                # Success case - notify employee and manager
                try:
                    # 1. Notify employee about successful submission
                    await Mongo.notify_leave_submitted(
                        userid=item.userid,
                        leave_type=item.leaveType,
                        leave_id=None  # No specific ID for permission
                    )
                    print(f"✅ Employee notification sent for permission submission")
                    
                    # 2. Check if the user is a manager and send appropriate notifications
                    user_position = await Mongo.get_user_position(item.userid)
                    
                    if user_position == "Manager":
                        # Manager permission request - notify admin
                        admin_ids = await Mongo.get_admin_user_ids()
                        if admin_ids:
                            permission_details = f"{item.selectedDate} ({item.timeSlot})"
                            await Mongo.notify_admin_manager_leave_request(
                                manager_name=item.employeeName,
                                manager_id=item.userid,
                                leave_type=item.leaveType,
                                leave_date=permission_details,
                                leave_id=None
                            )
                            print(f"✅ Admin notification sent for manager permission request")
                        else:
                            print(f"⚠️ No admin found, skipping admin notification")
                    else:
                        # Regular employee permission request - notify manager
                        manager_id = await Mongo.get_user_manager_id(item.userid)
                        if manager_id:
                            permission_details = f"{item.selectedDate} ({item.timeSlot})"
                            await Mongo.notify_manager_leave_request(
                                employee_name=item.employeeName,
                                employee_id=item.userid,
                                leave_type=item.leaveType,
                                leave_date=permission_details,
                                manager_id=manager_id,
                                leave_id=None
                            )
                            print(f"✅ Manager notification sent for employee permission approval request")
                        else:
                            print(f"⚠️ No manager found for user {item.userid}, skipping manager notification")
                        
                except Exception as notification_error:
                    print(f"⚠️ Notification error: {notification_error}")
                
                return {
                    "success": True,
                    "status": "submitted",
                    "message": "Permission request submitted successfully",
                    "details": result
                }
            else:
                # Other validation errors (Sunday, too many days, etc.)
                return {
                    "success": False,
                    "status": "validation_error",
                    "message": "Request validation failed",
                    "details": result,
                    "suggestion": "Please check your request details and try again."
                }

        return {"message": "Permission request processed", "result": result}
    except Exception as e:
        print(f"❌ Error in permission request: {e}")
        raise HTTPException(400, str(e))
   
@app.get("/Other-leave-history/{userid}/") 
async def get_other_leave_history(userid: str = Path(..., title="The ID of the user")):
    try:
        # Call your function to get the leave history for the specified user
        leave_history = Otherleave_History_Details(userid)

        # Return the leave history
        return {"leave_history": leave_history}
    except Exception as e:
        # If an exception occurs, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail=str(e))
   
@app.get("/Permission-history/{userid}/")  # Also handle requests with trailing slash
async def get_Permission_history(userid: str = Path(..., title="The ID of the user")):
    try:
        # Call your function to get the leave history for the specified user
        leave_history = Permission_History_Details(userid)

        # Return the leave history
        return {"leave_history": leave_history}
    except Exception as e:
        # If an exception occurs, return a 500 Internal Server Error
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/leave_details/user/{userid}/")  # Also handle requests with trailing slash
async def get_user_leave_details(
    userid: str,
    status_filter: str = Query("All", alias="statusFilter"),
    leave_type_filter: str = Query("All", alias="leaveTypeFilter")
):
    """Get all leave details for a specific user"""
    try:
        # Base query
        match_conditions = {"userid": userid}

        # Status filter
        if status_filter and status_filter != "All":
            if status_filter == "Pending":
                # Match leaves with no status or status == "Pending"
                match_conditions["$or"] = [
                    {"status": {"$exists": False}},
                    {"status": "Pending"}
                ]
            else:
                match_conditions["status"] = status_filter

        # Leave type filter
        if leave_type_filter and leave_type_filter != "All":
            match_conditions["leaveType"] = leave_type_filter

        # Fetch data from MongoDB
        leave_details = list(Leave.find(match_conditions))

        # Convert ObjectId to string & format dates safely
        for leave in leave_details:
            leave["_id"] = str(leave["_id"])
            for date_field in ["selectedDate", "requestDate", "ToDate"]:
                if leave.get(date_field) and hasattr(leave[date_field], "strftime"):
                    leave[date_field] = leave[date_field].strftime("%d-%m-%Y")

        return {"leave_details": leave_details}

    except Exception as e:
        # Return proper 500 error
        raise HTTPException(status_code=500, detail=str(e))


# ============== REMOTE WORK ENDPOINTS ==============
@app.get("/remote_work_details/user/{userid}/")  # Also handle requests with trailing slash
async def get_user_remote_work_details(
    userid: str,
    status_filter: str = Query("All", alias="statusFilter")
):
    """Get all remote work details for a specific user"""
    try:
        match_conditions = {"userid": userid}
        
        if status_filter and status_filter != "All":
            if status_filter == "Pending":
                match_conditions["status"] = {"$exists": False}
                match_conditions["Recommendation"] = {"$exists": False}
            elif status_filter == "Recommended":
                match_conditions["Recommendation"] = "Recommend"
            else:
                match_conditions["status"] = status_filter
        
        remote_work_details = list(RemoteWork.find(match_conditions))
        
        # Convert ObjectId and format dates
        for remote_work in remote_work_details:
            remote_work["_id"] = str(remote_work["_id"])
            if "fromDate" in remote_work and remote_work["fromDate"]:
                remote_work["fromDate"] = remote_work["fromDate"].strftime("%d-%m-%Y")
            if "toDate" in remote_work and remote_work["toDate"]:
                remote_work["toDate"] = remote_work["toDate"].strftime("%d-%m-%Y")
            if "requestDate" in remote_work and remote_work["requestDate"]:
                remote_work["requestDate"] = remote_work["requestDate"].strftime("%d-%m-%Y")
        
        return {"remote_work_details": remote_work_details}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========all
@app.get("/manager/leave_details/{user_id}")
async def get_manager_team_leave_details(
    user_id: str,
    statusFilter: Optional[str] = Query(None),
    leaveTypeFilter: Optional[str] = Query(None),
    departmentFilter: Optional[str] = Query(None)
):
    """Get leave details for team members under a specific manager"""
    try:
        # First, verify the manager exists and get their info
        manager = Users.find_one({"_id": ObjectId(user_id)})
        if not manager:
            raise HTTPException(status_code=404, detail="Manager not found")
        
        manager_name = manager.get("name")
        if not manager_name:
            raise HTTPException(status_code=400, detail="Manager name not found")
        
        # Build the aggregation pipeline
        pipeline = []
        
        # Convert userid to ObjectId if it's a string
        pipeline.append({
            "$addFields": {
                "userid_as_objectid": {
                    "$cond": {
                        "if": {"$eq": [{"$type": "$userid"}, "objectId"]},
                        "then": "$userid",
                        "else": {"$toObjectId": "$userid"}
                    }
                }
            }
        })
        
        # Join with Users collection
        pipeline.append({
            "$lookup": {
                "from": "Users",
                "localField": "userid_as_objectid",
                "foreignField": "_id",
                "as": "user_info"
            }
        })
        
        # Unwind the user_info array
        pipeline.append({"$unwind": "$user_info"})
        
        # Filter to only show team members under this manager
        base_match = {
            "user_info.TL": manager_name,  # Team members have this manager as TL
            "user_info.position": {"$ne": "Manager"}  # Exclude other managers
        }
        
        # Add additional filters
        if departmentFilter and departmentFilter != "All":
            base_match["user_info.department"] = departmentFilter
        
        if statusFilter and statusFilter != "All":
            if statusFilter == "Pending":
                base_match["status"] = {"$exists": False}
            else:
                base_match["status"] = statusFilter
        
        if leaveTypeFilter and leaveTypeFilter != "All":
            base_match["leaveType"] = leaveTypeFilter
        
        # Apply the match conditions
        pipeline.append({"$match": base_match})
        
        # Add employee info fields to output
        pipeline.append({
            "$addFields": {
                "employeeName": "$user_info.name",
                "position": "$user_info.position",
                "department": "$user_info.department",
                "email": "$user_info.email",
                "teamLeader": "$user_info.TL"
            }
        })
        
        # Remove temporary fields
        pipeline.append({
            "$project": {
                "user_info": 0,
                "userid_as_objectid": 0
            }
        })
        
        # Sort by request date (most recent first)
        pipeline.append({
            "$sort": {"requestDate": -1}
        })
        
        # Execute aggregation
        leave_details = list(Leave.aggregate(pipeline))
        
        # Format dates and ObjectIds
        for leave in leave_details:
            leave["_id"] = str(leave["_id"])
            if "selectedDate" in leave and leave["selectedDate"]:
                leave["selectedDate"] = leave["selectedDate"].strftime("%d-%m-%Y")
            if "requestDate" in leave and leave["requestDate"]:
                leave["requestDate"] = leave["requestDate"].strftime("%d-%m-%Y")
            if "ToDate" in leave and leave["ToDate"]:
                leave["ToDate"] = leave["ToDate"].strftime("%d-%m-%Y")
        
        return {
            "manager_info": {
                "user_id": user_id,
                "manager_name": manager_name
            },
            "leave_details": leave_details,
            "total_count": len(leave_details),
            "filters_applied": {
                "status": statusFilter or "All",
                "leave_type": leaveTypeFilter or "All",
                "department": departmentFilter or "All"
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/manager/remote_work_details/{user_id}")
async def get_manager_team_remote_work_details(
    user_id: str,
    statusFilter: Optional[str] = Query(None),
    departmentFilter: Optional[str] = Query(None)
):
    """Get remote work details for team members under a specific manager"""
    try:
        # First, verify the manager exists and get their info
        manager = Users.find_one({"_id": ObjectId(user_id)})
        if not manager:
            raise HTTPException(status_code=404, detail="Manager not found")
        
        manager_name = manager.get("name")
        if not manager_name:
            raise HTTPException(status_code=400, detail="Manager name not found")
        
        # Build the aggregation pipeline
        pipeline = []
        
        # Convert userid to ObjectId if it's a string
        pipeline.append({
            "$addFields": {
                "userid_as_objectid": {
                    "$cond": {
                        "if": {"$eq": [{"$type": "$userid"}, "objectId"]},
                        "then": "$userid",
                        "else": {"$toObjectId": "$userid"}
                    }
                }
            }
        })
        
        # Join with Users collection
        pipeline.append({
            "$lookup": {
                "from": "Users",
                "localField": "userid_as_objectid",
                "foreignField": "_id",
                "as": "user_info"
            }
        })
        
        # Unwind the user_info array
        pipeline.append({"$unwind": "$user_info"})
        
        # Filter to only show team members under this manager
        base_match = {
            "user_info.TL": manager_name,  # Team members have this manager as TL
            "user_info.position": {"$ne": "Manager"}  # Exclude other managers
        }
        
        # Add additional filters
        if departmentFilter and departmentFilter != "All":
            base_match["user_info.department"] = departmentFilter
        
        if statusFilter and statusFilter != "All":
            if statusFilter == "Pending":
                base_match["status"] = {"$exists": False}
                base_match["Recommendation"] = {"$exists": False}
            elif statusFilter == "Recommended":
                base_match["Recommendation"] = "Recommend"
            else:
                base_match["status"] = statusFilter
        
        # Apply the match conditions
        pipeline.append({"$match": base_match})
        
        # Add employee info fields to output
        pipeline.append({
            "$addFields": {
                "employeeName": "$user_info.name",
                "position": "$user_info.position",
                "department": "$user_info.department",
                "email": "$user_info.email",
                "teamLeader": "$user_info.TL"
            }
        })
        
        # Remove temporary fields
        pipeline.append({
            "$project": {
                "user_info": 0,
                "userid_as_objectid": 0
            }
        })
        
        # Sort by request date (most recent first)
        pipeline.append({
            "$sort": {"requestDate": -1}
        })
        
        # Execute aggregation
        remote_work_details = list(RemoteWork.aggregate(pipeline))
        
        # Format dates and ObjectId
        for remote_work in remote_work_details:
            remote_work["_id"] = str(remote_work["_id"])
            if "fromDate" in remote_work and remote_work["fromDate"]:
                remote_work["fromDate"] = remote_work["fromDate"].strftime("%d-%m-%Y")
            if "toDate" in remote_work and remote_work["toDate"]:
                remote_work["toDate"] = remote_work["toDate"].strftime("%d-%m-%Y")
            if "requestDate" in remote_work and remote_work["requestDate"]:
                remote_work["requestDate"] = remote_work["requestDate"].strftime("%d-%m-%Y")
        
        return {
            "manager_info": {
                "user_id": user_id,
                "manager_name": manager_name
            },
            "remote_work_details": remote_work_details,
            "total_count": len(remote_work_details),
            "filters_applied": {
                "status": statusFilter or "All",
                "department": departmentFilter or "All"
            }
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/manager/team_members/{user_id}")
async def get_manager_team_members(user_id: str):
    """Get list of team members under a specific manager"""
    try:
        # Get manager info
        manager = Users.find_one({"_id": ObjectId(user_id)})
        if not manager:
            raise HTTPException(status_code=404, detail="Manager not found")
        
        manager_name = manager.get("name")
        
        # Get team members under this manager
        team_members = list(Users.find(
            {
                "TL": manager_name,
                "position": {"$ne": "Manager"}
            },
            {
                "_id": 1,
                "name": 1,
                "email": 1,
                "position": 1,
                "department": 1,
                "phone": 1,
                "status": 1
            }
        ))
        
        # Format the response
        formatted_members = []
        for member in team_members:
            formatted_members.append({
                "userid": str(member["_id"]),
                "name": member.get("name"),
                "email": member.get("email"),
                "position": member.get("position"),
                "department": member.get("department"),
                "phone": member.get("phone"),
                "status": member.get("status", "Active")
            })
        
        return {
            "manager_info": {
                "user_id": user_id,
                "manager_name": manager_name
            },
            "team_members": formatted_members,
            "total_count": len(formatted_members)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/leave_details/user/")
async def get_all_users_leave_details(
    statusFilter: Optional[str] = Query(None),
    leaveTypeFilter: Optional[str] = Query(None),
    positionFilter: Optional[str] = Query(None),
    departmentFilter: Optional[str] = Query(None)
):
    """Get leave details for ALL users (no specific userid required)"""
    try:
        # Build the aggregation pipeline with flexible userid matching
        pipeline = []
        
        # Convert userid to ObjectId if it's a string
        pipeline.append({
            "$addFields": {
                "userid_as_objectid": {
                    "$cond": {
                        "if": {"$eq": [{"$type": "$userid"}, "objectId"]},
                        "then": "$userid",
                        "else": {"$toObjectId": "$userid"}
                    }
                }
            }
        })
        
        # Join with Users collection
        pipeline.append({
            "$lookup": {
                "from": "Users",
                "localField": "userid_as_objectid",
                "foreignField": "_id",
                "as": "user_info"
            }
        })
        
        # Handle cases where user info might not be found
        pipeline.append({
            "$addFields": {
                "user_info": {
                    "$cond": {
                        "if": {"$eq": [{"$size": "$user_info"}, 0]},
                        "then": [{"name": "Unknown User", "position": "Unknown", "department": "Unknown", "email": "Unknown", "TL": "Unknown"}],
                        "else": "$user_info"
                    }
                }
            }
        })
        
        # Unwind the user_info array
        pipeline.append({"$unwind": "$user_info"})
        
        # Build match conditions for filtering
        match_conditions = {}
        
        if positionFilter and positionFilter != "All":
            match_conditions["user_info.position"] = positionFilter
            
        if departmentFilter and departmentFilter != "All":
            match_conditions["user_info.department"] = departmentFilter
        
        if statusFilter and statusFilter != "All":
            if statusFilter == "Pending":
                match_conditions["status"] = {"$exists": False}
            else:
                match_conditions["status"] = statusFilter
        
        if leaveTypeFilter and leaveTypeFilter != "All":
            match_conditions["leaveType"] = leaveTypeFilter
        
        # Add match stage if there are conditions
        if match_conditions:
            pipeline.append({"$match": match_conditions})
        
        # Add employee info fields to output
        pipeline.append({
            "$addFields": {
                "employeeName": "$user_info.name",
                "position": "$user_info.position",
                "department": "$user_info.department",
                "email": "$user_info.email",
                "teamLeader": "$user_info.TL"
            }
        })
        
        # Remove temporary fields
        pipeline.append({
            "$project": {
                "user_info": 0,
                "userid_as_objectid": 0
            }
        })
        
        # Sort by request date (most recent first)
        pipeline.append({
            "$sort": {"requestDate": -1}
        })
        
        # Execute aggregation
        leave_details = list(Leave.aggregate(pipeline))
        
        # Format dates and ObjectIds
        for leave in leave_details:
            leave["_id"] = str(leave["_id"])
            if "selectedDate" in leave and leave["selectedDate"]:
                leave["selectedDate"] = leave["selectedDate"].strftime("%d-%m-%Y")
            if "requestDate" in leave and leave["requestDate"]:
                leave["requestDate"] = leave["requestDate"].strftime("%d-%m-%Y")
            if "ToDate" in leave and leave["ToDate"]:
                leave["ToDate"] = leave["ToDate"].strftime("%d-%m-%Y")
        
        return {
            "leave_details": leave_details,
            "total_count": len(leave_details),
            "filters_applied": {
                "position": positionFilter or "All",
                "status": statusFilter or "All",
                "leave_type": leaveTypeFilter or "All",
                "department": departmentFilter or "All"
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/remote_work_details/user/")
async def get_all_users_remote_work_details(
    statusFilter: Optional[str] = Query(None),
    positionFilter: Optional[str] = Query(None),
    departmentFilter: Optional[str] = Query(None)
):
    """Get remote work details for ALL users (no specific userid required)"""
    try:
        # Build the aggregation pipeline with flexible userid matching
        pipeline = []
        
        # Convert userid to ObjectId if it's a string
        pipeline.append({
            "$addFields": {
                "userid_as_objectid": {
                    "$cond": {
                        "if": {"$eq": [{"$type": "$userid"}, "objectId"]},
                        "then": "$userid",
                        "else": {"$toObjectId": "$userid"}
                    }
                }
            }
        })
        
        # Join with Users collection
        pipeline.append({
            "$lookup": {
                "from": "Users",
                "localField": "userid_as_objectid",
                "foreignField": "_id",
                "as": "user_info"
            }
        })
        
        # Handle cases where user info might not be found
        pipeline.append({
            "$addFields": {
                "user_info": {
                    "$cond": {
                        "if": {"$eq": [{"$size": "$user_info"}, 0]},
                        "then": [{"name": "Unknown User", "position": "Unknown", "department": "Unknown", "email": "Unknown", "TL": "Unknown"}],
                        "else": "$user_info"
                    }
                }
            }
        })
        
        # Unwind the user_info array
        pipeline.append({"$unwind": "$user_info"})
        
        # Build match conditions for filtering
        match_conditions = {}
        
        if positionFilter and positionFilter != "All":
            match_conditions["user_info.position"] = positionFilter
            
        if departmentFilter and departmentFilter != "All":
            match_conditions["user_info.department"] = departmentFilter
        
        if statusFilter and statusFilter != "All":
            if statusFilter == "Pending":
                match_conditions["status"] = {"$exists": False}
                match_conditions["Recommendation"] = {"$exists": False}
            elif statusFilter == "Recommended":
                match_conditions["Recommendation"] = "Recommend"
            else:
                match_conditions["status"] = statusFilter
        
        # Add match stage if there are conditions
        if match_conditions:
            pipeline.append({"$match": match_conditions})
        
        # Add employee info fields to output
        pipeline.append({
            "$addFields": {
                "employeeName": "$user_info.name",
                "position": "$user_info.position",
                "department": "$user_info.department",
                "email": "$user_info.email",
                "teamLeader": "$user_info.TL"
            }
        })
        
        # Remove temporary fields
        pipeline.append({
            "$project": {
                "user_info": 0,
                "userid_as_objectid": 0
            }
        })
        
        # Sort by request date (most recent first)
        pipeline.append({
            "$sort": {"requestDate": -1}
        })
        
        # Execute aggregation
        remote_work_details = list(RemoteWork.aggregate(pipeline))
        
        # Format dates and ObjectId
        for remote_work in remote_work_details:
            remote_work["_id"] = str(remote_work["_id"])
            if "fromDate" in remote_work and remote_work["fromDate"]:
                remote_work["fromDate"] = remote_work["fromDate"].strftime("%d-%m-%Y")
            if "toDate" in remote_work and remote_work["toDate"]:
                remote_work["toDate"] = remote_work["toDate"].strftime("%d-%m-%Y")
            if "requestDate" in remote_work and remote_work["requestDate"]:
                remote_work["requestDate"] = remote_work["requestDate"].strftime("%d-%m-%Y")
        
        return {
            "remote_work_details": remote_work_details,
            "total_count": len(remote_work_details),
            "filters_applied": {
                "position": positionFilter or "All",
                "status": statusFilter or "All",
                "department": departmentFilter or "All"
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_all_users")
async def get_all_users_route():
        # Fetch all users using the function from Mongo.py
        users = get_all_users()
        if users:
            return users  # Return the list of users
        else:
            raise HTTPException(status_code=404, detail="No users found")


@app.post("/add_task")
async def add_task(item: Tasklist):
    try:
        # ✅ just validate, don't reformat
        datetime.strptime(item.date, "%Y-%m-%d")
        datetime.strptime(item.due_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use yyyy-mm-dd.")

    # ✅ pass raw, let add_task_list handle formatting
    result = add_task_list(item.task, item.userid, item.date, item.due_date, assigned_by="self", priority=item.priority, subtasks=[subtask.dict() for subtask in item.subtasks])
    return {"task_id": result, "message": "Task added successfully"}

from typing import Optional

from datetime import datetime

@app.get("/manager_tasks")
def get_manager_tasks(manager_name: str, userid: Optional[str] = None):
    try:
        tasks = Mongo.assigned_task(manager_name, userid)
        
        for t in tasks:
            # Attach employee name
            user = Mongo.get_user_info(t["userid"])
            if user:
                t["employee_name"] = user.get("name", "Unknown")
            
            # ✅ Normalize created_date
            if "created_date" not in t or not t["created_date"]:
                raw_date = t.get("date")
                if raw_date:
                    try:
                        # If it's in DD-MM-YYYY format
                        parsed = datetime.strptime(raw_date, "%d-%m-%Y")
                        t["created_date"] = parsed.strftime("%Y-%m-%d")  # ISO-like string
                    except Exception:
                        # fallback: keep original
                        t["created_date"] = str(raw_date)

        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/edit_task")
def edit_task(request: Taskedit):
    try:
        # Get current date for completed_date if status is being updated
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        result = Mongo.edit_the_task(
            taskid=str(request.taskid),  # Ensure taskid is string
            userid=request.userid,
            cdate=current_date,  # Pass the required cdate parameter
            due_date=request.due_date,
            updated_task=request.updated_task,
            status=request.status,
            priority=request.priority,
            subtasks=request.subtasks,
            comments=request.comments,
            files=request.files,
            verified=request.verified 
        )
        
        if result == "Task not found":
            raise HTTPException(status_code=404, detail="Task not found")
        elif result == "No fields to update":
            raise HTTPException(status_code=400, detail="No fields to update")
        elif result == "Cannot demote verified task":
            raise HTTPException(status_code=403, detail="Cannot change status of a verified task")
        
        return {"message": result}
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.delete("/task_delete/{taskid}")
async def task_delete(taskid: str):
    result = delete_a_task(taskid)
    return {"result": result}

# Enhanced Task Notification Endpoints
@app.post("/trigger_deadline_check")
async def trigger_deadline_check():
    """Manually trigger deadline checking for testing/immediate needs"""
    try:
        overdue_count = await Mongo.check_and_notify_overdue_tasks()
        upcoming_count = await Mongo.check_upcoming_deadlines()
        
        return {
            "status": "success",
            "overdue_notifications_sent": overdue_count,
            "upcoming_deadline_notifications_sent": upcoming_count,
            "message": f"Processed {overdue_count} overdue tasks and {upcoming_count} upcoming deadline reminders"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking deadlines: {str(e)}")

@app.delete("/task_delete/{taskid}")
async def task_delete(taskid: str):
    result = delete_a_task(taskid)
    return {"result": result}

@app.get("/get_tasks/{userid}/")  # Also handle requests with trailing slash
async def get_tasks(userid: str):
    result = get_the_tasks(userid)
    if not result:
        return {"message": "No tasks found for the given user"}

    for t in result:
        t["subtasks"] = t.get("subtasks", [])
        t["comments"] = t.get("comments", [])   # NEW
        t["files"] = t.get("files", [])         # NEW

    return result


@app.get("/get_tasks/{userid}/{date}")
async def get_tasks(userid: str, date: str):
    result = get_the_tasks(userid, date)
    if not result:
        return {"message": "No tasks found for the given user in selected date"}

    for t in result:
        t["subtasks"] = t.get("subtasks", [])
        t["comments"] = t.get("comments", [])   # NEW
        t["files"] = t.get("files", [])         # NEW

    return result

@app.get("/get_manager_tasks/{userid}")
async def fetch_manager_tasks(userid: str, date: str = None):
    try:
        tasks = Mongo.get_manager_only_tasks(userid, date)
        for t in tasks:
            t["subtasks"] = t.get("subtasks", [])
            t["comments"] = t.get("comments", [])   # NEW
            t["files"] = t.get("files", [])         # NEW
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/get_manager")
def get_manager():
    try:
        result = get_user_by_position("Manager")
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Manager not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/tasks/{taskid}")
async def get_task(taskid: str):
    task = get_single_task(taskid)   # ← your DB function
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


    
@app.get("/get_hr_assigned_tasks/{hr_name}")
def api_get_hr_assigned_tasks(hr_name: str, userid: str = None, date: str = None):
    try:
        tasks = get_hr_assigned_tasks(hr_name, userid, date)
        return JSONResponse(content=tasks)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)



@app.get("/get_single_task/{taskid}")
async def get_task(taskid : str):
    result = get_single_task(taskid)
    if not result:
        return {"message": "No tasks found for the given task id"}
    return result

@app.post("/task/{taskid}/files")
async def upload_task_file(
    taskid: str,
    file: UploadFile = File(...),
    uploaded_by: str = Form(...)
):
   
    try:
        file_bytes = await file.read()
        
        # Test MongoDB connection before attempting to save
        try:
            client.admin.command('ping')
        except Exception as conn_error:
            print(f"MongoDB connection error: {conn_error}")
            raise HTTPException(status_code=503, detail=f"Database connection failed: {str(conn_error)}")
        
        gridfs_id = fs.put(file_bytes, filename=file.filename, content_type=file.content_type, uploadedBy=uploaded_by)
        file_meta = {
            "id": str(gridfs_id),
            "name": file.filename,
            "size": len(file_bytes),
            "type": file.content_type,
            "uploadedAt": datetime.now().isoformat(),
            "uploadedBy": uploaded_by,
            "gridfs_id": str(gridfs_id)
        }

        ok = Mongo.add_file_to_task(taskid, file_meta)
        if not ok:
            fs.delete(gridfs_id)
            raise HTTPException(status_code=404, detail="Task not found")

        # Send file upload notifications
        try:
            task = Mongo.Tasks.find_one({"_id": Mongo.ObjectId(taskid)})
            if task:
                task_title = task.get("task", "Task")
                task_userid = task.get("userid")
                
                # Get uploader name
                uploader = Mongo.Users.find_one({"_id": Mongo.ObjectId(uploaded_by)}) if ObjectId.is_valid(uploaded_by) else None
                uploader_name = uploader.get("name", "Team Member") if uploader else "Team Member"
                
                # Notify task owner if file uploaded by someone else
                if task_userid and uploaded_by != task_userid:
                    Mongo.create_notification(
                        userid=task_userid,
                        title="File Uploaded",
                        message=f"{uploader_name} uploaded a file '{file.filename}' to your task '{task_title}'.",
                        notification_type="task",
                        priority="medium",
                        action_url=Mongo.get_role_based_action_url(task_userid, "task"),
                        related_id=taskid,
                        metadata={
                            "task_title": task_title,
                            "action": "File Uploaded",
                            "filename": file.filename,
                            "uploaded_by": uploaded_by
                        }
                    )
                
                # Notify manager if they exist and didn't upload the file
                assigned_by = task.get("assigned_by")
                if assigned_by and assigned_by != "self" and assigned_by != uploaded_by and assigned_by != task_userid:
                    Mongo.create_notification(
                        userid=assigned_by,
                        title="File Uploaded to Assigned Task",
                        message=f"{uploader_name} uploaded a file '{file.filename}' to the task '{task_title}'.",
                        notification_type="task",
                        priority="medium",
                        action_url=Mongo.get_role_based_action_url(assigned_by, "manager_task"),
                        related_id=taskid,
                        metadata={
                            "task_title": task_title,
                            "action": "File Uploaded",
                            "filename": file.filename,
                            "uploaded_by": uploaded_by
                        }
                    )
        except Exception as e:
            print(f"Error sending file upload notification: {e}")
            traceback.print_exc()

        return {"message": "File uploaded successfully", "file": file_meta}
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"File upload error: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"File upload failed: {str(e)}")

@app.get("/task/{taskid}/files/{fileid}")
async def get_task_file(taskid: str, fileid: str):
    file_meta = Mongo.get_task_file_metadata(taskid, fileid)
    if not file_meta:
        raise HTTPException(status_code=404, detail="File not found")

    
    gridfs_id = file_meta.get("gridfs_id")
    if not gridfs_id:
        raise HTTPException(status_code=404, detail="File not stored in GridFS")
    try:
        file_obj = fs.get(ObjectId(gridfs_id))
        return StreamingResponse(file_obj, media_type=file_meta.get("type", "application/octet-stream"),
                                headers={"Content-Disposition": f"attachment; filename={file_meta.get('name', 'file')}"})
    except Exception:
        raise HTTPException(status_code=404, detail="File not found in GridFS")

@app.get("/get_user/{userid}")
def get_user(userid: str):
    print("Searching user ID:", userid)

    try:
        obj_id = ObjectId(userid)
    except Exception as e:
        print(f"Invalid ObjectId format: {str(e)}")
        return JSONResponse(
            content={"error": f"Invalid ID format: {str(e)}", "userid": userid},
            status_code=400
        )

    try:
        # First, try to find in Users collection
        user = Users.find_one({"_id": obj_id}, {"password": 0})
        
        if user:
            user = serialize_mongo_doc(user)
            print(f"User found in Users collection: {user.get('email')}")
            return JSONResponse(content=user, status_code=200)
        
        # If not found in Users, check admin collection
        admin_user = admin.find_one({"_id": obj_id}, {"password": 0})
        
        if admin_user:
            admin_user = serialize_mongo_doc(admin_user)
            print(f"User found in admin collection: {admin_user.get('email')}")
            return JSONResponse(content=admin_user, status_code=200)
        
        # User not found in either collection
        print("User not found in any collection!")
        return JSONResponse(
            content={"error": "User not found", "userid": userid},
            status_code=404
        )
    
    except Exception as e:
        print(f"Database error in get_user: {str(e)}")
        import traceback
        traceback.print_exc()
        return JSONResponse(
            content={"error": "Internal server error", "details": str(e)},
            status_code=500
        )




@app.put("/edit_employee")
def edit_employee(item: EditEmployee):
    try:
        # Convert Pydantic model to dict
        employee_dict = item.dict()
       
        # Call the edit function
        result = edit_an_employee(employee_dict)
        return result
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in edit_employee endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/get_managers_list")
async def fetch_managers():
 result = get_managers()
 return result




@app.get("/get_admin/{userid}")
def get_admin(userid: str):
    result = Mongo.get_admin_information(userid)
    return result


@app.post("/add_employee")
def add_employee(item:AddEmployee):
    result = add_an_employee(item.dict())
    return result




@app.get("/auto_approve_manager_leaves")
async def trigger_auto_approval():
    result = auto_approve_manager_leaves()
    return result

@app.get("/get_team_members")
def get_members(TL: str = Query(..., alias="TL")):
    result = get_team_members(TL)
    return result

@app.post("/task_assign_to_multiple_members") 
async def task_assign(item: Taskassign):
    print(item.Task_details)
    # Add assigned_by field and get assigner name
    assigner_name = None
    for t in item.Task_details:
        if "assigned_by" not in t:
            t["assigned_by"] = t.get("TL", "Manager")
        # Get assigner name from first item
        if not assigner_name and t.get("assigned_by"):
            assigner_name = t.get("assigned_by")
        elif not assigner_name and t.get("TL"):
            assigner_user = Users.find_one({"_id": ObjectId(t["TL"])}) if ObjectId.is_valid(t["TL"]) else None
            if not assigner_user:
                assigner_user = Users.find_one({"name": t["TL"]})
            assigner_name = assigner_user.get("name", t["TL"]) if assigner_user else t["TL"]
    
    # ✅ FIX: Actually insert the tasks into database with notifications
    result = await task_assign_to_multiple_users_with_notification(
        task_details=item.Task_details, 
        assigner_name=assigner_name
    )
    
    return {
        "message": "Tasks assigned successfully",
        "task_ids": result,
        "count": len(result)
    }

@app.get("/get_manager_hr_tasks/{userid}")
async def fetch_manager_hr_tasks(userid: str, date: str = None):
    try:
        tasks = get_manager_hr_assigned_tasks(userid, date)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_hr_self_tasks/{userid}")
async def fetch_hr_self_tasks(userid: str, date: str = None):
    try:
        tasks = get_hr_self_assigned_tasks(userid, date)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_assigned_task")
def get_assigned_tasks(TL: str = Query(..., alias="TL"), userid: str | None = Query(None, alias = "userid")):
    result = assigned_task(TL, userid)
    return result

@app.get("/ip-info")
def fetch_ip_info():
    return {
        "public_ip": get_public_ip(),
        "local_ip": get_local_ip()
}

# Notification System Endpoints
@app.post("/notifications/create")
async def create_notification_endpoint(notification: NotificationModel):
    """Create a new notification"""
    try:
        result = create_notification(
            userid=notification.userid,
            title=notification.title,
            message=notification.message,
            notification_type=notification.type,
            priority=notification.priority,
            action_url=notification.action_url,
            related_id=notification.related_id,
            metadata=notification.metadata
        )
        if result:
            return {"message": "Notification created successfully", "notification_id": result}
        else:
            raise HTTPException(status_code=500, detail="Failed to create notification")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notifications/{userid}")
async def get_user_notifications(
    userid: str,
    type: str = None,
    priority: str = None,
    is_read: bool = None,
    limit: int = 50
):
    """Get notifications for a user with optional filters"""
    try:
        notifications = get_notifications(
            userid=userid,
            notification_type=type,
            priority=priority,
            is_read=is_read,
            limit=limit
        )
        return {"notifications": notifications}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/notifications/{notification_id}/read")
async def mark_notification_as_read(notification_id: str, update: NotificationUpdate):
    """Mark a notification as read/unread"""
    try:
        success = mark_notification_read(notification_id, update.is_read)
        if success:
            return {"message": "Notification updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Notification not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/notifications/{userid}/mark-all-read")
async def mark_all_user_notifications_read(userid: str):
    """Mark all notifications as read for a user"""
    try:
        count = mark_all_notifications_read(userid)
        return {"message": f"Marked {count} notifications as read"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notifications/{userid}/unread-count")
async def get_user_unread_count(userid: str):
    """Get count of unread notifications for a user"""
    try:
        count = get_unread_notification_count(userid)
        return {"unread_count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/notifications/{notification_id}")
async def delete_notification_endpoint(notification_id: str):
    """Delete a notification"""
    try:
        success = delete_notification(notification_id)
        if success:
            return {"message": "Notification deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Notification not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notifications/{userid}/type/{notification_type}")
async def get_notifications_by_type_endpoint(userid: str, notification_type: str):
    """Get notifications by type for a user"""
    try:
        notifications = get_notifications_by_type(userid, notification_type)
        return {"notifications": notifications}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# WebSocket endpoint for real-time notifications
@app.websocket("/ws/notifications/{userid}")
async def websocket_endpoint(websocket: WebSocket, userid: str):
    print(f"WebSocket connection attempt for user: {userid}")
    try:
        await notification_manager.connect(websocket, userid)
        print(f"WebSocket connected successfully for user: {userid}")
        
        # Send existing unread notifications on connection
        try:
            notifications = get_notifications(userid, is_read=False, limit=10)
            if notifications:
                for notification in notifications:
                    if websocket.client_state.value == 1:  # WebSocketState.CONNECTED
                        await websocket.send_text(json.dumps({
                            "type": "notification",
                            "data": notification
                        }))
        except Exception as e:
            print(f"Error sending initial notifications: {e}")
        
        # Keep the connection alive
        while True:
            try:
                # Check if connection is still open
                if websocket.client_state.value != 1:  # Not CONNECTED
                    break
                    
                # Receive any message (ping/pong or other client messages)
                data = await websocket.receive_text()
                print(f"Received message from {userid}: {data}")
                
                # Only send response if connection is still open
                if websocket.client_state.value == 1:  # WebSocketState.CONNECTED
                    await websocket.send_text(json.dumps({"type": "pong", "message": "Connection alive"}))
                    
            except WebSocketDisconnect:
                print(f"WebSocket disconnect for user: {userid}")
                break
            except Exception as e:
                print(f"WebSocket receive error for user {userid}: {e}")
                break
                
    except WebSocketDisconnect:
        print(f"WebSocket disconnect for user: {userid}")
    except Exception as e:
        print(f"WebSocket error for user {userid}: {e}")
    finally:
        # Ensure cleanup happens
        notification_manager.disconnect(websocket, userid)

@app.get("/debug/admin-data")
async def debug_admin_data():
    """Debug endpoint to check admin user data and potential issues"""
    try:
        results = {}
        
        # Check admin collection
        admin_users = list(Mongo.admin.find({}, {"_id": 1, "name": 1, "email": 1}))
        results["admin_collection"] = {
            "count": len(admin_users),
            "users": admin_users[:5]  # Show first 5 for debugging
        }
        
        # Check Users collection for admin positions
        admin_position_users = list(Mongo.Users.find(
            {"position": {"$in": ["Admin", "Administrator", "CEO", "Director"]}}, 
            {"_id": 1, "name": 1, "position": 1, "email": 1}
        ))
        results["users_collection_admins"] = {
            "count": len(admin_position_users),
            "users": admin_position_users[:5]  # Show first 5 for debugging
        }
        
        # Check all positions in Users collection
        all_positions = list(Mongo.Users.distinct("position"))
        results["all_positions"] = all_positions
        
        # Test admin ID retrieval
        admin_ids = await Mongo.get_admin_user_ids()
        results["retrieved_admin_ids"] = admin_ids
        
        # Check for pending manager leaves
        manager_users = list(Mongo.Users.find({"position": "Manager"}, {"_id": 1, "name": 1}))
        manager_ids = [str(manager["_id"]) for manager in manager_users]
        
        pending_manager_leaves = list(Mongo.Leave.find({
            "userid": {"$in": manager_ids},
            "Recommendation": {"$exists": False},
            "status": {"$exists": False}
        }, {"_id": 1, "employeeName": 1, "leaveType": 1, "selectedDate": 1}))
        
        results["manager_data"] = {
            "manager_count": len(manager_users),
            "pending_leaves_count": len(pending_manager_leaves),
            "sample_pending_leaves": pending_manager_leaves[:3]
        }
        
        return {
            "success": True,
            "debug_results": results
        }
        
    except Exception as e:
        print(f"Error in admin debug: {e}")
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    # Get port from environment variable (Railway sets this)
    port = int(os.environ.get("PORT", 8080))
    
    # Check if SSL certificates exist (for local development)
    key_file_path = os.path.join(os.path.dirname(__file__), '../certificates/key.pem')
    cert_file_path = os.path.join(os.path.dirname(__file__), '../certificates/cert.pem')
    
    # Use SSL only if certificates exist (local development)
    # Railway handles SSL at the edge, so we don't need it in production
    if os.path.exists(key_file_path) and os.path.exists(cert_file_path):
        print(f"Starting with SSL on port {port}")
        uvicorn.run(
            "Server:app",
            host="0.0.0.0",
            port=port,
            ssl_keyfile=key_file_path,
            ssl_certfile=cert_file_path
        )
    else:
        print(f"Starting without SSL on port {port}")
        uvicorn.run(
            "Server:app",
            host="0.0.0.0",
            port=port
        )


#---------------------------------------------------------------------------------------------------------




# Holiday Management Endpoints
@app.post("/api/holidays/{year}")
def add_holidays(year: int, body: HolidayYear):
    """Admin only - Add holidays for a specific year"""
    if body.year != year:
        raise HTTPException(status_code=400, detail="Year mismatch between path and body")
   
    insert_holidays(year, [h.dict() for h in body.holidays])
    return {"message": f"Holidays saved for {year}"}


@app.get("/api/holidays/{year}")
def get_holidays_for_year(year: int):
    holiday_doc = get_holidays(year)
    if not holiday_doc:
        return {"year": year, "holidays": []}
   
    # Convert ObjectId to string if exists
    if "_id" in holiday_doc:
        holiday_doc["_id"] = str(holiday_doc["_id"])
   
    return holiday_doc




@app.get("/working-days/{year}")
def get_working_days(year: int):
    """Get working days calculation for a year"""
    holiday_doc = get_holidays(year)
    if not holiday_doc:
        raise HTTPException(status_code=404, detail=f"No holidays defined for {year}")
   
    holidays = holiday_doc["holidays"]
    working_days = calculate_working_days(year, holidays)
   
    return {
        "year": year,
        "totalWorkingDays": len(working_days),
        "workingDays": working_days,
        "holidays": holidays
    }

@app.get("/attendance/user/{userid}/year/{year}")
async def get_user_attendance_by_year(userid: str, year: int):
    """User can see their attendance stats for a specific year"""
    try:
        stats = calculate_user_attendance_stats(userid, year)
        user = Users.find_one({"_id": ObjectId(userid)}, {"name": 1, "email": 1})
        
        return {
            "user_info": {
                "userid": userid,
                "name": user.get("name", "Unknown") if user else "Unknown",
                "email": user.get("email", "") if user else ""
            },
            "attendance_stats": stats,
            "year": year
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 


@app.get("/attendance/team/{team_leader}")
async def get_team_attendance(team_leader: str, year: int = Query(None)):
    """Team Leader can see their team members' attendance"""
    try:
        if year is None:
            year = date.today().year
        
        team_stats = get_team_attendance_stats(team_leader, year)
        return team_stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        
# User Level Endpoints (Lowest Level - Own Data Only)
@app.get("/attendance/user/{userid}")
async def get_user_attendance(userid: str):
    """User can see only their own attendance statistics"""
    try:
        dashboard_data = get_user_attendance_dashboard(userid)
        return dashboard_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance/team/{team_leader}/member/{userid}")
async def get_team_member_attendance(team_leader: str, userid: str, year: int = Query(None)):
    """Team Leader can see specific team member's attendance"""
    try:
        if year is None:
            year = date.today().year
       
        # Verify that the user belongs to this team leader
        user = Users.find_one({"_id": ObjectId(userid), "TL": team_leader})
        if not user:
            raise HTTPException(status_code=403, detail="User is not in your team")
       
        stats = calculate_user_attendance_stats(userid, year)
        stats["user_info"] = {
            "name": user.get("name"),
            "email": user.get("email"),
            "department": user.get("department"),
            "position": user.get("position")
        }
       
        return {
            "team_leader": team_leader,
            "member_stats": stats,
            "year": year
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Manager Level Endpoints
@app.get("/attendance/manager/{manager_userid}")
async def get_manager_attendance_overview(manager_userid: str, year: int = Query(None)):
    """Manager can see all teams under them"""
    try:
        if year is None:
            year = date.today().year
       
        manager_stats = get_manager_team_attendance(manager_userid, year)
        return manager_stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance/department/{department}")
async def get_department_attendance(department: str, year: int = Query(None)):
    """Manager can see department-wise attendance"""
    try:
        if year is None:
            year = date.today().year
       
        dept_stats = get_department_attendance_stats(department, year)
        return dept_stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Admin Level Endpoints (Highest Level - Can See Everything)
@app.get("/attendance/admin/overview")
async def get_admin_attendance_overview(year: int = Query(None)):
    """Admin can see company-wide attendance statistics"""
    try:
        if year is None:
            year = date.today().year
       
        company_stats = get_department_attendance_stats(year=year)  # All departments
        return company_stats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Utility Endpoints
@app.post("/attendance/refresh-stats")
async def refresh_attendance_stats():
    """Manually trigger attendance statistics refresh (Admin only)"""
    try:
        updated_count = update_daily_attendance_stats()
        return {"message": f"Successfully updated attendance stats for {updated_count} users"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/attendance/summary/{userid}")
async def get_attendance_summary(userid: str):
    """Get a quick summary of user's attendance (for dashboard cards)"""
    try:
        current_year = date.today().year
        stats = calculate_user_attendance_stats(userid, current_year)
       
        return {
            "userid": userid,
            "current_year": current_year,
            "attendance_percentage": stats["attendance_percentage"],
            "present_days": stats["present_days"],
            "total_working_days": stats["total_working_days"],
            "leave_days_taken": stats["leave_days_taken"],
            "leave_percentage": stats["leave_percentage"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Role-based access endpoint
@app.get("/attendance/dashboard/{userid}")
async def get_role_based_attendance_dashboard(userid: str, year: int = Query(None)):
    """Get attendance dashboard based on user's role"""
    try:
        if year is None:
            year = date.today().year
       
        # Get user info to determine role
        user = Users.find_one({"_id": ObjectId(userid)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
       
        position = user.get("position", "User").lower()
       
        if position == "admin":
            return await get_admin_attendance_overview(year)
        elif position == "hr":
            # Placeholder: HR analytics not implemented, return empty or basic stats
            return {"message": "HR attendance analytics not implemented", "year": year}
        elif position == "manager":
            return await get_manager_attendance_overview(userid, year)
        elif position == "tl" or position == "team lead":
            team_leader_name = user.get("name")
            return await get_team_attendance(team_leader_name, year)
        else:  # Regular user
            return await get_user_attendance(userid)
           
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.websocket("/ws/notify/{user_id}")
async def ws_notify(websocket: WebSocket, user_id: str):
    await notify_manager.connect(user_id, websocket)
    try:
        # Keep the connection alive; client does not need to send anything frequently.
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        await notify_manager.disconnect(user_id, websocket)


# Fetch chat history
# server.py
active_users: dict[str, WebSocket] = {}

@app.websocket("/ws/{userid}")
async def websocket_endpoint(websocket: WebSocket, userid: str):
    # Connect socket
    await direct_chat_manager.connect(userid, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            msg["timestamp"] = datetime.utcnow().isoformat() + "Z"
            msg.pop("pending", None)

            msg_type = msg.get("type", "chat")

            if msg_type == "thread":
                temp_id = msg.get("tempId")
                msg["id"] = msg.get("id") or str(ObjectId())
                threads_collection.insert_one(msg.copy())
                msg["_tempId"] = temp_id
                msg.pop("_id", None)

                if msg.get("chatId") and msg.get("chatId").startswith("group_"):
                    # Send to group channel
                    await group_ws_manager.send_message(msg["chatId"], msg)
                else:
                    # Direct chat
                    await direct_chat_manager.send_message(msg["to_user"], msg)

            else:  # normal chat
                msg["chatId"] = msg.get("chatId") or "_".join(sorted([userid, msg["to_user"]]))
                chats_collection.insert_one(msg.copy())
                msg.pop("_id", None)

                # send to both sender and recipient
                await direct_chat_manager.send_message(msg["to_user"], msg)

    except WebSocketDisconnect:
        direct_chat_manager.disconnect(userid, websocket)





@app.get("/history/{chatId}")
async def history(chatId: str):
    cursor = chats_collection.find({"chatId": chatId}).sort("timestamp", 1)
    messages = []
    for doc in cursor:
        mid = str(doc.get("id") or doc.get("_id"))
        reply_count = threads_collection.count_documents({"rootId": mid})
        messages.append({
            "id": mid,
            "from_user": doc.get("from_user"),
            "to_user": doc.get("to_user"),
            "text": doc.get("text"),
            "file": doc.get("file"),
            "timestamp": doc["timestamp"].isoformat() if isinstance(doc.get("timestamp"), datetime) else doc.get("timestamp"),
            "chatId": doc.get("chatId"),
            "reply_count": reply_count,  
        })
    return messages


@app.post("/thread")
async def save_thread(payload: dict = Body(...)):
    payload["id"] = payload.get("id") or str(ObjectId())
    payload["timestamp"] = datetime.utcnow().isoformat() +"Z"
    threads_collection.insert_one(payload.copy())
    return {"status": "success", "thread": payload}

@app.get("/thread/{rootId}")
async def get_threads(rootId: str):
    threads = list(threads_collection.find({"rootId": rootId}).sort("timestamp", 1))
    result = []
    for t in threads:
        result.append({
            "id": str(t.get("id") or t.get("_id")),
            "from_user": t.get("from_user"),
            "to_user": t.get("to_user"),
            "text": t.get("text"),
            "file": t.get("file"),
            "timestamp": t.get("timestamp"),
            "rootId": t.get("rootId"),
        })
    return result


# Assign docs to users
# ------------------ Assign Documents ------------------

# ------------------ Assign Document ------------------
@app.post("/assign_docs")
async def assign_docs(payload: AssignPayload, assigned_by: str = "HR"):
    if not payload.userIds or not payload.docName:
        raise HTTPException(status_code=400, detail="docName and userIds required")
    
    count = 0
    for uid in payload.userIds:
        # Only add doc if not already assigned
        result = Users.update_one(
            {"userid": uid, "assigned_docs.docName": {"$ne": payload.docName}},
            {"$push": {
                "assigned_docs": {
                    "docName": payload.docName,
                    "status": "Pending",
                    "assignedBy": assigned_by,
                    "assignedAt": datetime.utcnow(),
                    "fileId": None,
                    "remarks": None
                }
            }}
        )
        if result.modified_count > 0:
            count += 1
            
            # Send notification to user about document assignment
            try:
                await Mongo.create_document_assignment_notification(
                    userid=uid,
                    doc_name=payload.docName,
                    assigned_by_name=assigned_by,
                    assigned_by_id=None  # Can be enhanced to get actual assigner ID
                )
            except Exception as e:
                print(f"Error sending document assignment notification: {e}")

    return {"message": f'"{payload.docName}" assigned to {count} user(s)'}
@app.get("/assign_docs")
def get_assigned_docs(userId: str = Query(...)):
    """
    Return all assigned documents for a given userId.
    """
    user = Users.find_one({"userId": userId}, {"assigned_docs": 1, "_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    assigned_docs = user.get("assigned_docs", [])
    # Optional: sort by assignedAt descending
    assigned_docs.sort(key=lambda d: d["assignedAt"], reverse=True)
    return assigned_docs

# ------------------ Fetch Assigned Documents ------------------
@app.get("/documents/assigned/{userId}")
def fetch_assigned_docs(userId: str):
    # First try to find user in Users collection
    user = Users.find_one({"userid": userId})
    
    # If not found, try with ObjectId format
    if not user:
        try:
            user = Users.find_one({"_id": ObjectId(userId)})
        except:
            pass
    
    # If still not found, check admin collection
    if not user:
        try:
            user = admin.find_one({"_id": ObjectId(userId)})
        except:
            pass
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    assigned_docs = []
    for doc in user.get("assigned_docs", []):
        file_id = doc.get("fileId")
        file_doc = assignments_collection.find_one({"_id": ObjectId(file_id)}) if file_id else None
        
        assigned_docs.append({
            "docName": doc.get("docName"),
            "status": doc.get("status", "Pending"),
            "fileUrl": f"/download_file/{file_id}" if file_doc else None,
            "assignedBy": doc.get("assignedBy"),
            "assignedAt": doc.get("assignedAt"),
            "fileId": file_id,
            "remarks": doc.get("remarks")
        })
    return assigned_docs



# ------------------ Review Document ------------------
@app.put("/review_document")
async def review_document(payload: ReviewPayload):
    result = Users.update_one(
        {"userid": payload.userId, "assigned_docs.docName": payload.docName},
        {"$set": {
            "assigned_docs.$.status": payload.status,
            "assigned_docs.$.remarks": payload.remarks,
            "assigned_docs.$.reviewedAt": datetime.utcnow()
        }}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Document assignment not found")
    
    # Send notification to user about document review
    try:
        # Get reviewer info (assuming it's from the request or session)
        # For now, we'll use a placeholder - you can enhance this to get actual reviewer info
        reviewer_name = payload.remarks or "Reviewer"  # This should be enhanced
        
        await Mongo.create_document_review_notification(
            userid=payload.userId,
            doc_name=payload.docName,
            reviewer_name="Document Reviewer",  # Should get actual reviewer name
            reviewer_id=None,  # Should get actual reviewer ID
            status=payload.status,
            remarks=payload.remarks
        )
    except Exception as e:
        print(f"Error sending document review notification: {e}")
    
    return {"message": f"Document {payload.docName} marked as {payload.status}"}



@app.post("/chat_upload")
async def upload_chat_file(
    file: UploadFile = File(...),
    from_user: str = Form(...),
    to_user: str = Form(...),
    chatId: str = Form(...)
):
    try:
        file_bytes = await file.read()
        file_doc = {
            "filename": file.filename,
            "content": Binary(file_bytes),
            "from_user": from_user,
            "to_user": to_user,
            "chatId": chatId,
            "timestamp": datetime.utcnow(),
            "size": len(file_bytes),
            "mime_type": file.content_type,
        }
        result = files_collection.insert_one(file_doc)
        file_doc["_id"] = str(result.inserted_id)

        # Optional: return all files for the chat
        docs = list(files_collection.find({"chatId": chatId}))
        for d in docs:
            d["_id"] = str(d["_id"])

        return {"status": "success", "file": file_doc, "all_chat_files": docs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_files/{chatId}")
async def get_files(chatId: str):
    docs = list(files_collection.find({"chatId": chatId}))
    return [{"name": d["name"], "type": d["type"], "data": d["data"]} for d in docs]

# ------------------ Upload Document ------------------

@app.post("/upload_document")
async def upload_document(
    userid: str = Form(...),
    docName: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # Read file content
        file_data = await file.read()

        # Create file document
        file_doc = {
            "userid": userid,
            "docName": docName,
            "file": Binary(file_data),
            "filename": file.filename,
            "content_type": file.content_type,
            "createdAt": datetime.utcnow()
        }

        # Insert into files collection
        result = assignments_collection.insert_one(file_doc)
        file_id = str(result.inserted_id)

        # Update assigned_docs with consistent field names
        result_update = Users.update_one(
            {"userid": userid, "assigned_docs.docName": docName},
            {"$set": {"assigned_docs.$.status": "Uploaded", "assigned_docs.$.fileId": file_id}}
        )

        # If no existing doc, append
        if result_update.matched_count == 0:
            Users.update_one(
                {"userid": userid},
                {"$push": {
                    "assigned_docs": {
                        "docName": docName,
                        "status": "Uploaded",
                        "fileId": file_id
                    }
                }}
            )
        
        # Send notification about document upload to reviewers
        try:
            # Get user info
            user = Users.find_one({"userid": userid})
            user_name = user.get("name", "User") if user else "User"
            
            # Send notification to HR and manager
            await Mongo.create_document_upload_notification(
                userid=userid,
                doc_name=docName,
                uploaded_by_name=user_name,
                uploaded_by_id=userid,
                reviewer_ids=None  # Will auto-detect HR and manager
            )
        except Exception as e:
            print(f"Error sending document upload notification: {e}")

        return {"message": "File uploaded successfully", "file_id": file_id}

    except Exception as e:
        print("Error storing file in MongoDB:", e)
        raise HTTPException(status_code=500, detail="500: Failed to save file in database")

# ------------------ Download Document ------------------
@app.get("/download_file/{file_id}")
def download_file(file_id: str):
    try:
        file_doc = assignments_collection.find_one({"_id": ObjectId(file_id)})
        if not file_doc:
            raise HTTPException(status_code=404, detail="File not found")

        return StreamingResponse(
            iter([file_doc["file"]]),
            media_type=file_doc.get("content_type", "application/octet-stream"),
            headers={"Content-Disposition": f'attachment; filename="{file_doc["filename"]}"'}
        )
    except Exception as e:
        print("Download error:", e)
        raise HTTPException(status_code=500, detail="Failed to download file")

    try:
        file_doc = assignments_collection.find_one({"_id": ObjectId(file_id)})
        if not file_doc:
            raise HTTPException(status_code=404, detail="File not found")

        # Delete file from collection
        assignments_collection.delete_one({"_id": ObjectId(file_id)})

        # Update user's assigned_docs to remove fileId and set status to pending
        Users.update_one(
            {"userid": file_doc["userid"], "assigned_docs.fileId": file_id},
            {"$set": {"assigned_docs.$.status": "Pending", "assigned_docs.$.fileId": None}}
        )

        return {"message": "File deleted successfully"}
    except Exception as e:
        print("Delete error:", e)
        raise HTTPException(status_code=500, detail="Failed to delete file")

@app.delete("/documents/delete/{file_id}")
def delete_file(file_id: str):
    try:
        file_doc = assignments_collection.find_one({"_id": ObjectId(file_id)})  
        if not file_doc:
            raise HTTPException(status_code=404, detail="File not found")

        # Delete file from collection
        assignments_collection.delete_one({"_id": ObjectId(file_id)})

        # Update user's assigned_docs
        Users.update_one(
            {"userid": file_doc["userid"], "assigned_docs.fileId": file_id},
            {"$set": {"assigned_docs.$.status": "Pending", "assigned_docs.$.fileId": None}}
        )

        return {"message": "File deleted successfully"}
    except Exception as e:
        print("Delete error:", e)
        raise HTTPException(status_code=500, detail="Failed to delete file")

@app.delete("/assigned_doc_delete")
async def delete_assigned_doc(data: dict):
    userId = data.get("userId")
    docName = data.get("docName")

    user = Users.find_one({"userid": userId})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    Users.update_one(
        {"userid": userId},
        {"$pull": {"assigned_docs": {"docName": docName}}}
    )

    return {"message": f"Document '{docName}' deleted successfully"}

from fastapi import Response

@app.get("/view_file/{file_id}")
async def view_file(file_id: str):
    file_doc = files_collection.find_one({"_id": ObjectId(file_id)})
    if not file_doc:
        raise HTTPException(status_code=404, detail="File not found")
    return Response(
        content=file_doc["file"],
        media_type=file_doc["content_type"],
        headers={"Content-Disposition": f"inline; filename={file_doc['filename']}"}
    )

@app.post("/create_group")
async def create_group(group: GroupCreate):
    group_id = str(uuid.uuid4())
    doc = {
        "_id": group_id,
        "name": group.name,
        "members": group.members,
        "created_at": datetime.utcnow()
    }
    groups_collection.insert_one(doc)
    return {"status": "success", "group_id": group_id, "name": group.name}

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

@app.get("/get_user_groups/{user_id}")
async def get_user_groups(user_id: str):
    # Fetch groups where user is a member
    groups_cursor = groups_collection.find({"members": user_id})
    groups = list(groups_cursor)  # <--- await here

    # Convert MongoDB ObjectId and datetime to JSON-safe
    groups_json = jsonable_encoder(groups)

    return JSONResponse(content=groups_json)


@app.get("/group_members/{group_id}")
async def get_group_members(group_id: str):
    group = groups_collection.find_one({"_id": group_id})
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    members = list(Users.find({"_id": {"$in": group.get("members", [])}}, {"name": 1, "depart": 1}))
    # Convert ObjectId to string for frontend
    for m in members:
        m["_id"] = str(m["_id"])
    return members



@app.websocket("/ws/group/{group_id}")
async def websocket_group(websocket: WebSocket, group_id: str):
    await group_ws_manager.connect(group_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Add timestamp & unique id
            data["timestamp"] = datetime.utcnow().isoformat() + "Z"
            data["id"] = data.get("id") or str(ObjectId())

            # Save to MongoDB
            messages_collection.insert_one({
                "chatId": group_id,
                "from_user": data.get("from_user"),
                "text": data.get("text"),
                "file": data.get("file"),
                "timestamp": data["timestamp"]
            })

            # Broadcast to all group members
            await group_ws_manager.broadcast(group_id, data)
            
            # Create group chat notifications
            try:
                sender_id = data.get("from_user")
                message_text = data.get("text", "")
                
                # Get group info
                group = groups_collection.find_one({"_id": group_id})
                if group and message_text:
                    group_name = group.get("name", "Group")
                    member_ids = group.get("members", [])
                    
                    # Get sender name
                    sender = Users.find_one({"userid": sender_id})
                    sender_name = sender.get("name", "Unknown User") if sender else "Unknown User"
                    
                    # Send notifications to all members except sender
                    await Mongo.create_group_chat_notification(
                        sender_id=sender_id,
                        group_id=group_id,
                        sender_name=sender_name,
                        group_name=group_name,
                        message_preview=message_text,
                        member_ids=member_ids
                    )
            except Exception as e:
                print(f"Error creating group chat notification: {e}")
                
    except Exception as e:
        print("WS disconnected", e)
    finally:
        group_ws_manager.disconnect(group_id, websocket)


# Fetch group chat history
@app.get("/group_history/{group_id}")
async def group_history(group_id: str):
    cursor = messages_collection.find({"chatId": group_id}).sort("timestamp", 1)
    messages = []
    for doc in cursor:
        messages.append({
            "id": str(doc.get("_id")),
            "from_user": doc.get("from_user"),
            "text": doc.get("text"),
            "file": doc.get("file"),
            "timestamp": doc.get("timestamp").isoformat() if isinstance(doc.get("timestamp"), datetime) else doc.get("timestamp"),
            "chatId": doc.get("chatId")
        })
    return messages

@app.delete("/delete_group/{group_id}")
async def delete_group(group_id: str):
    result = groups_collection.delete_one({"_id": group_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
    
    # Optionally, delete all messages in that group
    messages_collection.delete_many({"chatId": group_id})
    
    return {"status": "success", "message": f"Group {group_id} deleted successfully"}

@app.put("/update_group/{group_id}")
async def update_group(group_id: str, group: GroupUpdate):
    result = groups_collection.update_one(
        {"_id": group_id},
        {"$set": {"name": group.name, "members": group.members, "updated_at": datetime.utcnow()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"status": "success", "group_id": group_id, "name": group.name}

# ===============================
# ENHANCED TASK NOTIFICATION ENDPOINTS
# ===============================

@app.post("/tasks/{taskid}/comments")
async def add_task_comment(
    taskid: str,
    comment: str = Form(...),
    userid: str = Form(...)
):
    """Add comment to task and send notifications"""
    try:
        # Get current task
        task = Mongo.Tasks.find_one({"_id": ObjectId(taskid)})
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        # Create comment object
        comment_obj = {
            "id": str(uuid.uuid4()),
            "text": comment,
            "userId": userid,
            "timestamp": datetime.now().isoformat(),
            "userName": ""  # Will be populated from user data
        }
        
        # Get user name
        user = Mongo.Users.find_one({"_id": ObjectId(userid)})
        if user:
            comment_obj["userName"] = user.get("name", "Unknown User")
        
        # Add comment to task
        Mongo.Tasks.update_one(
            {"_id": ObjectId(taskid)},
            {"$push": {"comments": comment_obj}}
        )
        
        # Send notifications
        task_title = task.get("task", "Task")
        task_userid = task.get("userid")
        
        # Get commenter name
        commenter = Mongo.Users.find_one({"_id": ObjectId(userid)})
        commenter_name = commenter.get("name", "Team Member") if commenter else "Team Member"
        
        # Notify task owner if comment is by someone else
        if task_userid and userid != task_userid:
            Mongo.create_notification(
                userid=task_userid,
                title="New Comment Added",
                message=f"{commenter_name} added a comment to your task '{task_title}': '{comment[:100]}{'...' if len(comment) > 100 else ''}'",
                notification_type="task",
                priority="medium",
                action_url=Mongo.get_role_based_action_url(task_userid, "task"),
                related_id=taskid,
                metadata={
                    "task_title": task_title,
                    "action": "Comment Added",
                    "comment_text": comment,
                    "commented_by": userid
                }
            )
        
        # Notify manager if they exist and didn't make the comment
        assigned_by = task.get("assigned_by")
        if assigned_by and assigned_by != "self" and assigned_by != userid and assigned_by != task_userid:
            Mongo.create_notification(
                userid=assigned_by,
                title="Comment Added to Assigned Task",
                message=f"{commenter_name} added a comment to the task '{task_title}': '{comment[:100]}{'...' if len(comment) > 100 else ''}'",
                notification_type="task",
                priority="medium",
                action_url=Mongo.get_role_based_action_url(assigned_by, "manager_task"),
                related_id=taskid,
                metadata={
                    "task_title": task_title,
                    "action": "Comment Added",
                    "comment_text": comment,
                    "commented_by": userid
                }
            )
        
        return {"message": "Comment added successfully", "comment_id": comment_obj["id"]}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks/{taskid}/subtasks")
async def add_task_subtask(
    taskid: str,
    subtask_text: str = Form(...),
    assigned_by: str = Form(...)
):
    """Add subtask to task and send notifications"""
    try:
        # Get current task
        task = Mongo.Tasks.find_one({"_id": ObjectId(taskid)})
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        # Create subtask object
        subtask_obj = {
            "id": int(datetime.now().timestamp()),
            "text": subtask_text,
            "completed": False,
            "assignedBy": assigned_by,
            "createdAt": datetime.now().isoformat()
        }
        
        # Add subtask to task
        Mongo.Tasks.update_one(
            {"_id": ObjectId(taskid)},
            {"$push": {"subtasks": subtask_obj}}
        )
        
        # Send notifications
        task_title = task.get("task", "Task")
        task_userid = task.get("userid")
        
        # Get assigner name
        assigner = Mongo.Users.find_one({"_id": ObjectId(assigned_by)}) if ObjectId.is_valid(assigned_by) else None
        assigner_name = assigner.get("name", "Manager") if assigner else "Manager"
        
        if task_userid:
            Mongo.create_notification(
                userid=task_userid,
                title="Subtask Added",
                message=f"{assigner_name} added a new subtask '{subtask_text}' to your task '{task_title}'.",
                notification_type="task",
                priority="medium",
                action_url=Mongo.get_role_based_action_url(task_userid, "task"),
                related_id=taskid,
                metadata={
                    "task_title": task_title,
                    "action": "Subtask Added",
                    "subtask_text": subtask_text,
                    "assigned_by": assigned_by
                }
            )
        
        return {"message": "Subtask added successfully", "subtask_id": subtask_obj["id"]}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tasks/trigger-deadline-reminders")
async def trigger_deadline_reminders():
    """Manually trigger deadline reminder checks"""
    try:
        import asyncio
        from notification_automation import check_upcoming_deadlines, check_and_notify_overdue_tasks
        
        # Check upcoming deadlines
        upcoming_result = await check_upcoming_deadlines()
        
        # Check overdue tasks
        overdue_result = await check_and_notify_overdue_tasks()
        
        return {
            "message": "Deadline reminder checks completed",
            "upcoming_deadlines": upcoming_result,
            "overdue_tasks": overdue_result,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))