import React, { useEffect } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter,createBrowserRouter, Outlet, Route, RouterProvider, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./index.css";
import App from "./App";
import Clockin from "./components/Clockin";
import Sidebar from "./components/Sidebar";
import Checkauth from "./Utils/Checkauth";
import Setting from "./components/Setting";
import Clockdashboard from "./components/Clockdashboard";
import Clockin_int from "./components/Clockin_int";
import Leave from "./components/leave/Leave";
import LeaveHistory from "./components/leave/LeaveHistory";
import Leaverequest from "./components/leave/Leaverequest";
import Holidaylist from "./components/Holidayslist";
import Workfromhome from "./components/leave/Workfromhome";
import Remote_details from "./components/leave/Remote_details";
import UserProfile from "./components/UserProfile";
import Timemanagement from "./components/Adminfrontend/Timemanagement";
import Employeelist from "./components/Adminfrontend/Employeelist";
import Leavemanagement from "./components/Adminfrontend/leave/Leavemanagement";
import Leaveapproval from "./components/Adminfrontend/leave/Leave_approval";
import Wfh from "./components/Adminfrontend/leave/Wfh_approval";
import AdminProfile from "./components/Adminfrontend/Adminprofile";
import AddUser from "./components/Adminfrontend/new_employee";
import EmployeeDetails from "./components/EmployeeDetails";
import LoginPage from "./components/Loginpage";
import Navbar from "./components/Navbar";
import ProgressDetail from './components/Task/ProgressDetail';
import TaskAssign from './components/Task/TaskAssign';
import TaskDetailsPage from "./components/Task/TaskDetailsPage";
import TaskPage from "./components/Task/Taskpage";
import TaskProgress from "./components/Task/TaskProgress";
import ToDoList from "./components/Task/Todo";
import NotificationDashboard from "./components/NotificationDashboard";
import EnhancedNotificationDashboard from "./components/EnhancedNotificationDashboard";
import ApiTest from "./components/ApiTest";
import AdminAuth from "./Utils/AdminAuth";


import Attendance from "./components/Adminfrontend/Attendance";
import AddLeave from "./components/Adminfrontend/leave/AddLeave";
import AttendanceStats from "./components/AttendanceStats";
import LeaveDetails from "./components/Adminfrontend/leave/LeaveDetails";
import RemoteDetails from "./components/Adminfrontend/leave/RemoteDetails";
import Chat from './components/Chat';
import OnboardingDocs from './components/OnboardingDocs';
import HRDocsReview from './components/Adminfrontend/AdminDocsReview';

import Fileuploader from './components/Fileuploader';
import GlobalNotificationToast from './components/GlobalNotificationToast';



// Create a simple dashboard home component for admin
const DashboardHome = () => (
  <div className="p-6">
    <h1 className="text-2xl font-bold text-gray-800 mb-4">Admin Dashboard</h1>
    <p className="text-gray-600">Welcome to the admin panel. Select an option from the sidebar to get started.</p>
  </div>
);

const DashboardPage = () => (
  <Checkauth>
    <div className="flex h-screen w-full flex-col lg:flex-row">
      <Sidebar />
      <div
        id="temp"
        className="h-full w-full overflow-x-hidden flex justify-center items-center"
      >
        <Outlet />
      </div>
      {/* Global Toast Notifications */}
      <GlobalNotificationToast />
    </div>
  </Checkauth>
);

const AdminDashboardPage = () => (
  <AdminAuth>
    <DashboardPage />
  </AdminAuth>
);

/*const rou = [];
const tempdata = [
  rou.map((item) => {
    return item;
  }),
];*/



