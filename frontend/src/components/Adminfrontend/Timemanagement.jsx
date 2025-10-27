
import React, { useState, useEffect } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch, faDownload, faExclamationTriangle } from "@fortawesome/free-solid-svg-icons";
import axios from "axios";
import { ipadr } from "../../Utils/Resuse";
import "react-date-range/dist/styles.css";
import "react-date-range/dist/theme/default.css";
import { DateRangePicker } from "react-date-range";
import { format, isWithinInterval, parseISO, startOfDay, endOfDay } from 'date-fns';
import * as XLSX from 'xlsx';
import { LS } from "../../Utils/Resuse";

const Timemanagement = () => {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [attendanceData, setAttendanceData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedMonth, setSelectedMonth] = useState("");
  const [selectedYear, setSelectedYear] = useState(new Date().getFullYear().toString());
  const [searchTerm, setSearchTerm] = useState("");
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 5;
  const Admin = LS.get('isadmin');
  const [dateRange, setDateRange] = useState([
    {
      startDate: null,
      endDate: null,
      key: "selection",
    },
  ]);

  // Generate years array for dropdown (current year and past 5 years)
  const generateYears = () => {
    const currentYear = new Date().getFullYear();
    const years = [];
    for (let i = 0; i < 6; i++) {
      years.push((currentYear - i).toString());
    }
    return years;
  };

  const years = generateYears();

  // Fetch data when component mounts or when search/date changes
  useEffect(() => {
    fetchData();
  }, [selectedDate, searchTerm]);

  // Effect to filter data when date range, search term, or year changes
  useEffect(() => {
    filterData();
  }, [attendanceData, dateRange, searchTerm, selectedYear]);

  const fetchData = async () => {
    try {
      setLoading(true);
      // Request all attendance records, not just for a specific date
      const response = await axios.post(
        `${ipadr}/attendance/manage`,
        {}
      );
      const data = response.data && Array.isArray(response.data.attendance)
        ? response.data.attendance
        : [];
      setAttendanceData(data);
      setLoading(false);
      setError(null);
    } catch (error) {
      setLoading(false);
      setAttendanceData([]);
      setError("Error fetching data");
    }
  };

  const filterData = () => {
    let filtered = [...attendanceData];

    // Filter by search term
    if (searchTerm) {
      filtered = filtered.filter(item =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    // Filter by year if selected
    if (selectedYear) {
      filtered = filtered.filter(item => {
        const itemDate = parseISO(item.date);
        return itemDate.getFullYear().toString() === selectedYear;
      });
    }

    // Filter by date range
    if (dateRange[0].startDate && dateRange[0].endDate) {
      filtered = filtered.filter(item => {
        const itemDate = parseISO(item.date);
        return isWithinInterval(itemDate, {
          start: startOfDay(dateRange[0].startDate),
          end: endOfDay(dateRange[0].endDate)
        });
      });
    }

    setFilteredData(filtered);
    setCurrentPage(1); // Reset to first page when filters change
  };

  const handleDateRangeChange = (ranges) => {
    setDateRange([ranges.selection]);
    setSelectedMonth("");
    setSelectedYear("");
  };

  const formatDate = (date) => {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, "0");
    const day = date.getDate().toString().padStart(2, "0");
    return `${year}-${month}-${day}`;
  };

  const formatTime = (timeString) => {
    if (!timeString) return 'N/A';
    try {
      const date = new Date(timeString);
      // Check if date is valid
      if (isNaN(date.getTime())) return timeString;
      // Format as HH:MM:SS AM/PM
      return format(date, 'hh:mm:ss a');
    } catch (error) {
      console.error('Error formatting time:', error);
      return timeString;
    }
  };

  const formatDateOnly = (dateString) => {
    if (!dateString) return 'N/A';
    try {
      const date = new Date(dateString);
      // Check if date is valid
      if (isNaN(date.getTime())) return dateString;
      // Format as DD/MM/YYYY
      return format(date, 'dd/MM/yyyy');
    } catch (error) {
      console.error('Error formatting date:', error);
      return dateString;
    }
  };

  const formatDateTime = (timeString) => {
    if (!timeString) return 'N/A';
    try {
      const date = new Date(timeString);
      // Check if date is valid
      if (isNaN(date.getTime())) return timeString;
      // Format as DD/MM/YYYY HH:MM:SS AM/PM
      return format(date, 'dd/MM/yyyy hh:mm:ss a');
    } catch (error) {
      console.error('Error formatting datetime:', error);
      return timeString;
    }
  };

  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentItems = filteredData.slice(indexOfFirstItem, indexOfLastItem);

  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const downloadExcel = () => {
    // Format the data before exporting to match the table display
    const formattedData = filteredData.map((item, index) => ({
      'S.No': index + 1,
      'User ID': item.userid,
      'Name': item.name,
      'Date': formatDateOnly(item.date),
      'Clock In': formatTime(item.clockin),
      'Clock Out': formatTime(item.clockout),
      'Total Hours Worked': item.total_hours_worked || 'N/A',
      'Status': item.status,
      'Remark': item.remark || 'N/A'
    }));
    
    const worksheet = XLSX.utils.json_to_sheet(formattedData);
    
    // Auto-size columns
    const maxWidth = 20;
    const wscols = [
      { wch: 6 },  // S.No
      { wch: 15 }, // User ID
      { wch: 20 }, // Name
      { wch: 12 }, // Date
      { wch: 12 }, // Clock In
      { wch: 12 }, // Clock Out
      { wch: 18 }, // Total Hours Worked
      { wch: 10 }, // Status
      { wch: 15 }  // Remark
    ];
    worksheet['!cols'] = wscols;
    
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Attendance Data");
    
    // Generate filename with year and date range info
    let filename = 'attendance_data';
    if (selectedYear) {
      filename += `_${selectedYear}`;
    }
    if (dateRange[0].startDate && dateRange[0].endDate) {
      const startDate = format(dateRange[0].startDate, 'yyyy-MM-dd');
      const endDate = format(dateRange[0].endDate, 'yyyy-MM-dd');
      filename += `_${startDate}_to_${endDate}`;
    }
    filename += '.xlsx';
    
    XLSX.writeFile(workbook, filename);
  };

  return (
    
    <div className="mr-8 p-10 bg-white min-h-96 lg:min-h-[90vh] w-full shadow-black rounded-xl justify-center items-center relative jsonback ml-10 rounded-md">
      <div className="">
        <h1 className="text-5xl font-semibold font-inter pb-2 text-transparent bg-gradient-to-r from-zinc-600 to-zinc-950 bg-clip-text border-b-2">
          Clock In & Clock Out
        </h1>
        <div className="w-full bg-gradient-to-b from-white to-blue-50 shadow-lg rounded-xl border border-gray-200 my-2 mt-10">
          <header className="flex flex-wrap justify-between px-5 py-4 border-b border-gray-200 gap-4">
            <div className="flex items-center gap-4 flex-wrap">
              <div className="relative">
                <input
                  type="text"
                  placeholder="Search by name..."
                  className="px-2 py-1 rounded-md border text-sm pl-8 border-gray-300 w-40"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
                <div className="absolute top-0 left-0 mt-1 ml-2 text-gray-400 cursor-text">
                  <FontAwesomeIcon icon={faSearch} />
                </div>
              </div>

              <div className="flex items-center gap-2">
                <label className="text-sm font-medium text-gray-700">Year:</label>
                <select
                  value={selectedYear}
                  onChange={(e) => {
                    setSelectedYear(e.target.value);
                    // Clear date range when year is selected
                    if (e.target.value) {
                      setDateRange([{
                        startDate: null,
                        endDate: null,
                        key: "selection",
                      }]);
                    }
                  }}
                  className="px-3 py-1 rounded-md border border-gray-300 text-sm bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="">All Years</option>
                  {years.map(year => (
                    <option key={year} value={year}>{year}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="flex items-center gap-4">
              <div className="relative">
                <button
                  onClick={() => setShowDatePicker(!showDatePicker)}
                  className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition-colors text-sm"
                >
                  {showDatePicker ? 'Hide Date Range' : 'Show Date Range'}
                </button>
                {showDatePicker && (
                  <div className="absolute right-0 top-12 z-50 bg-white shadow-xl rounded-md border">
                    <DateRangePicker
                      ranges={dateRange}
                      onChange={handleDateRangeChange}
                      moveRangeOnFirstSelection={false}
                    />
                  </div>
                )}
              </div>
            </div>
          </header>

          <div className="p-3">
            <div>
              {error && <p className="text-red-500">{error}</p>}
              <table className="table-auto w-full overflow-y-auto">
                <thead className="text-sm font-semibold uppercase text-black bg-[#6d9eeb7a]">
                  <tr>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">S.No</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Name</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Date</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Login Time</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Logout Time</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Total Hours of Working</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Status</div>
                    </th>
                    <th scope="col" className="p-2 whitespace-nowrap">
                      <div className="font-semibold text-center">Remark</div>
                    </th>
                  </tr>
                </thead>

                <tbody className="text-sm">
                  {loading ? (
                    <tr>
                      <td colSpan="8" className="p-2 whitespace-nowrap font-inter text-center">
                        <div className="font-medium text-center">Loading...</div>
                      </td>
                    </tr>
                  ) : currentItems.length > 0 ? (
                    currentItems.map((row, index) => (
                      <tr key={index}>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">
                            {index + 1 + (currentPage - 1) * itemsPerPage}.
                          </div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{row.name}</div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{formatDateOnly(row.date)}</div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{formatTime(row.clockin)}</div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{formatTime(row.clockout)}</div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{row.total_hours_worked}</div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{row.status}</div>
                        </td>
                        <td scope="col" className="p-2 whitespace-nowrap">
                          <div className="font-medium text-center">{row.remark}</div>
                        </td>
                      </tr>
                    ))
                  ) : (
                    <tr>
                      <td colSpan="8" className="p-2 whitespace-nowrap">
                        <div className="font-medium text-center">No data available</div>
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div className="mt-2 flex justify-between items-center">
          <div>
            <button
              className="py-1 px-3 bg-blue-500 hover:bg-blue-400 text-white text-sm font-inter rounded-full shadow-lg mr-2"
              onClick={() => paginate(currentPage - 1)}
              disabled={currentPage === 1}
            >
              Previous
            </button>
            <button
              className="py-1 px-3 bg-blue-500 hover:bg-blue-400 text-white text-sm font-inter rounded-full shadow-lg"
              onClick={() => paginate(currentPage + 1)}
              disabled={indexOfLastItem >= filteredData.length}
            >
              Next
            </button>
          </div>
          <div className="text-sm font-semibold text-gray-800">
            Page {filteredData.length > 0 ? currentPage : 0} of{" "}
            {filteredData.length > 0
              ? Math.ceil(filteredData.length / itemsPerPage)
              : 0}
          </div>
          <button
            className="py-2 px-4 bg-blue-600 hover:bg-green-600 text-white text-sm font-inter rounded-md shadow-lg transition-colors flex items-center gap-2"
            onClick={downloadExcel}
            disabled={filteredData.length === 0}
          >
            <FontAwesomeIcon icon={faDownload} /> 
            Download Excel 
          </button>
        </div>
      </div>
    </div>
  );
};

export default Timemanagement;