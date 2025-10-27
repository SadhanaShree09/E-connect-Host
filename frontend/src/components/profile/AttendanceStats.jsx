import React, { useState, useEffect } from "react";
import { Calendar, TrendingUp, Clock, UserCheck } from "lucide-react";
import { LS, ipadr } from "../../Utils/Resuse";

const API_BASE_URL = `${ipadr}`;

const AttendanceStats = ({ onClose = () => {} }) => {
  const userid = LS.get("userid");
  
  const getCurrentYear = () => new Date().getFullYear();
  const generateAvailableYears = () => {
    const currentYear = getCurrentYear();
    return [currentYear, currentYear - 1, currentYear - 2];
  };

  const [availableYears] = useState(generateAvailableYears());
  const [selectedYear, setSelectedYear] = useState(getCurrentYear());
  const [attendanceData, setAttendanceData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Compact Bar Chart Component
  const CustomBarChart = ({ data }) => {
    const maxCount = Math.max(...data.map(d => d.count));
    
    return (
      <div className="space-y-3">
        {data.map((item, index) => (
          <div key={index} className="space-y-1">
            <div className="flex justify-between items-center">
              <span className="text-xs font-medium text-gray-700">{item.metric}</span>
              <span className="text-xs text-gray-500">
                {item.count} days ({item.percentage.toFixed(1)}%)
              </span>
            </div>
            <div className="bg-gray-200 rounded-full h-6 relative overflow-hidden">
              <div
                className={`h-full ${item.bgColor} rounded-full transition-all duration-500 ease-out flex items-center justify-end pr-2`}
                style={{ 
                  width: `${maxCount > 0 ? (item.count / maxCount) * 100 : 0}%`,
                  minWidth: item.count > 0 ? '30px' : '0px'
                }}
              >
                <span className="text-white text-xs font-medium">
                  {item.count}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    );
  };

  const fetchAttendanceData = async (year) => {
    if (!userid) {
      setError("User ID is not available.");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}/attendance/user/${userid}?year=${year}`);
      
      if (response.ok) {
        const data = await response.json();
        setAttendanceData(data);
      } else {
        setError(`Failed to fetch attendance data for ${year}`);
      }
    } catch (err) {
      setError("Error fetching attendance data: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (userid) {
      fetchAttendanceData(selectedYear);
    }
  }, [selectedYear, userid]);

  const handleYearChange = (year) => {
    setSelectedYear(year);
  };

  const getChartData = () => {
    if (!attendanceData) return [];

    const stats = attendanceData.attendance_stats;
    return [
      {
        metric: "Present",
        count: stats.present_days,
        percentage: stats.attendance_percentage,
        bgColor: "bg-green-500"
      },
      {
        metric: "Leave",
        count: stats.leave_days_taken,
        percentage: stats.leave_percentage,
        bgColor: "bg-yellow-500"
      },
      {
        metric: "Absent",
        count: stats.total_working_days - stats.present_days - stats.leave_days_taken,
        percentage: 100 - stats.attendance_percentage - stats.leave_percentage,
        bgColor: "bg-red-500"
      }
    ];
  };

  const StatCard = ({ icon, title, value, subtitle }) => (
    <div className="bg-white p-3 rounded-lg border border-gray-200">
      <div className="flex items-center gap-2">
        <div className="p-2 rounded-lg bg-gray-50">
          {icon}
        </div>
        <div className="flex-1 min-w-0">
          <p className="text-xs text-gray-600 truncate">{title}</p>
          <p className="text-lg font-bold text-blue-600">{value}</p>
          {subtitle && <p className="text-xs text-gray-500">{subtitle}</p>}
        </div>
      </div>
    </div>
  );

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg max-w-4xl w-full max-h-[85vh] overflow-y-auto">
        {/* Compact Header */}
        <div className="flex items-center justify-between p-4 border-b border-gray-200 bg-gradient-to-r from-blue-50 to-indigo-50 sticky top-0 z-10">
          <div className="flex items-center gap-2">
            <Calendar className="h-5 w-5 text-blue-600" />
            <div>
              <h2 className="text-lg font-bold text-gray-800">Attendance Analytics</h2>
              <p className="text-xs text-gray-600">
                {attendanceData?.user_info?.name || "Employee"} - {selectedYear}
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <svg className="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="p-4 space-y-4">
          {/* Year Selector */}
          <div className="flex gap-2">
            {availableYears.map((year) => (
              <button
                key={year}
                onClick={() => handleYearChange(year)}
                className={`px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
                  selectedYear === year
                    ? "bg-blue-600 text-white"
                    : "bg-gray-100 text-gray-700 hover:bg-gray-200"
                }`}
              >
                {year}
              </button>
            ))}
          </div>

          {loading && (
            <div className="flex items-center justify-center py-8">
              <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-blue-600"></div>
              <span className="ml-2 text-sm text-gray-600">Loading...</span>
            </div>
          )}

          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-3">
              <div className="flex items-center">
                <svg className="w-4 h-4 text-red-600 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
                <span className="text-sm text-red-800">{error}</span>
              </div>
            </div>
          )}

          {attendanceData && !loading && (
            <>
              {/* Compact Stats Grid */}
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-3">
                <StatCard
                  icon={<Calendar className="h-4 w-4 text-blue-600" />}
                  title="Working Days"
                  value={attendanceData.attendance_stats.total_working_days}
                />
                <StatCard
                  icon={<UserCheck className="h-4 w-4 text-green-600" />}
                  title="Present"
                  value={attendanceData.attendance_stats.present_days}
                  subtitle={`${attendanceData.attendance_stats.attendance_percentage.toFixed(1)}%`}
                />
                <StatCard
                  icon={<Clock className="h-4 w-4 text-yellow-600" />}
                  title="Leave"
                  value={attendanceData.attendance_stats.leave_days_taken}
                  subtitle={`${attendanceData.attendance_stats.leave_percentage.toFixed(1)}%`}
                />
                <StatCard
                  icon={<TrendingUp className="h-4 w-4 text-purple-600" />}
                  title="Rate"
                  value={`${attendanceData.attendance_stats.attendance_percentage.toFixed(1)}%`}
                />
              </div>

              {/* Compact Chart */}
              <div className="bg-white border border-gray-200 rounded-lg p-4">
                <h3 className="text-sm font-semibold text-gray-800 mb-3">Breakdown</h3>
                <CustomBarChart data={getChartData()} />
              </div>

              {/* Compact Summary */}
              <div className="bg-gray-50 rounded-lg p-4">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                  <div className="space-y-1">
                    <p className="text-gray-600">
                      <span className="font-medium">Employee:</span> {attendanceData.user_info.name}
                    </p>
                    <p className="text-gray-600">
                      <span className="font-medium">Email:</span> {attendanceData.user_info.email}
                    </p>
                  </div>
                  <div className="space-y-1">
                    <p className="text-gray-600">
                      <span className="font-medium">Updated:</span>{" "}
                      {new Date(attendanceData.attendance_stats.last_updated).toLocaleDateString()}
                    </p>
                    <p className="text-gray-600">
                      <span className="font-medium">Status:</span>{" "}
                      <span className={`font-medium ${
                        attendanceData.attendance_stats.attendance_percentage >= 75 
                          ? 'text-green-600' 
                          : attendanceData.attendance_stats.attendance_percentage >= 60 
                          ? 'text-yellow-600' 
                          : 'text-red-600'
                      }`}>
                        {attendanceData.attendance_stats.attendance_percentage >= 75 
                          ? 'Excellent' 
                          : attendanceData.attendance_stats.attendance_percentage >= 60 
                          ? 'Good' 
                          : 'Needs Improvement'}
                      </span>
                    </p>
                  </div>
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default AttendanceStats;