const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
     { index: true, element: <LoginPage /> }, 
  ],
  },
  {
    path: "/Login",
    element: <LoginPage />,
  },
  {
    path: "/websocket-test",
    element: <NotificationDashboard />,
  },
  // {path:"Login",
  // element:<LoginPage />
  // },
  {
    path: "/User",
    element: <DashboardPage />,
    children: [
      { path: "", element: <></> },
      {
        path: "Clockin_int",
        element: <Clockin_int />,
        children: [
          { path: "", element: <Clockin /> },
          { path: "Clockdashboard", element: <Clockdashboard /> },
        ],
      },
      {
        path: "Setting",
        element: <Setting />,
      },
      {
        path: "profile",
        element: <UserProfile />,
      },
        {
      path: "Task/Todo",
      element: <ToDoList />,
    },
    {
      path: "Task/Todo/TaskPage",
      element: <TaskPage />,
    },
    {
      path: "Task/Todo/TaskPage/TaskDetailsPage/:taskId",
      element: <TaskDetailsPage />,
    },
      {
        path: "Leave",
        element: <Leave />,
      },
      {
        path: "LeaveHistory",
        element: <LeaveHistory />,
      },
      {
        path: "Holidaylist",
        element: <Holidaylist />,
      },
      {
        path: "Workfromhome",
        element: <Workfromhome />,
      },
      {
        path: "Leaverequest",
        element: <Leaverequest />,
      },
      {
        path: "Remote_details",
        element: <Remote_details />,
      },
      {
        path: "notifications",
        element: <NotificationDashboard />,
      },
      {
        path: "enhanced-notifications",
        element: <EnhancedNotificationDashboard />,
      },
      {
        path: "test",
        element: <ApiTest />,
},
{
  path: "LeaveManage",
  element: <Leavemanagement />,
},
{
  path: "newUser",
  element: <AddUser />,
},
{
  path: "leaveapproval",
  element: <Leaveapproval />,
},
{
  path: "wfh",
  element: <Wfh />,
},
{
  path: 'chat',
  element: <Chat />, // your Slack-like chat component
},
{
        path: "timemanage",
        element: <Timemanagement />,
      },
    {
      path: "Task/TaskProgress",
      element: <TaskProgress/>,
    },
    {path:"/User/Task/TaskProgress/ProgressDetail/:taskId",
      element:<ProgressDetail role="manager" dashboardRoute="/User/Task/TaskProgress" commentLabel="TeamLead" fileUploadLabel="TeamLead" />, 
    },
    {path:"/User/Task/TaskProgress/ProgressDetail/:taskId",
      element:<ProgressDetail role="hr" dashboardRoute="/User/Task/TaskProgress" commentLabel="HR" fileUploadLabel="HR" />, 
    },
    {
      path: "Task/TaskProgress/TaskAssign",
      element: <TaskAssign assignType="TL-to-employee" />
    },
    {
      path: "Task/TaskProgress/TaskAssign",
      element: <TaskAssign assignType="hr-to-TL" />
    },
 {
        path:'my-documents',
        element:<OnboardingDocs/>,
        
      },
      {
          path: 'fileuploader',
          element:<Fileuploader/>,
        },
{ path: "leave_details", element: <LeaveDetails /> },
{ path: "wfh_details", element: <RemoteDetails />},
{ path: "attendance", element: <Attendance />},
{ path: "individualStats", element: <AttendanceStats />},
    ],
  },
  {
    path: "/admin",
    element: <AdminDashboardPage />,
    children: [
      {
        path: "",
        element: <></>,
      },
      {
        path: "leave",
        element: <Leavemanagement />,
      },
      {
        path: 'chat',
        element: <Chat />, // your Slack-like chat component
      },
      {
        path: "time",
        element: <Timemanagement />,
      },
      {
        path: "employee",
        element: <Employeelist />,
        // children:[{
        //   path:':id',
        //   element:<EmployeeDetails/>
        // },],
      },
      {
        path: "leaveapproval",
        element: <Leaveapproval />,
      },
      {
        path: "wfh",
        element: <Wfh />,
      },
      {
        path: "profile",
        element: <AdminProfile />,
      },
      {
        path: "newUser",
        element: <AddUser />,
      },
      {
        path: "task",
        element: <TaskPage />,
      },
      {
        path: "notifications",
        element: <NotificationDashboard />,
      },
      {
        path: "enhanced-notifications",
        element: <EnhancedNotificationDashboard />,
      },
      {
        path:':id',
        element:<EmployeeDetails/>
      },
      {
        path: 'review-docs',
        element: <HRDocsReview />,
      },
      {
  path: 'chat',
  element: <Chat />, 
},
      
      
      { index: true, element: <DashboardHome /> }, // default admin page
      { path: "leave", element: <Leavemanagement /> },
      { path: "time", element: <Timemanagement /> },
      { path: "employee", element: <Employeelist /> },
      { path: "employee/:id", element: <EmployeeDetails /> },
      { path: "leaveapproval", element: <Leaveapproval /> },
      { path: "leave_details", element: <LeaveDetails /> },
      { path: "wfh", element: <Wfh /> },
      { path: "wfh_details", element: <RemoteDetails />},
      { path: "profile", element: <AdminProfile /> },
      { path: "attendance", element: <Attendance />},
      { path: "newUser", element: <AddUser /> },
      { path: "leave/addLeave", element: <AddLeave /> },
    ],
  }, // Fixed: Added missing comma here
]);

const MainApp = () => {
  useEffect(() => {
    const handleBeforeUnload = (event) => {
      const isRunning = localStorage.getItem("isRunning") === "true";
      if (isRunning) {
        const confirmationMessage = "Are you sure you want to leave?";
        event.preventDefault();
        event.returnValue = confirmationMessage;
        return confirmationMessage;
      }
    };

    window.addEventListener("beforeunload", handleBeforeUnload);
    return () => {
      window.removeEventListener("beforeunload", handleBeforeUnload);
    };
  }, []);

  return (
    <>
      <RouterProvider router={router}>
        <Outlet />
        <BrowserRouter>
        <Routes>
          <Route path="/admin/employee" element={<Employeelist/>}/>
          <Route path="/admin/employee/:id" element={<EmployeeDetails/>}/>
        </Routes>
        
        </BrowserRouter>
      </RouterProvider>
      
      <ToastContainer
        position="top-right"
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={true}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss={false}
        draggable
        pauseOnHover
        theme="light"
        limit={3}
      />
    </>
  );
  //return <RouterProvider router={router} />;
};

createRoot(document.getElementById("root")).render(<MainApp />);