import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";

function ReportInfo() {
  const [report, setReport] = useState([]);
  const params = useParams();

  useEffect(() => {
    fetch(`https://phase-5-api-o5ni.onrender.com/reports/${params.id}`)
      .then((r) => r.json())
      .then((data) => setReport((report) => (report = data)));
  }, [params.id]);
  return (
    <div className="reportDiv">
      <div className="reportHeaderDiv">
        <h1>Report Tittle</h1>
        <h3>
          {report.type_of_report}- {report.client_name}
        </h3>
        <br></br>
      </div>
      <br></br>
      <div className="contentDiv">
        <h2>Summary/Report</h2>
        <p>{report.context}</p>
      </div>
    </div>
  );
}

export default ReportInfo;
