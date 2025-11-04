import { useState, useEffect, useMemo, useRef } from "react";
import {
  Check,
  FileText,
  X,
  User,
  PlusCircle,
  Upload,
  CheckCircle,
  Clock,
  Trash2,
  Eye,
  Search,
  Filter,
  ChevronDown,
  ChevronUp,
  Users,
  ClipboardList,
  AlertTriangle,
  BarChart3,
} from "lucide-react";
import axios from "axios";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { ipadr } from "../../Utils/Resuse";

export default function AdminDocsReview() {
  const headerRef = useRef(null);
  const [users, setUsers] = useState([]);
  const [selectedUsers, setSelectedUsers] = useState([]);
  const [newDocName, setNewDocName] = useState("");
  const [assignedDocs, setAssignedDocs] = useState({});
  const [reviewUser, setReviewUser] = useState(null);
  const [loadingUsers, setLoadingUsers] = useState(false);
  const [loadingAssign, setLoadingAssign] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");
  const [showStats, setShowStats] = useState(false);
  const [selectedUserId, setSelectedUserId] = useState(null);
  const [assignModal, setAssignModal] = useState(false);

  useEffect(() => {
    fetchUsers();
  }, []);

  useEffect(() => {
    const setHeaderVar = () => {
      const h = headerRef.current ? headerRef.current.offsetHeight : 0;
      document.documentElement.style.setProperty('--adr-header-height', `${h}px`);
    };
    setHeaderVar();
    window.addEventListener('resize', setHeaderVar);
    return () => window.removeEventListener('resize', setHeaderVar);
  }, [showStats, searchTerm, statusFilter]);

 const fetchUsers = async () => {
  try {
    setLoadingUsers(true);
    const res = await axios.get(`${ipadr}/get_all_users`);
    const normalizedUsers = res.data
      .map((u) => ({
        ...u,
        userId: u.id || u._id || u.userId,
      }))
      .filter((u) => u.position?.toLowerCase() !== "admin");

    setUsers(normalizedUsers);
    await Promise.all(normalizedUsers.map((user) => fetchAssignedDocs(user.userId)));
  } catch (err) {
    console.error("Error fetching users:", err);
    toast.error("Failed to fetch users");
  } finally {
    setLoadingUsers(false);
  }
};


  const fetchAssignedDocs = async (userId) => {
    try {
      const res = await axios.get(`${ipadr}/documents/assigned/${userId}`);
      setAssignedDocs((prev) => ({ ...prev, [userId]: res.data }));
    } catch (err) {
      console.error(`Error fetching docs for user ${userId}:`, err);
    }
  };

  const toggleUserSelection = (userId) => {
    setSelectedUsers((prev) =>
      prev.includes(userId) ? prev.filter((id) => id !== userId) : [...prev, userId]
    );
  };

  const handleAssignDocument = async () => {
    if (!selectedUsers.length) {
      toast.warning("Select at least 1 user.");
      return;
    }
    if (!newDocName.trim()) {
      toast.warning("Enter a document name.");
      return;
    }
    const docNameTrimmed = newDocName.trim();

    try {
      setLoadingAssign(true);
      setAssignedDocs((prev) => {
        const updated = { ...prev };
        selectedUsers.forEach((uid) => {
          const prevDocs = prev[uid] || [];
          updated[uid] = [
            ...prevDocs,
            { docName: docNameTrimmed, status: "pending", assignedBy: "Admin", fileUrl: null },
          ];
        });
        return updated;
      });

      await axios.post(`${ipadr}/assign_docs`, {
        userIds: selectedUsers,
        docName: docNameTrimmed,
      });

      await Promise.all(selectedUsers.map((uid) => fetchAssignedDocs(uid)));
      setNewDocName("");
      setSelectedUsers([]);
      toast.success("Document assigned successfully!");
      setAssignModal(false);
    } catch (err) {
      console.error(err);
      toast.error("Failed to assign document");
    } finally {
      setLoadingAssign(false);
    }
  };

  const handleVerify = async (userId, docName) => {
    try {
      await axios.put(`${ipadr}/review_document`, {
        userId,
        docName,
        status: "verified",
        remarks: "Verified by HR",
      });
      await fetchAssignedDocs(userId);
      toast.success("Document verified successfully!");
    } catch (err) {
      console.error(err);
      toast.error("Verification failed");
    }
  };

  const handleDelete = (userId, docName) => {
    toast(
      ({ closeToast }) => (
        <div className="flex flex-col gap-2">
          <span>Are you sure you want to delete <strong>{docName}</strong>?</span>
          <div className="flex justify-end gap-2">
            <button
              onClick={async () => {
                closeToast();
                try {
                  await axios.delete(`${ipadr}/assigned_doc_delete`, {
                    data: { userId, docName },
                  });
                  setAssignedDocs((prev) => ({
                    ...prev,
                    [userId]: (prev[userId] || []).filter((d) => d.docName !== docName),
                  }));
                  toast.success("Document deleted successfully!");
                } catch (err) {
                  console.error(err);
                  toast.error("Failed to delete document");
                }
              }}
              className="px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600 text-xs"
            >
              Yes
            </button>
            <button
              onClick={closeToast}
              className="px-3 py-1 bg-gray-300 text-gray-800 rounded hover:bg-gray-400 text-xs"
            >
              No
            </button>
          </div>
        </div>
      ),
      {
        autoClose: false,
        closeOnClick: false,
        draggable: false,
      }
    );
  };

  const filteredUsers = useMemo(() => {
    return users.filter((user) => {
      const matchesSearch = user.name?.toLowerCase().includes(searchTerm.toLowerCase());
      
      if (statusFilter === "all") return matchesSearch;
      
      const userDocs = assignedDocs[user.userId] || [];
      const hasStatus = userDocs.some(doc => {
        if (statusFilter === "pending") return !doc.fileUrl;
        if (statusFilter === "uploaded") return doc.fileUrl && doc.status !== "verified";
        if (statusFilter === "verified") return doc.status === "verified";
        return true;
      });

      return matchesSearch && hasStatus;
    });
  }, [users, searchTerm, statusFilter, assignedDocs]);

  const filterDocsByStatus = (docs) => {
    if (statusFilter === "all") return docs;
    return docs.filter((doc) => {
      if (statusFilter === "pending") return !doc.fileUrl;
      if (statusFilter === "uploaded") return doc.fileUrl && doc.status !== "verified";
      if (statusFilter === "verified") return doc.status === "verified";
      return true;
    });
  };

 const UserCard = ({ user }) => {
  const handleCardClick = () => {
    setSelectedUserId(user.userId);
    setReviewUser(user); 
  };
  const userDocs = assignedDocs[user.userId] || [];
  const statusCount = filterDocsByStatus(userDocs).length;

  return (
    <div
      onClick={handleCardClick}
      className="bg-white rounded-lg p-3 shadow-sm border cursor-pointer hover:shadow-lg transition-all mb-3 h-[100px] flex flex-col justify-between"
    >
      <div className="flex justify-between items-start">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-full bg-blue-600 flex items-center justify-center text-white font-semibold text-sm">
            {user.name?.[0]?.toUpperCase() || <User size={14} />}
          </div>
          <div className="leading-tight">
            <div className="flex items-center gap-2">
              <h4 className="font-semibold text-gray-800 text-sm">{user.name}</h4>
            </div>
            <p className="text-[11px] text-gray-500">{user.email || "—"}</p>
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between mt-1">
        <div className="flex items-center">
          {statusFilter !== 'all' && (
            <span className="text-xs px-2 py-0.5 rounded-full bg-blue-50 text-blue-800 font-medium">
              {statusCount} {statusFilter === 'pending' ? 'pending' : statusFilter === 'uploaded' ? 'uploaded' : 'verified'}
            </span>
          )}
        </div>

        <div className="flex items-center justify-end">
          <button
            onClick={(e) => {
              e.stopPropagation();
              setReviewUser(user);
            }}
            className="text-blue-600 hover:text-blue-800 text-xs flex items-center gap-1 hover:bg-blue-50 px-2 py-0.5 rounded transition-colors -mt-1"
          >
            <Eye size={11} /> Review
          </button>
        </div>
      </div>
    </div>
  );

};


  if (loadingUsers) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <div className="text-xl text-gray-600">Loading users...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col overflow-hidden bg-gray-50">
      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />

      <div ref={headerRef} className="bg-white shadow-sm border-b border-gray-200 p-4 shrink-0">
        <div className="flex justify-between items-center mb-3">
          <div>
            <h2 className="text-3xl font-bold font-inter pb-2 text-gray-800 bg-clip-text border-b-2">Document Management</h2>
          </div>
        </div>

<div className="flex justify-between items-start mb-4">
  <div className="bg-gradient-to-br from-gray-50 to-gray-100 p-2 rounded-xl border border-gray-200 shadow-sm w-[75%]">
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Search</label>
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={16} />
          <input
            type="text"
            placeholder="Search users by name..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="pl-10 pr-3 py-1.5 w-full border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
          />
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Status</label>
        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
          className="w-full p-1.5 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
        >
          <option value="all">All Status</option>
          <option value="pending">Pending</option>
          <option value="uploaded">Uploaded</option>
          <option value="verified">Verified</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Actions</label>
        <button
          onClick={() => {
            setSearchTerm('');
            setStatusFilter('all');
            setSelectedUsers([]);
          }}
          className="w-full px-3 py-1.5 bg-gray-500 text-white rounded-md hover:bg-gray-400 transition-colors text-sm"
        >
          Clear Filters
        </button>
      </div>
    </div>
  </div>

  <div className="ml-4 mt-[30px]">
    <button
      onClick={() => setAssignModal("select")}
      className="bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700 transition-all text-sm font-medium"
    >
      Assign Documents
    </button>
  </div>
</div>

      </div>
      <div className="flex-1 overflow-hidden p-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 overflow-y-auto" style={{ maxHeight: 'calc(100vh - var(--adr-header-height) - 32px)' }}>
          {filteredUsers.length === 0 ? (
            <div className="col-span-full text-center py-12">
              <ClipboardList className="mx-auto text-gray-400 mb-4" size={48} />
              <p className="text-gray-500 text-lg">No users found</p>
            </div>
          ) : (
            filteredUsers.map((user, index) => (
              <UserCard key={user.userId} user={user} index={index} />
            ))
          )}
        </div>
      </div>

{reviewUser && (
  <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex justify-center items-center z-50 p-4">
    <div className="bg-white rounded-2xl shadow-2xl w-full max-w-5xl max-h-[85vh] flex flex-col">
      <div className="flex justify-between items-center p-6 border-b border-gray-200 flex-shrink-0">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 bg-gradient-to-br from-blue-400 to-blue-600 text-white rounded-full flex items-center justify-center font-bold text-xl shadow-md">
            {reviewUser.name?.[0]?.toUpperCase() || <User size={24} />}
          </div>
          <div>
            <h2 className="text-2xl font-bold text-gray-800">{reviewUser.name}</h2>
            <p className="text-sm text-gray-500">Document Review & Management</p>
          </div>
        </div>
        <button
          className="text-gray-400 hover:text-gray-600 transition-colors p-2 hover:bg-gray-100 rounded-full"
          onClick={() => setReviewUser(null)}
        >
          <X size={24} />
        </button>
      </div>

<div className="flex-1 p-6">
  <div className="border rounded-t-lg bg-[#6d9eeb7a]">
    <table className="min-w-full border-collapse">
      <thead className="text-xs font-semibold uppercase text-black">
        <tr>
          <th className="p-3 text-left w-[45%]">Document</th>
          <th className="p-3 text-center w-[20%]">
            <div className="flex justify-center items-center gap-1">
              <span>Status</span>
            </div>
          </th>
          <th className="p-3 text-center w-[20%]">
            <div className="flex justify-center items-center gap-1">
              <span>Actions</span>
            </div>
          </th>
        </tr>
      </thead>
    </table>
  </div>

  <div className="overflow-y-auto max-h-[400px] border border-t-0 rounded-b-lg">
    <table className="min-w-full border-collapse table-fixed">
    <tbody className="text-sm divide-y divide-gray-100">
  {filterDocsByStatus(assignedDocs[reviewUser.userId] || []).length === 0 ? (
    <tr>
      <td colSpan="4" className="p-8 text-center text-gray-400">
        No documents found.
      </td>
    </tr>
  ) : (
    filterDocsByStatus(assignedDocs[reviewUser.userId] || [])
      .slice() 
      .reverse()
      .map((doc) => (
        <tr key={doc.docName} className="hover:bg-blue-50 transition-colors">
          <td className="p-3 align-middle w-[45%]">
            <div className="flex items-center gap-2 text-gray-800">
              <FileText size={18} className="text-blue-500 flex-shrink-0" />
              <span className="font-medium truncate">{doc.docName}</span>
            </div>
          </td>

         <td className="p-3 text-center align-middle w-[20%]">
  <div className="flex justify-center gap-4">
    {doc.status === "verified" ? (
      <div
        className="text-green-600 hover:text-green-800 transition"
        title="Verified"
      >
        <CheckCircle size={18} />
      </div>
    ) : doc.fileUrl ? (
      <div
        className="text-blue-600 hover:text-blue-800 transition"
        title="Uploaded"
      >
        <Upload size={18} />
      </div>
    ) : (
      <div
        className="text-gray-600 hover:text-gray-800 transition"
        title="Pending"
      >
        <Clock size={18} />
      </div>
    )}
  </div>
</td>


          <td className="p-3 text-center align-middle w-[20%]">
            <div className="flex justify-center gap-4">
              {doc.fileUrl && (
                <a
                  href={`${ipadr}${doc.fileUrl}`}
                  target="_blank"
                  rel="noreferrer"
                  className="text-blue-600 hover:text-blue-800 transition"
                  title="View Document"
                >
                  <Eye size={18} />
                </a>
              )}
            
              {doc.fileUrl && doc.status !== "verified" && (
                <button
                  onClick={() => handleVerify(reviewUser.userId, doc.docName)}
                  className="text-green-600 hover:text-green-800 transition"
                  title="Verify Document"
                >
                  <Check size={18} />
                </button>
              )}
              <button
                onClick={() => handleDelete(reviewUser.userId, doc.docName)}
                className="text-red-600 hover:text-red-800 transition"
                title="Delete Document"
              >
                <Trash2 size={18} />
              </button>
            </div>
          </td>
        </tr>
      ))
  )}
</tbody>

    </table>
  </div>
</div>

    </div>
  </div>
)}

{assignModal === "select" && (
  <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex justify-center items-center z-50 p-4">
    <div className="bg-white rounded-2xl shadow-2xl w-full max-w-lg">
      <div className="flex justify-between items-center p-4 border-b border-gray-200">
        <h3 className="text-xl font-semibold text-gray-800">Select Users</h3>
        <button
          onClick={() => setAssignModal(false)}
          className="text-gray-400 hover:text-gray-600 p-1 rounded-full hover:bg-gray-100"
        >
          <X size={20} />
        </button>
      </div>

      <div className="p-4">
        <p className="text-sm text-gray-600 mb-3">
          Select one or more users to assign documents.
        </p>

        <div className="max-h-60 overflow-y-auto border rounded-md p-2">
          {users.map((u) => (
            <label
              key={u.userId}
              className="flex items-center gap-2 py-1 text-sm cursor-pointer"
            >
              <input
                type="checkbox"
                checked={selectedUsers.includes(u.userId)}
                onChange={() => toggleUserSelection(u.userId)}
                className="text-blue-600 rounded border-gray-300"
              />
              <span className="text-gray-700">{u.name}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 p-4 border-t border-gray-200">
  <p className="text-sm text-gray-600 text-center w-full sm:w-auto">
    <strong>{selectedUsers.length}</strong> user
    {selectedUsers.length > 1 ? "s are" : " is"} selected.
  </p>

  <div className="flex justify-end gap-3 w-full sm:w-auto">
    <button
      onClick={() => setAssignModal(false)}
      className="px-4 py-2 text-sm rounded-md bg-gray-200 text-gray-700 hover:bg-gray-300"
    >
      Cancel
    </button>
    <button
      onClick={() => {
        if (selectedUsers.length === 0) {
          toast.warning("Select at least one user");
          return;
        }
        setAssignModal("confirm");
      }}
      className="px-4 py-2 text-sm rounded-md bg-blue-600 text-white hover:bg-blue-700"
    >
      Next
    </button>
  </div>
</div>
    </div>
  </div>
)}

{assignModal === "confirm" && (
  <div className="fixed inset-0 bg-black/40 backdrop-blur-sm flex justify-center items-center z-50 p-4">
    <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md">
      <div className="flex justify-between items-center p-4 border-b border-gray-200">
        <h3 className="text-xl font-semibold text-gray-800">Assign Documents</h3>
        <button
          onClick={() => setAssignModal("select")}
          className="text-gray-400 hover:text-gray-600 p-1 rounded-full hover:bg-gray-100"
        >
          <X size={20} />
        </button>
      </div>

      <div className="p-4">
        <p className="text-sm text-gray-600 mb-3"> 
          Enter the document name to assign.
        </p>

        <div className="relative">
          <FileText
            size={16}
            className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
          />
          <input
            type="text"
            placeholder="Enter document name..."
            value={newDocName}
            onChange={(e) => setNewDocName(e.target.value)}
            className="w-full pl-9 pr-3 py-2 border rounded-md focus:ring-2 focus:ring-blue-500 text-sm"
          />
        </div>
      </div>

      <div className="flex justify-end gap-3 p-4 border-t border-gray-200">
        <button
          onClick={() => setAssignModal("select")}
          className="px-4 py-2 text-sm rounded-md bg-gray-200 text-gray-700 hover:bg-gray-300"
        >
          Back
        </button>
        <button
          onClick={handleAssignDocument}
          disabled={loadingAssign}
          className="flex items-center gap-2 px-4 py-2 text-sm bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-60"
        >
          {loadingAssign ? (
            <>
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
              Assigning...
            </>
          ) : (
            <>
              <PlusCircle size={16} />
              Assign
            </>
          )}
        </button>
      </div>
    </div>
  </div>
)}
    </div>
  );
}